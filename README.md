# 🦜 AIGC课程代码仓库

## 📖 参考图书 
O’Reilly 出版图书 《Generative Deep Learning: Teaching Machines to Paint, Write, Compose and Play》（生成式深度学习：教会机器绘画、写作、作曲与博弈）第二版

[O’Reilly 官方链接](https://www.oreilly.com/library/view/generative-deep-learning/9781098134174/)

<img src="img/book_cover.png" width="300px">

## 🪶 课程列表

以下是本书的章节结构概览：
| 序号 | 内容 | 参考代码 |
|:----:|:----:|:----:|
| 1 | AIGC概述 | 无 |
| 2 | 深度学习与概率论基础 | [deeplearning](./AIGC-Course/notebooks/02_deeplearning) |
| 3 | VAE | 无 |
| 4 | GAN | 无 |
| 5 | Diffusion | 无 |
| 6 | 自回归模型 | 无 |
| 7 | 大语言模型 | 无 |
| 8 | 多模态大语言模型 | 无 |
| 9 | 视觉生成模型 | 无 |
| 10 | AIGC模型的安全与伦理问题 | 无 |
| 11 | 课程项目展示与评估 | 无 |

## 🚀 快速开始

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


## 📦 其他资源

本书中的部分示例改编自 Keras 官方网站提供的优秀开源实现[Keras website](https://keras.io/examples/generative/)强烈建议查阅该资源，其中会不断增加新的模型与示例。


