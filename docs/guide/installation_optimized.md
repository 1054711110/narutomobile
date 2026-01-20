<h1 style="color:#3366FF; text-align:center; font-size:28px; margin-bottom:30px; font-weight:bold;">🚀 开发环境搭建</h1>

---

## <span style="color:#FF6B6B;">1. 安装 Python 🐍</span>

首先需要安装 Python 环境，<span style="color:#FF6B6B; font-weight:bold;">推荐使用 Python 3.12.9 版本</span>。

### <span style="color:#4ECDC4;">下载 Python</span>

访问华为云镜像站下载 Python：

- 📁 镜像地址：[https://repo.huaweicloud.com/python/3.12.9/](https://repo.huaweicloud.com/python/3.12.9/)
- 📥 推荐下载：[https://repo.huaweicloud.com/python/3.12.9/python-3.12.9.exe](https://repo.huaweicloud.com/python/3.12.9/python-3.12.9.exe)

### <span style="color:#4ECDC4;">安装 Python</span>

运行下载的 Python 安装程序，<span style="background-color:#FFF3CD; padding:2px 8px; border-radius:4px; font-weight:bold;">强烈建议</span>勾选 "Add Python to PATH" 选项，然后按照默认设置完成安装。

---

## <span style="color:#FF6B6B;">2. 克隆项目代码 📦</span>

使用 Git 克隆项目代码到本地：

```bash
git clone https://github.com/duorua/narutomobile.git
cd narutomobile
```

---

## <span style="color:#FF6B6B;">3. 安装 MaaFramework 依赖 🛠️</span>

MaaFramework 依赖可以通过以下两种方式之一安装：

### <span style="color:#4ECDC4;">方式一：直接下载发布包</span>

1. 🌐 访问 [MaaFramework 发布页面](https://github.com/MaaXYZ/MaaFramework/releases)
2. 📥 下载最新版本的发布包
3. 📂 将下载的文件解压到项目根目录下的 `deps` 文件夹中

### <span style="color:#4ECDC4;">方式二：使用下载脚本 <span style="color:#FFD166; font-weight:bold;">(推荐)</span></span>

在项目根目录下执行以下命令：

```bash
python tools\download_maafw.py
```

---

## <span style="color:#FF6B6B;">4. 安装 Python 依赖 📋</span>

使用 pip 安装项目所需的 Python 依赖：

```bash
# 创建虚拟环境（可选但推荐）
python -m venv .venv
.venv\Scripts\activate  # Windows 系统
# source .venv/bin/activate  # Linux/macOS 系统

# 安装依赖
pip install -r requirements.txt
```

---

## <span style="color:#FF6B6B;">5. 验证安装 ✅</span>

安装完成后，可以运行项目来验证是否安装成功：

```bash
python -m agent.main (这里加上narutomobile\assets\interface里的identifier)
```

<span style="color:#06D6A0; font-weight:bold;">✓ 如果能够正常启动，说明开发环境已经搭建完成！</span>

---

## <span style="color:#FF6B6B;">常见问题 ❓</span>

如果遇到问题，请参考：

- 📖 [项目常见问题](../../guide/faq.md)
- 📚 [MaaFramework 官方文档](https://maafw.xyz/)
