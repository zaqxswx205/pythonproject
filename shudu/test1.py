# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 22:54:24 2019

@author: 78616
"""

import numpy

def process (unsolve,question) :
    possibilityArr = {}
    sample = numpy.arange(1,10)
    for i in zip(unsolve[:,0],unsolve[:,1]):
        row = question[i[0],numpy.nonzero(question[i[0]])]
        col = question[numpy.nonzero(question[:,i[1]]),i[1]]
        tup = question[(i[0]-i[0]%3):(i[0]-i[0]%3+3),(i[1]-i[1]%3):(i[1]-i[1]%3+3)]
        prow = sample[numpy.in1d(sample,row,invert=True)]
        pcol = sample[numpy.in1d(sample,col,invert=True)]
        ptup = sample[numpy.in1d(sample,tup,invert=True)]
        ptemp = numpy.argwhere(numpy.bincount(numpy.hstack((prow,pcol,ptup)))==3)
        if len(ptemp) == 1:
            Question[i] = ptemp
        else:
            possibilityArr[i] = ptemp   
if __name__ == '__main__':
    Question = numpy.array([[0,4,9,0,7,0,0,5,0],[0,8,0,4,0,0,9,0,3],[2,3,0,0,0,9,7,8,4],
                [0,6,7,0,0,4,0,0,0],[0,0,0,0,1,0,0,0,0],[1,5,2,0,3,0,4,0,8],
                [5,0,0,2,4,0,8,0,0],[8,2,3,0,9,7,0,0,0],[9,0,4,8,6,0,0,3,0]])
    sign = 0
    while True:
        Unsolve = numpy.argwhere(Question==0)
        if len(Unsolve)!=0:
            process(Unsolve,Question)
            if sign == len(Unsolve):
                print('Question can not be solved')
                break
            sign = len(Unsolve)
        elif len(Unsolve)==0:
            print('Qestion completed')
            break