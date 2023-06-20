#!/usr/bin/env python
# -*- coding: utf-8  -*-
#将原始数据合并到一个txt文件

import logging
import os,os.path
import codecs,sys

#读取文件内容
def getContent(fullname):
    # ,encoding='gbk',errors='ignore'
    # 因为本实验导入的评论文件数量较多，单个文件重要性不大，只要在读取的过程中忽略这些文件既可。运行之后发现，有四个文件编码方式不同，
    f = codecs.open(fullname, 'r',encoding='utf-8',errors='ignore')
    content = f.readline()
    f.close()
    return content
    

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])#得到文件名
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    
    #输入文件目录
    inp = 'data\ChnSentiCorp_htl_ba_2000' 
    folders = ['neg','pos']

    for foldername in folders:
        logger.info("running "+ foldername +" files.")
        
        outp = '2000_' + foldername +'.txt' #输出文件
        output = codecs.open(outp, 'w')
        i = 0
        
        rootdir = inp + '\\' + foldername
        #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for parent,dirnames,filenames in os.walk(rootdir):
            for filename in filenames:
                content = getContent(rootdir + '\\' + filename)
                output.writelines(content)
                i = i+1
                
        output.close()
        logger.info("Saved "+str(i)+" files.")
                
                
    
    
    
