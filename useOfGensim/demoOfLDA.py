#-*-coding:utf8-*-
from gensim import corpora,models,similarities
import logging
from util import io
from tqdm import tqdm
"""
选取2-3篇文章，实现LDA算法，调试改进算法有效性
省去数据清晰环节，直接给出清洗过的文章词语列表test_cleanArticleWordList_pw
"""
#配置日志
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)

if __name__ == '__main__':
    topicNumList = [10]
    numWord = 20

    # 加载数据对象
    cleanedArticleWordList = io.loadPersistenceData('useOfGensim','test_cleanedArticleWordList_pw.pkl')
    # 生成dictionary字典
    dictionary = corpora.Dictionary(cleanedArticleWordList)
    print('已生成dictionary字典...')
    # 词频向量（词语列表---->id标识词语的词频向量）
    corpus = [dictionary.doc2bow(text) for text in cleanedArticleWordList]
    print('已生成词频向量...')
    ## 在这里添加TF-IDF模型
    # -----

    for topicNum in tqdm(topicNumList):
        # 根据话题数生成LDA模型
        print('开始训练LDA模型，主题数为：'+str(topicNum))
        LDAModel = models.LdaModel(corpus,num_topics=topicNum,id2word=dictionary,passes=15)
        # LDAModel = gensim.models.ldamodel.LdaModel(corpus,num_topics=topicNum,id2word=dictionary,passes=15)

        # 输出LDA主题
        print('输出主题数为：'+ str(topicNum) + ',显示主题词语数为：' + str(numWord) + '的主题')
        for keyWords in LDAModel.print_topics(num_topics=topicNum,num_words=numWord):
            print(keyWords)

        # 根据LDA模型，计算每篇文档相对于主题的权重
        print('输出文档对应主题的权重')
        # for i in range(len(corpus)):
        #     topicWeightList = LDAModel[corpus[i]]
        #     print('文档：' + str(i+1) + '相应的主题权重为：' , str(topicWeightList))

        # for i in range(len(corpus)):
        #     print('LDAModel[corpus[i]]的类型为：',type(LDAModel[corpus[i]]))
        #     for item in LDAModel[corpus[i]]:
        #         print(item)

        topicWeightMatrix = LDAModel[corpus]    # <gensim.interfaces.TransformedCorpus object at 0x000001ADDDF2CDD8>
        print('topicWeightMatrix的类型为：',type(topicWeightMatrix))
        for topicWeightList in topicWeightMatrix:
            print('文档x相应的主题权重为：' + str(topicWeightList))



