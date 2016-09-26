#-*-coding:utf8-*-
from gensim import corpora,models,similarities
import logging

#配置日志
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)

# document list
documents = ['Shipment of gold damaged in a fire','Delivery of silver arrived in a silver truck','Shipment of gold arrived in a truck']
# 预处理
texts = [[word for word in document.lower().split()]for document in documents]
# 生成字典
dictionary = corpora.Dictionary(texts)
print(dictionary)
print(dictionary.token2id)


