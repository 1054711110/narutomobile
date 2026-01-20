# 🚀 Maa Auto Naruto 开发环境搭建与开发指南

<div style="background-color:#FFF3CD; color:#856404; padding:15px; border-radius:4px; border:1px solid #FFEAA7;">
  <p style="font-weight:bold; font-size:16px; margin-top:0; display:flex; align-items:center;">
    <span style="margin-right:8px;">⚠️</span>
    <span style="color:#FF0000;">警告：本项目目前的开发文档尚未完善！</span>
  </p>
  <p style="margin-bottom:0;">
    你可以先阅读<a href="https://1999.fan/zh_cn/develop/development.html" style="color:#856404; text-decoration:underline;">M9A 开发须知</a>以了解如何在本地以开发模式运行项目（本项目与M9A的项目结构类似，可以作为学习参考）。更多内容请自行学习MaaFramework的<a href="https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/1.1-%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B.md" style="color:#856404; text-decoration:underline;">开发文档</a>的内容。
  </p>
</div>

---

## 📋 目录

- [1. 开发环境配置 🛠️](#1-开发环境配置)
- [2. Python 安装详情 🐍](#2-python-安装详情)
- [3. 克隆项目代码 📦](#3-克隆项目代码)
- [4. 安装 MaaFramework 依赖 📥](#4-安装-maaframework-依赖)
- [5. 安装 Python 依赖 📋](#5-安装-python-依赖)
- [6. 验证安装 ✅](#6-验证安装)
- [7. 开始开发 💻](#7-开始开发)
- [8. 常见问题与解决方案 ❓](#8-常见问题与解决方案)

---

<h2 id="1-开发环境配置" style="color:#FF6B6B; font-size:20px;">1. 开发环境配置 🛠️</h2>

### <span style="color:#4ECDC4; font-size:18px;">1.1 编辑器推荐</span>

我们<span style="color:#FF6B6B; font-weight:bold;">强烈推荐</span>使用 [VSCode](https://code.visualstudio.com/Download) 进行开发，因为社区提供了优秀的 [Maa Pipeline Support](https://marketplace.visualstudio.com/items?itemName=nekosu.maa-support) VSCode 插件来进行调试。

### <span style="color:#4ECDC4; font-size:18px;">1.2 必要软件安装</span>

1. **安装 VSCode** - 代码编辑器 📝
2. **安装 Git** - 版本控制工具 🔧
3. **安装 Python** - 开发语言（<span style="color:#FF6B6B; font-weight:bold;">≥3.12</span>，推荐使用 <span style="color:#4ECDC4; font-weight:bold;">Python 3.12.9</span> 版本）🐍

### <span style="color:#4ECDC4; font-size:18px;">1.3 可选开发工具</span>

| 工具 | 简介 |
| --- | --- |
| [MaaDebugger](https://github.com/MaaXYZ/MaaDebugger) | 独立调试工具 |
| [Maa Pipeline Support](https://marketplace.visualstudio.com/items?itemName=nekosu.maa-support) | VSCode 插件，提供调试、截图、获取 ROI 、取色等功能 |
| [MFAToolsPlus](https://github.com/SweetSmellFox/MFAToolsPlus) | 独立截图、获取 ROI 及取色工具 |
| [MaaPipelineEditor](https://github.com/kqcoxn/MaaPipelineEditor) | 任务流程pipeline可视化工具 |

---

<h2 id="2-python-安装详情" style="color:#FF6B6B; font-size:20px;">2. Python 安装详情 🐍</h2>

### <span style="color:#4ECDC4; font-size:18px;">2.1 下载 Python</span>

访问华为云镜像站下载 Python：

<p style="background-color:#F8F9FA; padding:15px; border-left:4px solid #4ECDC4; border-radius:4px;">
  📁 <strong>镜像地址：</strong> <a href="https://repo.huaweicloud.com/python/3.12.9/" style="color:#007BFF; text-decoration:none;">https://repo.huaweicloud.com/python/3.12.9/</a><br>
  📥 <strong>推荐下载：</strong> <a href="https://repo.huaweicloud.com/python/3.12.9/python-3.12.9.exe" style="color:#007BFF; text-decoration:none;">https://repo.huaweicloud.com/python/3.12.9/python-3.12.9.exe</a>
</p>

### <span style="color:#4ECDC4; font-size:18px;">2.2 安装 Python</span>

运行下载的 Python 安装程序，<span style="background-color:#FFF3CD; padding:2px 8px; border-radius:4px; font-weight:bold; color:#856404;">强烈建议</span>勾选 "Add Python to PATH" 选项，然后按照默认设置完成安装。

---

<h2 id="3-克隆项目代码" style="color:#FF6B6B; font-size:20px;">3. 克隆项目代码 📦</h2>

使用 Git 克隆项目代码到本地：

```bash
git clone https://github.com/duorua/narutomobile.git
cd narutomobile
```

<div style="background-color:#E8F5E9; padding:10px; border-radius:4px; margin-top:10px;">
  <strong style="color:#2E7D32;">💡 提示：</strong> 确保您已经安装了 Git 工具，否则无法执行上述命令。
</div>

---

<h2 id="4-安装-maaframework-依赖" style="color:#FF6B6B; font-size:20px;">4. 安装 MaaFramework 依赖 🛠️</h2>

MaaFramework 依赖可以通过以下三种方式之一安装：

### <span style="color:#4ECDC4; font-size:18px;">3.1 方式一：直接下载发布包</span>

1. 🌐 访问 [MaaFramework 发布页面](https://github.com/MaaXYZ/MaaFramework/releases)
2. 📥 下载最新版本的发布包
3. 📂 将下载的文件解压到项目根目录下的 `deps` 文件夹中

### <span style="color:#4ECDC4; font-size:18px;">3.2 方式二：使用下载脚本 <span style="color:#FFD166; font-weight:bold;">(推荐)</span></span>

在项目根目录下执行以下命令：

```bash
python tools\download_maafw.py
```

### <span style="color:#4ECDC4; font-size:18px;">3.3 方式三：使用 Git Submodule</span>

在项目根目录下执行以下命令：

```bash
git submodule update --init --recursive
```

---

<h2 id="5-安装-python-依赖" style="color:#FF6B6B; font-size:20px;">5. 安装 Python 依赖 📋</h2>

使用 pip 安装项目所需的 Python 依赖：

```bash
# 创建虚拟环境（可选但推荐）
python -m venv .venv
.venv\Scripts\activate  # Windows 系统
# source .venv/bin/activate  # Linux/macOS 系统

# 安装依赖
pip install -r requirements.txt
```

<div style="background-color:#F8F9FA; padding:15px; border-radius:4px; margin-top:10px;">
  <strong style="color:#495057;">📝 说明：</strong> <br>
  - 虚拟环境可以隔离项目依赖，避免与系统 Python 环境冲突<br>
  - 如果不使用虚拟环境，可以直接执行 `pip install -r requirements.txt`
</div>

---

<h2 id="6-验证安装" style="color:#FF6B6B; font-size:20px;">6. 验证安装 ✅</h2>

安装完成后，可以运行项目来验证是否安装成功：

```bash
python -m agent.main (这里加上narutomobile\assets\interface里的identifier)
```

<span style="color:#06D6A0; font-weight:bold; font-size:16px;">✓ 如果能够正常启动，说明开发环境已经搭建完成！</span>

---

<h2 id="7-开始开发" style="color:#FF6B6B; font-size:20px;">7. 开始开发 💻</h2>

### <span style="color:#4ECDC4; font-size:18px;">7.1 入门指南</span>

1. 📚 阅读 [M9A 开发须知](https://1999.fan/zh_cn/develop/development.html)，了解如何在本地以开发模式运行本项目（本项目与M9A的项目结构类似，可以作为学习参考）。

2. 🎯 如果不会写代码，但对某些功能的实现有明确的思路：
   - 参考 [任务流水线（Pipeline）协议](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/3.1-%E4%BB%BB%E5%8A%A1%E6%B5%81%E6%B0%B4%E7%BA%BF%E5%8D%8F%E8%AE%AE.md) 学习如何将思路转化为具体实现
   - 了解如何在 `assets\resource\base\pipeline` 中编写流水线文件
   - 学习 [Project Interface 协议](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/3.2-ProjectInterface%E5%8D%8F%E8%AE%AE.md#project-interface-%E5%8D%8F%E8%AE%AE)，了解如何让软件能够调用你写的流水线文件

3. 💻 如果你有一定的 Python 基础，想要尝试为项目编写代码：
   - 阅读 [MaaFramework 集成接口](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/2.2-%E9%9B%86%E6%88%90%E6%8E%A5%E5%8F%A3%E4%B8%80%E8%A7%88.md) 并<span style="color:#FF6B6B; font-weight:bold;">结合本项目源码</span>以了解如何为项目开发高级功能
   - <span style="background-color:#FFF3CD; padding:2px 8px; border-radius:4px; font-weight:bold; color:#856404;">重要提示</span>：纸上学来终觉浅，绝知此事要躬行。不结合代码实践读文档，等于白读。

4. 🤝 为项目贡献你所编写的内容，请参考 [牛牛也能看懂的 GitHub Pull Request 使用指南](https://maa.plus/docs/zh-cn/develop/pr-tutorial.html)

---

<h2 id="8-常见问题与解决方案" style="color:#FF6B6B; font-size:20px;">8. 常见问题与解决方案 ❓</h2>

### <span style="color:#4ECDC4; font-size:18px;">6.1 Python 安装问题</span>

1. **错误**：安装完成后无法在命令行中使用 python 命令
   **解决方案**：重新安装 Python，确保勾选了 "Add Python to PATH" 选项

2. **错误**：提示 Python 版本过低
   **解决方案**：卸载当前版本，下载并安装 Python 3.12.9 或更高版本

### <span style="color:#4ECDC4; font-size:18px;">6.2 Git 克隆问题</span>

1. **错误**：git 命令无法识别
   **解决方案**：安装 Git 工具，下载地址：[https://git-scm.com/downloads](https://git-scm.com/downloads)

2. **错误**：克隆速度缓慢
   **解决方案**：使用国内镜像地址或更换网络环境

### <span style="color:#4ECDC4; font-size:18px;">6.3 MaaFramework 依赖问题</span>

1. **错误**：`python tools\download_maafw.py` 命令执行失败
   **解决方案**：检查网络连接，确保可以访问 GitHub

2. **错误**：提示找不到 `deps` 目录
   **解决方案**：手动创建 `deps` 目录，然后重新执行安装命令

### <span style="color:#4ECDC4; font-size:18px;">6.4 Python 依赖问题</span>

1. **错误**：pip 命令执行失败
   **解决方案**：确保 Python 已正确安装并添加到 PATH

2. **错误**：安装依赖时提示权限不足
   **解决方案**：在命令前添加 `--user` 参数，或使用管理员权限运行命令行

3. **错误**：提示找不到 `requirements.txt` 文件
   **解决方案**：确保当前目录是项目根目录

### <span style="color:#4ECDC4; font-size:18px;">6.5 运行项目问题</span>

1. **错误**：提示 "Failed to load det or rec", "ocrer is null"
   **解决方案**：确保 MaaFramework 依赖已正确安装，且 OCR 模型文件完整

2. **错误**：提示找不到模块
   **解决方案**：检查是否已正确激活虚拟环境（如果使用了虚拟环境），或重新安装依赖

### <span style="color:#4ECDC4; font-size:18px;">8.6 开发相关问题</span>

1. **问题**：我在这个仓库里提了 Issue 很久没人回复
   **解决方案**：本项目目前紧缺人手，你可以先阅读文档自行尝试寻找解决方案。欢迎提交 PR 贡献代码！

2. **问题**：OCR 文字识别一直没有识别结果，报错 "Failed to load det or rec", "ocrer is null"
   **解决方案**：请确保已正确执行所有安装步骤，且 MaaFramework 依赖已正确安装。详细检查 OCR 模型文件是否完整。

---

## 🎉 完成！

您已经成功搭建了 Maa Auto Naruto 的开发环境！

如果您在使用过程中遇到其他问题，请参考：
- [项目常见问题](guide/faq.md)
- [MaaFramework 官方文档](https://maafw.xyz/)

祝您开发愉快！🚀
