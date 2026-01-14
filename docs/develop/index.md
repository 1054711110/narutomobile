# 开发文档

:::warning

本项目目前的开发文档尚未完善！

你可以先阅读[M9A 开发须知](https://1999.fan/zh_cn/develop/development.html)以了解如何在本地以开发模式运行项目（本项目与M9A的项目结构类似，可以作为学习参考）。更多内容请自行学习MaaFramework的[开发文档](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/1.1-%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B.md)的内容。

:::

## 环境配置

我们强烈推荐您使用[VSCode](https://code.visualstudio.com/Download)进行开发，因为社区提供了优秀的[Maa Pipeline Support](https://marketplace.visualstudio.com/items?itemName=nekosu.maa-support) VSCode 插件来进行调试。同时，你还能在项目的推荐插件列表来获取我们推荐使用的插件。

- 安装vscode
- 安装git
- 安装 python（≥3.12）
- 选择性安装调试/开发工具

    | 工具 | 简介 |
    | --- | --- |
    | [MaaDebugger](https://github.com/MaaXYZ/MaaDebugger) | 独立调试工具 |
    | [Maa Pipeline Support](https://marketplace.visualstudio.com/items?itemName=nekosu.maa-support) | VSCode 插件，提供调试、截图、获取 ROI 、取色等功能 |
    | [MFAToolsPlus](https://github.com/SweetSmellFox/MFAToolsPlus) | 独立截图、获取 ROI 及取色工具 |
    | [MaaPipelineEditor](https://github.com/kqcoxn/MaaPipelineEditor) | 任务流程pipeline可视化工具 |

## 开始开发

1. 阅读[M9A 开发须知](https://1999.fan/zh_cn/develop/development.html)，了解如何在本地以开发模式运行本项目（本项目与M9A的项目结构类似，可以作为学习参考）。

2. 如果不会写代码，但对某些功能的实现有明确的思路可以参考
[任务流水线（Pipeline）协议](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/3.1-%E4%BB%BB%E5%8A%A1%E6%B5%81%E6%B0%B4%E7%BA%BF%E5%8D%8F%E8%AE%AE.md)以学习如何将思路转化为具体实现，并通过这个去了解如何在`assets\resource\base\pipeline`中编写流水线文件。然后学习[Project Interface 协议](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/3.2-ProjectInterface%E5%8D%8F%E8%AE%AE.md#project-interface-%E5%8D%8F%E8%AE%AE)，了解如何让软件能够调用你写的流水线文件。

3. 我有一定的Python基础，想要尝试为项目编写代码。可以阅读
[MaaFramework 继承接口](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/2.2-%E9%9B%86%E6%88%90%E6%8E%A5%E5%8F%A3%E4%B8%80%E8%A7%88.md)并**结合本项目源码**以了解如何为项目开发高级功能。**纸上学来终觉浅，绝知此事要躬行。不结合代码实践读文档，等于白读。**

4. 为项目贡献你所编写的内容，请参考[牛牛也能看懂的 GitHub Pull Request 使用指南](https://maa.plus/docs/zh-cn/develop/pr-tutorial.html)

## FAQ

### 1. 我在这个仓库里提了 Issue 很久没人回复

本项目目前紧缺人手，你可以先阅读文档自行尝试寻找解决方案。欢迎可以提交pr。

### 2. OCR 文字识别一直没有识别结果，报错 "Failed to load det or rec", "ocrer is null"

你不但没有仔细阅读MaaFramework的开发文档，还无视了前面步骤的报错。我不想解释了，请再把文档仔细阅读一遍！
