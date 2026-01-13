from maa.context import Context
from maa.define import RectType
from utils.logger import logger


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
        logger.info(f"OCR 识别成功: {reco_detail.best_result.text}")  # type: ignore
        return reco_detail.best_result.box  # type: ignore
    else:
        box = None
        for res in reco_detail.filtered_results:
            logger.debug(f"OCR 识别结果: {res.text}\texpected: {expected}")  # type: ignore
            if res.text == expected:  # type: ignore
                box = res.box  # type: ignore
                break

        if box is not None:
            logger.info(f"OCR 绝对匹配成功: {expected}")
            return box
        else:
            logger.debug(f"识别失败：{reco_detail.filtered_results}")
            return None
