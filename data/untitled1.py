# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:35:30 2020

@author: Administrator
"""
import os
import re 
import numpy
import time
import xlwings
import pandas
import datetime
from shutil import copyfile
from decimal import *
import multiprocessing
import matplotlib.pyplot as plt



def FileClassify (p,n):
    if not os.access(n,os.F_OK):
        os.mkdir(n)
    CopyList = list(filter(lambda x: p.findall(x) != [],FileList))
    [copyfile(os.path.join(FilePath,x),(os.path.join(n,x))) for x in CopyList]

def DataProcess (path,filelist):
    Data = pandas.DataFrame()
    col = ['T:T','U:U','V:V','Y:Y','Z:Z','AA:AA','AD:AD','AE:AE','AF:AF','AQ:AQ','AR:AR','AS:AS','AT:AT','AZ:AZ','BB:BB','BC:BC']
    if (re.compile('^寿命件3').findall(filelist[0]) !=[]) :
        col = ['T:T','U:U','V:V','Y:Y','Z:Z','AA:AA','AD:AD','AE:AE','AF:AF','AQ:AQ','AR:AR','AS:AS','AT:AT','AU:AU','AV:AV','AW:AW']
    app=xlwings.App(visible=False,add_book=False)
    app.display_alerts=False
    app.screen_updating=False
    for f in filelist:
        app.books.open(os.path.join(path,f))
        data = {}
        LastCellCol = app.books[0].sheets[0].used_range.last_cell.row
        tempdate = numpy.array([i.timetuple()[0:3] for i in app.books[0].sheets[0].range('A:A')[1:LastCellCol].value])
        temptime = numpy.array([(int((Decimal.from_float(i)*24*3600)/3600),int(int(((Decimal.from_float(i)*24*3600)%3600))/60),int((Decimal.from_float(i)*24*3600)%3600)%60) for i in app.books[0].sheets[0].range('B:B')[1:LastCellCol].value])
        tempdatetime=['-'.join(str(i) for i in j) for j in numpy.hstack((tempdate,temptime))]
        data['datetime'] = [datetime.datetime.strptime(i,'%Y-%m-%d-%H-%M-%S') for i in tempdatetime]
        data[app.books[0].sheets[0].range('L:L')[0].value] = [0.1*int(str(i).split('.')[0],16)+91.2 for i in app.books[0].sheets[0].range('L:L')[1:LastCellCol].value]
        data[app.books[0].sheets[0].range('N:N')[0].value] = [int(str(i).split('.')[0],16)+78.2 if int(str(i).split('.')[0],16)<102 else 0.8*int(str(i).split('.')[0],16)+98.4 for i in app.books[0].sheets[0].range('O:O')[1:LastCellCol].value]
        data[app.books[0].sheets[0].range('P:P')[0].value] = [0.1*int(str(i).split('.')[0],16)+108.6 for i in app.books[0].sheets[0].range('P:P')[1:LastCellCol].value]
        if (r'凝视中波2制冷温度（粗）') in data:
            data[app.books[0].sheets[0].range('O:O')[0].value] = [int(str(i).split('.')[0],16)+78.2 if int(str(i).split('.')[0],16)<102 else 0.8*int(str(i).split('.')[0],16)+98.4 for i in app.books[0].sheets[0].range('O:O')[1:LastCellCol].value]
        if (r'凝视短波2制冷温度（细）') in data:
                data[app.books[0].sheets[0].range('P:P')[0].value] = [0.1*int(str(i).split('.')[0],16)+106.6 for i in app.books[0].sheets[0].range('P:P')[1:LastCellCol].value]
        elif (r'凝视短波3制冷温度（细）') in data:
                data[app.books[0].sheets[0].range('P:P')[0].value] = [0.1*int(str(i).split('.')[0],16)+112.6 for i in app.books[0].sheets[0].range('P:P')[1:LastCellCol].value]
        for i in numpy.arange(len(col)) :
            data[app.books[0].sheets[0].range(col[i])[0].value] = [i if len(str(i).split('K')) == 1 else float(str(i).split('K')[0]) for i in app.books[0].sheets[0].range(col[i])[1:LastCellCol].value]
        app.books[0].close()
        data = pandas.DataFrame(data,index=data['datetime'])
        data = data.groupby(data.index.hour).mean().set_index(data.resample('1h').mean().index)
        Data  = Data.append(data)
    app.quit()
    return Data

def DataReform(data):
    typename = ['扫描','中波','短波']
    index = data.index
    col = [[i for i in list(data) if re.findall(j,i)] for j in typename]
    col[0] = [col[0][13],col[0][9],col[0][7],col[0][8],col[0][4],col[0][5],col[0][6],col[0][20],col[0][16],col[0][14],col[0][15],col[0][10],col[0][11],col[0][12],col[0][0],col[0][1],col[0][2],col[0][3],col[0][17],col[0][18],col[0][19]]
    data = [pandas.DataFrame([[numpy.modf(i)[1] for i in data[j]] for j in col[k]]) for k in numpy.arange(3)]
    data = [pandas.DataFrame(data[i].values.T,index=index,columns=col[i]) for i in numpy.arange(3)]
    return data
def DataWrite(col,data):
    app = xlwings.App(visible=False,add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    work = app.books.open(r'C:\\Users\\Administrator\\Desktop\\201410-新汇总.xlsx')
    for i in range(3):
        LastCellCol = app.books[0].sheets[0].used_range.last_cell.row
        work.sheets[i].range('A:A')[LastCellCol-1].value = data[col[i]]
    work.save()
    work.close()
    app.quit()

#def DataPlot(data,col):
   
#def Dataanalysis(data,col):

    
    
def main(filelist):
    Pattern = [re.compile('^寿命件1'),re.compile('^寿命件2'),re.compile('^寿命件3'),]
    NewPath = [os.path.join(FilePath,'a1'),os.path.join(FilePath,'a2'),os.path.join(FilePath,'a3')]
    [FileClassify(Pattern[i],NewPath[i]) for i in numpy.arange(3)]
    [os.remove(os.path.join(FilePath,x)) for x in filter(lambda x: re.compile(r'a').findall(x) == [], filelist)]
    filelist = [os.listdir(i) for i in NewPath]
    [i.sort(key = lambda x: int(x.split('-')[2][:-4])) for i in filelist]
    pool = multiprocessing.Pool()
    Data = pool.starmap_async(DataProcess,((NewPath[0],filelist[0]),(NewPath[1],filelist[1]),(NewPath[2],filelist[2]))).get()
    pool.close()
    pool.join()
    Data = pandas.concat([Data[0],Data[1],Data[2]],axis=1)
    Data = DataReform(Data)
    #DataWrite(Columns,Data)
    #Dataanalysis(Data)
    #DataPlot(Data,Columns)
    return Data
if __name__ =='__main__':
    start = time.time()
    FilePath = r'G:\\寿命试验数据\\YXX\\2019-12'
    FileList = os.listdir(FilePath)
    Data = main(FileList)
    stop = time.time()
    print('{}'.format(stop-start))