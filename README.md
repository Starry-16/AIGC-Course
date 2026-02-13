# 🦜 AIGC课程代码仓库

## 📖 参考图书 
O’Reilly 出版图书 《Generative Deep Learning: Teaching Machines to Paint, Write, Compose and Play》（生成式深度学习：教会机器绘画、写作、作曲与博弈）第二版

[O’Reilly 官方链接](https://www.oreilly.com/library/view/generative-deep-learning/9781098134174/)

<img src="img/book_cover.png" width="300px">

## 🪶 课程列表

以下是本书的章节结构概览：
| 序号 | 内容 | 参考代码 |
|:----:|:----:|:----:|
| 1 | AIGC概述                | 无 |
| 2 | 深度学习与概率论基础      | [deeplearning](./notebooks/02_deeplearning) |
| 3 | VAE                     | [vea](./notebooks/03_vae) |
| 4 | GAN                     | [gan](./notebooks/04_gan)  |
| 5 | Diffusion               | [diffusion](./notebooks/08_diffusion)  |
| 6 | 自回归模型               | [autoregressive](./notebooks/05_autoregressive)  |
| 7 | 大语言模型               | [transformer](./notebooks/09_transformer)  |
| 8 | 多模态大语言模型          | 无 |
| 9 | 视觉生成模型             | 无 |
| 10 | AIGC模型的安全与伦理问题 | 无 |
| 11 | 课程项目展示与评估       | 无 |

## 🚀 快速开始

### 工具的配置与安装教程
python、VSCode、Pytorch、Jupyter的安装教程见[安装操作手册](./doc)

### Kaggle API

为了下载书中使用的一些数据集，你需要一个 Kaggle 账号以及 API Token。使用 Kaggle API 的步骤如下：

1. 注册一个 [Kaggle 账号](https://www.kaggle.com).
2. 进入个人主页的 Account（账户）标签页
3. 点击 Create API Token，这将下载一个名为 'kaggle.json' 的文件，其中包含你的 API 凭据
4. 将上一步下载的kaggle.json文件放在C:\Users\zhao(你自己的用户名)\.kaggle目录下


## 🏞️ 数据下载

本代码仓库内置了一个数据下载辅助脚本。

运行以下命令，并从下列数据集名称中选择一个：

```
python scripts/download.py faces（要下载的数据集种类） [faces, bricks, recipes, flowers, wines, cellosuites, chorales]
```


## 📦 课程大作业考核要求

### 📌 项目目标

每个小组需基于 **深度神经网络技术**，设计并实现一个具有创新性的 **AIGC（AI-Generated Content）应用**。

---

### 👥 组织形式

- 每组 5–6 人

---

### ✅ 基本要求
- 必须基于 AIGC 模型（例如：GAN、VAE、Diffusion Models 等）
- 提供完整的：
  - 源代码
  - 训练好的模型文件
  - 运行与使用说明文档


### 📌 具体任务说明

项目应用需具备以下特点之一：

### 1️⃣ 创造性生成（Creative Generation）

基于生成模型，在特定领域生成全新的内容，例如：

- 🎨 服装设计生成
- 🎵 音乐生成
- 🖼️ 插画 / 艺术作品生成
- 🏠 室内设计生成
- 📚 文本内容创作

---

### 2️⃣ 智能编辑（Intelligent Editing）

对输入内容进行增强、修复或风格化处理，例如：

- 🖌️ 图像风格迁移
- 🧩 图像修复 / 超分辨率重建
- 🎬 视频增强
- 🎙️ 语音去噪或转换
- ✍️ 文本润色与改写

---

### 3️⃣ 模型改进与创新应用

- 对已有 AIGC 模型进行结构改进或优化
- 在特定应用场景中进行模型微调与创新应用
- 多模型融合（如 GAN + Diffusion 结合）

---

## 💡 候选项目题目示例

以下为参考选题方向（可自行选题与扩展）：

- 🎨 基于 Diffusion 的个性化服装设计生成系统  
- 🖼️ 艺术风格图像生成与交互式风格迁移网页  
- 📷 老照片智能修复与对比展示系统  
- 🎵 AI 音乐生成与情绪控制系统  
- 🏠 基于文本描述的室内设计生成系统  
- 📚 AI 小说片段生成与续写系统  
- 🧑‍🎨 多模态艺术创作平台（文本 → 图像）

---

## 🌐 可视化与交互要求

项目需具备 **可交互的网页展示界面**。

输出成果需具备可展示性，例如：

- 生成图像展示
- 处理前后对比效果
- 用户操作流程展示
- 应用实际操作视频演示

---

## 🎤 汇报与答辩

- 第八周进行项目验收
- 每组：
  - 8 分钟项目汇报
  - 2 分钟现场提问

需现场演示应用功能并回答相关问题。

---

## 📄 课程报告要求

提交完整的项目报告，内容包括：

- 项目背景与意义
- 技术方案与模型设计
- 实验过程与结果分析
- 成果展示
- 项目成员任务分工
- 各成员工作量占比说明

