from typing import Iterable
from time import sleep
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
    screenshot_refresh=True,
) -> RectType | None:
    """重新截图并进行 OCR 识别"""
    if screenshot_refresh:
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
        if isinstance(expected, Iterable):
            expected = expected[0]

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


def fast_swipe(
    context: Context,
    start_x: int,
    start_y: int,
    end_x: int,
    end_y: int,
    duration: int = 300,
    end_hold: bool = True,
    after_swipe_delay: int = 300,
):
    """
    快速滑动屏幕
    :param context: 上下文对象
    :param start_x: 起始点X坐标
    :param start_y: 起始点Y坐标
    :param end_x: 终点X坐标
    :param end_y: 终点Y坐标
    :param duration: 滑动持续时间，不建议低于200，单位毫秒
    :param end_hold: 滑动结束后是否急停，防止惯性滑动
    :param after_swipe_delay: 滑动完成后的延迟时间，单位毫秒

    如果要防止滑动动画存在惯性，end_hold参数需设置为0
    反之，如果要利用惯性滑动，需要将end_hold设为非0值
    """
    logger.debug(f"start swipe from ({start_x}, {start_y}) to ({end_x}, {end_y})")
    logger.debug(f"end hold: {end_hold}ms")
    # 1. 按下起始点
    controller = context.tasker.controller
    controller.post_touch_down(start_x, start_y).wait()

    # 2. 计算平滑移动间隔
    interval = 5
    total_steps = duration // interval
    x_step = (end_x - start_x) / total_steps
    y_step = (end_y - start_y) / total_steps

    # 3. 逐步移动
    for step in range(1, total_steps + 1):
        current_x = int(start_x + step * x_step)
        current_y = int(start_y + step * y_step)
        controller.post_touch_move(current_x, current_y).wait()

    # 4. 释放触摸
    if end_hold:
        sleep(0.3)
    controller.post_touch_up().wait()
    sleep(after_swipe_delay / 1000)
