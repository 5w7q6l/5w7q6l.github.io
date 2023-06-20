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

## 3 数据预处理
#### 3.1 正负向语料预处理
为了方便之后的操作，需要把正向和负向评论分别规整到对应的一个txt文件中，即正向语料的集合文档（命名为2000_pos.txt）和负向语料的集合文档（命名为2000_neg.txt）。
运行完成后得到2000_pos.txt和2000_neg.txt两个文本文件，分别存放正向评论和负向评论

#### 3.2 中文文本分词
本文采用**结巴分词**分别对正向语料和负向语料进行分词处理。特别注意，在执行代码前需要把txt源文件手动转化成UTF-8格式，否则会报中文编码的错误。在进行分词前，需要对文本进行去除数字、字母和特殊符号的处理，使用python自带的**string**和**re**模块可以实现，其中string模块用于处理字符串操作，re模块用于正则表达式处理。
处理完成后，得到2000_pos_cut.txt和2000_neg_cut.txt两个txt文件，分别存放正负向语料分词后的结果。

#### 3.3 去停用词
分词完成后，即可读取停用词表中的停用词，对分词后的正负向语料进行匹配并去除停用词。去除停用词的步骤非常简单，主要有两个：

+ 1）读取停用词表；
+ 2）遍历分词后的句子，将每个词丢到此表中进行匹配，若停用词表存在则替换为空。

