# -*-coding:utf-8-*-
import os
import sys
import pickle


def loadPersistenceData(subdirName,sourceFileName):
    """
    :param subdirName:
    :param sourceFileName:
    :return:返回持久化的对象
    """
    # 获取根目录
    rootPath = os.path.dirname(os.path.abspath(os.path.dirname(sys.argv[0])))
    if subdirName != None and sourceFileName != None and subdirName != '' and sourceFileName != '':
        filePath = os.path.join(rootPath,subdirName,sourceFileName)
        return pickle.load(open(filePath,'rb'))



def getInputStream(fullPath,encode = 'utf-8'):
    """
    :param fullPath:全文件路径
    :param encode: 设置的编码集，默认的编码集为u8
    :return:
    """
    return open(fullPath,'r',encoding='utf-8')


def getLocalPath(subdirName = None,fileName = None):
    """
    通过子目录，文件名，获取一个子目录下的路径；默认获取项目跟目录路径
    :param subdirName:
    :param fileName:
    :return:
    """
    # 获取根目录
    rootPath = os.path.dirname(os.path.abspath(os.path.dirname(sys.argv[0])))
    if subdirName == None and fileName == None:
        return os.path.join(rootPath)
    elif subdirName != None and fileName == None:
        return os.path.join(rootPath,subdirName)
    elif subdirName != None and fileName != None:
        return os.path.join(rootPath,subdirName,fileName)