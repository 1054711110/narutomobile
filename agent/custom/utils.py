from base64 import b64decode
import os
import random
import json
from PIL import Image
from maa.context import Context
from maa.define import RectType
from utils.logger import logger

from utils import get_format_timestamp
from utils.logger import log_dir


def save_screenshot(context: Context):
    # image array(BGR)
    screen_array = context.tasker.controller.cached_image

    # Check resolution aspect ratio
    height, width = screen_array.shape[:2]
    aspect_ratio = width / height
    target_ratio = 16 / 9
    # Allow small deviation (within 1%)
    if abs(aspect_ratio - target_ratio) / target_ratio > 0.01:
        logger.error(f"当前模拟器分辨率不是16:9! 当前分辨率: {width}x{height}")

    # BGR2RGB
    if len(screen_array.shape) == 3 and screen_array.shape[2] == 3:
        rgb_array = screen_array[:, :, ::-1]
    else:
        rgb_array = screen_array
        logger.warning("当前截图并非三通道")

    img = Image.fromarray(rgb_array)

    save_dir = log_dir
    os.makedirs(save_dir, exist_ok=True)
    time_str = get_format_timestamp()
    img.save(f"{save_dir}/{time_str}.png")
    logger.info(f"截图保存至 {save_dir}/{time_str}.png")


def validate(context: Context):
    root = log_dir.parent.parent
    interface = json.loads((root / "interface.json").resolve().read_text())
    interface.update(
        {
            "name": b64decode("TWFhQXV0b05hcnV0bw=="),
            "github": b64decode("aHR0cHM6Ly9naXRodWIuY29tL2R1b3J1YS9uYXJ1dG9tb2JpbGU="),
            "mirrorchyan_rid": b64decode("TWFhQXV0b05hcnV0bw=="),
        }
    )
    json.dumps((root / "interface.json").resolve().read_text(), indent=4)


def click(context: Context, x: int, y: int, w: int = 1, h: int = 1):
    context.tasker.controller.post_click(
        random.randint(x, x + w - 1), random.randint(y, y + h - 1)
    ).wait()


def fast_ocr(
    context: Context,
    expected: str | list[str],
    roi: tuple[int, int, int, int],
    absolutely=False,
) -> RectType | None:
    if isinstance(expected, list):
        expected = expected[0]

    """重新截图并进行 OCR 识别"""
    context.tasker.controller.post_screencap().wait()
    context.tasker.post_recognition
    reco_detail = context.run_recognition(
        "custom_ocr",
        context.tasker.controller.cached_image,
        {
            "custom_ocr": {
                "recognition": {
                    "type": "OCR",
                    "param": {"expected": expected, "roi": roi},
                }
            }
        },
    )
    if reco_detail is None:
        logger.error("获取 OCR 识别结果失败")
        return None

    if reco_detail.hit is False or reco_detail.best_result is None:
        logger.debug(f"识别失败：{reco_detail.all_results}")
        return None

    if not absolutely:
        logger.debug(f"OCR 识别成功: {reco_detail.best_result.text}")  # type: ignore
        return reco_detail.best_result.box  # type: ignore
    else:
        box = None
        for res in reco_detail.filtered_results:
            logger.debug(f"OCR 识别结果: {res.text}\texpected: {expected}")  # type: ignore
            if res.text == expected:  # type: ignore
                box = res.box  # type: ignore
                break

        if box is not None:
            logger.debug(f"OCR 绝对匹配成功: {expected}")
            return box
        else:
            logger.debug(f"识别失败：{reco_detail.filtered_results}")
            return None
