# -*-coding:utf-8-*-
import jieba
import jieba.analyse
import os
import sys
from util import io

# jieba分词模式的使用
def participle(text,userdict1Path):
    print(text)
    # jieba全模式
    print('full:','/'.join(jieba.cut(text,cut_all=True)))
    # jieba精准模式
    print('exact:','/'.join(jieba.cut(text,cut_all=False)))
    # jieba搜索引擎模式
    print('search:','/'.join(jieba.cut_for_search(text)))
    """
    1 精确模式下“社会”不能提取 （细粒度分词会遇到这个问题）
    2 专有名词“中国梦”三种模式都提取不出来
    """
    # 加入自定义字典后的效果
    jieba.load_userdict(userdict1Path)
    # jieba全模式
    print('full:','/'.join(jieba.cut(text, cut_all=True)))
    # jieba精准模式
    print('exact:','/'.join(jieba.cut(text, cut_all=False)))
    # jieba搜索引擎模式
    print('search:', '/'.join(jieba.cut_for_search(text)))
    """
    1 粗粒度的分词，使用精确模式 + 自定义词典方式
    2 细粒度的分词，因为词语长度较小jieba自身词典长度时，就会只分出较长的词，所以使用全模式能够分出更细粒度的词
    """

# jieba提取关键词的使用
def extractKeyword(text,userdict1Path):
    """
    jieba提取关键词只需要1 引入jieba.analyse包；2 调用相关的函数，指定关键词的个数
    :param text:
    :param userdict1Path:
    :return:
    """
    num = 4
    # 这里关键词的提取使用到了TF-IDF算法
    tags = jieba.analyse.extract_tags(text,topK=num)
    print(type(tags))
    print(','.join(tags))


if __name__ == '__main__':
    # 获取完整路径
    textSet1Path = io.getLocalPath('useOfjieba','TextSet1.txt')
    textSet2Path = io.getLocalPath('useOfjieba','TextSet2.txt')
    userdict1Path = io.getLocalPath('useOfjieba','userdict1.txt')
    # 获取文件输入流
    fr1 = io.getInputStream(textSet1Path)
    fr2 = io.getInputStream(textSet2Path)
    # 获取文本内容
    textSet1 = fr1.readline()
    textSet2 = fr2.readline()

    # jieba三种分词模式的使用
    # participle(textSet1,userdict1Path)

    # jiaba提取关键词的使用
    extractKeyword(textSet1,userdict1Path)




