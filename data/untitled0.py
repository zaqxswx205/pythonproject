# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:44:21 2019

@author: 78616
"""

import os

import re

from shutil import copyfile 

import numpy

import time

'''from multiprocessing import Process'''

def FileClassify (p,n):
    if not os.access(n,os.F_OK):
        os.mkdir(n)
    CopyList = list(filter(lambda x: p.findall(x) != [],FileList))
    [copyfile(os.path.join(FilePath,x),(os.path.join(n,x))) for x in CopyList]

'''def DataProcess ():'''
    
    
if __name__ =='__main__':
    start = time.time()
    FilePath = 'D:\\2019-7'
    NewPath = [os.path.join(FilePath,'a1'),os.path.join(FilePath,'a2'),os.path.join(FilePath,'a3')]
    Pattern = [re.compile('^寿命件1'),re.compile('^寿命件2'),re.compile('^寿命件3'),]
    FileList = os.listdir(FilePath) 
    [FileClassify(Pattern[i],NewPath[i]) for i in numpy.arange(3)]
    [os.remove(os.path.join(FilePath,x)) for x in filter(lambda x: re.compile(r'a').findall(x) == [], FileList)]
    '''[FileList[i].sort(key = lambda x: int(x.split('-')[2][0])) for i in numpy.arange(3)]'''
    '''DataProcess()'''
    stop = time.time()
    print('{}'.format(stop-start))