from pathlib import Path
import sys

# 计算项目根目录的绝对路径（基于此脚本的位置）
_current_file = Path(__file__).resolve()
_utils_dir = _current_file.parent  # utils 目录
_agent_dir = _utils_dir.parent  # agent 目录
_project_root = _agent_dir.parent  # 项目根目录

# 默认日志目录使用绝对路径
log_dir = _project_root / "debug" / "custom"

try:
    from loguru import logger as _logger

    def setup_logger(log_dir: Path = log_dir, console_level: str = "INFO"):
        """
        Set up the logger with optional file logging.

        Args:
            log_file (Path | None): The file path to log to. If None, file logging is disabled.
            log_level (str): The logging level (e.g., "DEBUG", "INFO", "WARNING", "ERROR").
        """
        _logger.remove()  # Remove default logger

        # Add console logger
        _logger.add(
            sys.stderr,
            level=console_level,
            format="[<level>{level}</level>] [<cyan>{module}</cyan>:<cyan>{line}</cyan>] <level>{message}</level>",
        )

        # 确保日志目录存在
        log_dir.mkdir(parents=True, exist_ok=True)

        _logger.add(
            log_dir / "{time:YYYY-MM-DD}.log",
            rotation="00:00",  # Rotate at midnight
            retention="2 weeks",  # Keep logs for 2 weeks
            compression="zip",  # Compress old logs
            level="DEBUG",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{line} - {message}",
            encoding="utf-8",
            enqueue=True,  # Ensure thread safety
            backtrace=True,  # 包含堆栈跟踪
            diagnose=True,  # 显示诊断信息
        )

        return _logger

    def change_console_level(level="DEBUG"):
        """动态修改控制台日志等级"""
        setup_logger(console_level=level)
        _logger.info(f"控制台日志等级已更改为: {level}")

    logger = setup_logger()

except ImportError:
    import logging

    logging.basicConfig(
        format="%(asctime)s | %(levelname)s | %(message)s", level=logging.INFO
    )
    logger = logging
