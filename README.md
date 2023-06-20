# 利用Python实现酒店评论的情感分析
##  我的期末作业
> **采用机器学习方法实现对酒店评论数据的情感分类，利用Python语言实现情感分类模型的构建和预测，不包含理论部分**
## 1 开发环境准备
+ 1）**Jieba**
目前使用最为广泛的中文分词组件。下载地址：https://pypi.python.org/pypi/jieba/
+ 2）**Gensim**
用于主题模型、文档索引和大型语料相似度索引的python库，主要用于自然语言处理（NLP）和信息检索（IR）。下载地址：https://pypi.python.org/pypi/gensim
本实例中的维基中文语料处理和中文词向量模型构建需要用到该模块。
+ 3）**Pandas**
用于高效处理大型数据集、执行数据分析任务的python库，是基于Numpy的工具包。下载地址：https://pypi.python.org/pypi/pandas/0.20.1
+ 4）**Numpy**
用于存储和处理大型矩阵的工具包。下载地址：https://pypi.python.org/pypi/numpy
+ 5）**Scikit-learn**
用于机器学习的python工具包，python模块引用名字为sklearn，安装前还需要Numpy和Scipy两个Python库。官网地址：http://scikit-learn.org/stable/
+ 6）**Matplotlib**
Matplotlib是一个python的图形框架，用于绘制二维图形。下载地址：https://pypi.python.org/pypi/matplotlib
+ 7）**Tensorflow**
Tensorflow是一个采用数据流图用于数值计算的开源软件库，用于人工智能领域。
官网地址：http://www.tensorfly.cn/
下载地址：https://pypi.python.org/pypi/tensorflow/1.1.0
+ 8）**PyTorch**
PyTorch提供了丰富的工具和接口，可以帮助研究人员和开发人员更快地构建和训练深度学习模型。

## 2 数据获取
#### 2.1 停用词词典
本文使用中科院计算所中文自然语言处理开放平台发布的中文停用词表，包含了1208个停用词。下载地址：http://www.hicode.cc/download/view-software-13784.html
#### 2.2 正负向语料库
文本从http://www.datatang.com/data/11936 下载“有关中文情感挖掘的酒店评论语料”作为训练集与测试集，该语料包含了4种语料子集，本文选用正负各1000的平衡语料（ChnSentiCorp_htl_ba_2000）作为数据集进行分析。







