# -*- coding: utf-8 -*-

# M9A
# https://github.com/MAA1999/M9A
# AGPL-3.0 License

import os
import sys
import json
import subprocess
from pathlib import Path

# utf-8
sys.stdout.reconfigure(encoding="utf-8")  # type: ignore

# 获取当前main.py路径并设置上级目录为工作目录
current_file_path = Path(__file__).resolve()  # 当前脚本的绝对路径
current_script_dir = current_file_path.parent  # 包含此脚本的目录
project_root_dir = current_script_dir.parent  # 假定的项目根目录

# 更改CWD到项目根目录
if Path.cwd() != project_root_dir:
    os.chdir(project_root_dir)
print(f"set cwd: {Path.cwd()}")

# 将脚本自身的目录添加到sys.path，以便导入utils、maa等模块
if current_script_dir.__str__() not in sys.path:
    sys.path.insert(0, current_script_dir.__str__())

from utils.logger import logger  # type: ignore

VENV_NAME = ".venv"  # 虚拟环境目录的名称
VENV_DIR = Path(project_root_dir) / VENV_NAME

### 虚拟环境相关 ###


def _is_running_in_our_venv():
    """检查脚本是否在此脚本管理的特定venv中运行。"""
    current_python = Path(sys.executable).resolve()

    logger.debug(f"当前Python解释器: {current_python}")

    if sys.platform.startswith("win"):
        # Windows: 如果在虚拟环境中，Python应该在 Scripts 目录下
        if current_python.parent.name == "Scripts":
            return True
        else:
            logger.debug("当前不在目标虚拟环境中")
            return False
    else:
        # Linux/Unix: 如果在虚拟环境中，Python应该在 bin 目录下
        if current_python.parent.name == "bin":
            return True
        else:
            logger.debug("当前不在目标虚拟环境中")
            return False


def ensure_venv_and_relaunch_if_needed():
    """
    确保venv存在，并且如果尚未在脚本管理的venv中运行，
    则在其中重新启动脚本。支持Linux和Windows系统。
    """
    logger.info(f"检测到系统: {sys.platform}。当前Python解释器: {sys.executable}")

    if _is_running_in_our_venv():
        logger.info(f"已在目标虚拟环境 ({VENV_DIR}) 中运行。")
        return

    if not VENV_DIR.exists():
        logger.info(f"正在 {VENV_DIR} 创建虚拟环境...")
        try:
            # 使用当前运行此脚本的Python（系统/外部Python）
            subprocess.run(
                [sys.executable, "-m", "venv", str(VENV_DIR)],
                check=True,
                capture_output=True,
            )
            logger.info(f"创建成功")
        except subprocess.CalledProcessError as e:
            logger.error(
                f"创建失败: {e.stderr.decode(errors='ignore') if e.stderr else e.stdout.decode(errors='ignore')}"
            )
            logger.error("正在退出")
            sys.exit(1)
        except FileNotFoundError:
            logger.error(
                f"命令 '{sys.executable} -m venv' 未找到。请确保 'venv' 模块可用。"
            )
            logger.error("无法在没有虚拟环境的情况下继续。正在退出。")
            sys.exit(1)

    if sys.platform.startswith("win"):
        python_in_venv = VENV_DIR / "Scripts" / "python.exe"
    else:
        python3_path = VENV_DIR / "bin" / "python3"
        python_path = VENV_DIR / "bin" / "python"
        if python3_path.exists():
            python_in_venv = python3_path
        elif python_path.exists():
            python_in_venv = python_path
        else:
            python_in_venv = python3_path  # 默认使用python3，让后续错误处理捕获

    if not python_in_venv.exists():
        logger.error(f"在虚拟环境 {python_in_venv} 中未找到Python解释器。")
        logger.error("虚拟环境创建可能失败或虚拟环境结构异常。")
        sys.exit(1)

    logger.info(f"正在使用虚拟环境Python重新启动")

    try:
        cmd = [str(python_in_venv)] + sys.argv
        logger.info(f"执行命令: {' '.join(cmd)}")

        result = subprocess.run(
            cmd,
            cwd=os.getcwd(),
            env=os.environ.copy(),
            check=False,  # 不在非零退出码时抛出异常
        )
        # 退出时使用子进程的退出码
        sys.exit(result.returncode)

    except Exception as e:
        logger.exception(f"在虚拟环境中重新启动脚本失败: {e}")
        sys.exit(1)


### 配置相关 ###


def read_interface_version(interface_file_name="./interface.json") -> str:
    interface_path = Path(project_root_dir) / interface_file_name
    assets_interface_path = Path(project_root_dir) / "assets" / interface_file_name

    target_path = None
    if interface_path.exists():
        target_path = interface_path
    elif assets_interface_path.exists():
        return "DEBUG"

    if target_path is None:
        logger.warning("未找到interface.json")
        return "unknown"

    try:
        with open(target_path, "r", encoding="utf-8") as f:
            interface_data = json.load(f)
            return interface_data.get("version", "unknown")
    except Exception:
        logger.exception(f"读取interface.json版本失败，文件路径：{target_path}")
        return "unknown"


### 依赖安装相关 ###


def _run_pip_command(cmd_args: list, operation_name: str) -> bool:
    try:
        logger.info(f"开始 {operation_name}")
        logger.debug(f"执行命令: {' '.join(cmd_args)}")

        # 使用subprocess.Popen进行实时输出
        process = subprocess.Popen(
            cmd_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # 将stderr重定向到stdout
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,  # 行缓冲
            universal_newlines=True,
        )

        # 收集所有输出用于日志记录
        all_output = []

        # 实时读取并显示输出
        for line in iter(process.stdout.readline, ""):  # type: ignore
            line = line.rstrip("\n\r")
            if line.strip():  # 只显示非空行
                logger.debug(line)  # 实时显示到终端
                all_output.append(line)  # 收集到列表中

        # 等待进程结束
        return_code = process.wait()

        # 记录完整输出到日志
        if all_output:
            full_output = "\n".join(all_output)
            logger.debug(f"{operation_name} 输出:\n{full_output}")

        if return_code == 0:
            logger.info(f"{operation_name} 完成")
            return True
        else:
            logger.error(f"{operation_name} 时出错。返回码: {return_code}")
            return False

    except Exception as e:
        logger.exception(f"{operation_name} 时发生未知异常: {e}")
        return False


### 核心业务 ###


def agent(is_dev_mode=False):
    global logger  # 声明使用全局 logger
    try:
        # 清理模块缓存
        utils_modules = [
            name for name in list(sys.modules.keys()) if name.startswith("utils")
        ]
        for module_name in utils_modules:
            del sys.modules[module_name]

        # 动态导入 utils 的所有内容
        import utils  # type: ignore
        import importlib

        importlib.reload(utils)

        # 重新导入 logger，确保使用新初始化的实例
        from utils.logger import logger as new_logger  # type: ignore

        # from utils.logger import logger  # type: ignore

        logger = new_logger

        if is_dev_mode:
            from utils.logger import change_console_level  # type: ignore

            change_console_level("DEBUG")
            logger.info("开发模式：日志等级已设置为DEBUG")

        try:
            from maa.agent.agent_server import AgentServer
            from maa.toolkit import Toolkit

            import custom  # type: ignore
        except ImportError as e:
            logger.error(e)
            logger.error("Failed to import modules")
            logger.error("Please try to run dependency deployment script first")
            logger.error("导入模块失败！")
            logger.error("请先尝试运行依赖部署脚本")

            return

        Toolkit.init_option("./")

        if len(sys.argv) < 2:
            logger.error("缺少必要的 socket_id 参数")
            return

        socket_id = sys.argv[-1]
        logger.info(f"socket_id: {socket_id}")

        AgentServer.start_up(socket_id)
        logger.info("AgentServer启动")
        AgentServer.join()
        AgentServer.shut_down()
        logger.info("AgentServer关闭")
    except ImportError as e:
        logger.error(f"导入模块失败: {e}")
        logger.error("考虑重新配置环境")
        sys.exit(1)
    except Exception as e:
        logger.exception("agent运行过程中发生异常")
        raise


### 程序入口 ###


def main():
    current_version = read_interface_version()
    is_dev_mode = current_version == "DEBUG"

    # 如果是Linux系统或开发环境，启动虚拟环境
    if sys.platform.startswith("linux") or is_dev_mode:
        ensure_venv_and_relaunch_if_needed()

    if is_dev_mode:
        os.chdir(Path("./assets"))
        logger.info(f"set cwd: {os.getcwd()}")

    agent(is_dev_mode=is_dev_mode)


if __name__ == "__main__":
    main()
