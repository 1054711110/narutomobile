from zipfile import ZipFile
import json
import sys
from pathlib import Path
import argparse
import shutil
import subprocess
import urllib.request as request


sys.path.insert(0, Path(__file__).parent.__str__())
sys.path.insert(0, (Path(__file__).parent / "ci").__str__())

from ci.install import (
    get_dotnet_platform_tag,
    install_maafw,
    install_resource,
    install_agent,
)
from ci.setup_embed_python import PYTHON_VERSION_TARGET
from setup_full_python import download_file

DEFAULT_MFA_VERSION = "v2.2.2"
GHPROXY_URL = "https://gh-proxy.natsuu.top/"

parser = argparse.ArgumentParser(
    description="Install MaaFramework to install directory"
)
parser.add_argument(
    "--install_dir", type=str, default="install", help="Install directory"
)
parser.add_argument(
    "--arch", type=str, default="amd64", help="Architecture (amd64 or win32)"
)
parser.add_argument(
    "--pre-release", type=bool, default=False, help="Install pre-release version"
)
parser.add_argument(
    "--ghproxy",
    type=bool,
    default=True,
    help="Use ghproxy to download from github",
)
parser.add_argument("--install-python", type=bool, default=True, help="Install Python")
parser.add_argument("--clean", type=bool, default=False, help="Clean install directory")
parser.add_argument(
    "--mfa_version",
    type=str,
    default=DEFAULT_MFA_VERSION,
    help="MFA version to install",
)

args = parser.parse_args()

TEMP_DIR = Path("temp")

# clean install directory
if args.clean:
    print(f"开始清理目录：{args.install_dir}")
    if Path(args.install_dir).exists():
        shutil.rmtree(args.install_dir)


# setup python environment
def setup_python():
    print(f"开始设置Python环境")
    TEMP_DIR.mkdir(exist_ok=True)

    print(f"下载python并解压...")
    cmd = [
        "python",
        "tools/setup_full_python.py",
        "--tmp_dir",
        TEMP_DIR,
    ]

    try:
        subprocess.run(cmd, check=True)
    except (subprocess.CalledProcessError, OSError) as e:
        print(f"Failed to install Python: {e}")
        sys.exit(1)

    # install Python dependents
    print("开始安装python依赖")
    cmd = [
        "python",
        "-m",
        "pip",
        "install",
        "-r",
        "./requirements.txt",
        "-t",
        "install/python/Lib/",
    ]

    try:
        subprocess.run(cmd, check=True)
    except (subprocess.CalledProcessError, OSError) as e:
        print(f"Failed to install Python: {e}")
        sys.exit(1)


# install MFA
def download_mfa_release(version, archive_name, cache_path):
    print(f"开始下载：{archive_name}")
    url = f"https://github.com/SweetSmellFox/MFAAvalonia/releases/download/{version}/{archive_name}"
    if args.ghproxy:
        url = GHPROXY_URL + url

    print(f"Downloading from {url}...")
    download_file(url, cache_path)


def install_mfa():
    arch = get_dotnet_platform_tag()

    if args.mfa_version:
        version = args.mfa_version
    else:
        print("尝试获取MFA版本信息")
        RELEASE_API = "https://api.github.com/repos/SweetSmellFox/MFAAvalonia/releases"
        response = request.urlopen(RELEASE_API)
        if response.status != 200:
            if response.status == 403:
                print("Rate limit exceeded")
                print(
                    "Please check the proxy settings or use tag argument to install specific version"
                )
                sys.exit(1)
            print(f"Failed to get release info: {response.status}")
            sys.exit(1)

        release_info = json.loads(response.read())
        if args.pre_release:
            pass
        else:
            release_info = [
                release for release in release_info if not release["prerelease"]
            ]

        release_info = release_info[0]
        version = release_info["tag_name"]

    archive_name = f"MFAAvalonia-{version}-{arch}.zip"
    cache_path = TEMP_DIR / archive_name
    if not cache_path.exists():
        download_mfa_release(version, archive_name, cache_path)
    else:
        print(f"MFAAvalonia-{version}-{arch}.zip already exists.")
        size = cache_path.stat().st_size
        MB = 1024 * 1024
        if size < 50 * MB:
            print(f"文件大小为：{size / 1024 / 1024}MB")
            print("文件大小小于50MB，可能下载不完整，重新下载...")
            cache_path.unlink()
            download_mfa_release(version, archive_name, cache_path)
            size = cache_path.stat().st_size
            MB = 1024 * 1024
            if size < 50 * MB:
                print(f"文件大小为：{size / 1024 / 1024}MB")
                print("文件大小仍然小于50MB，下载失败，退出安装")
                sys.exit(1)

    with ZipFile(cache_path, "r") as zip_ref:
        zip_ref.extractall(args.install_dir)


def main():
    print("开始本地构建流程")
    print("设置Python环境...")
    setup_python()
    print("MFAA环境")
    install_mfa()
    print("安装MaaFramework...")
    install_maafw()
    print("安装资源文件...")
    install_resource()
    print("安装Agent...")
    install_agent()


if __name__ == "__main__":
    main()
