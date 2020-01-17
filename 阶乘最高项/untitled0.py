# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 23:59:03 2020

@author: 78616
"""

import math
import numpy
def FirstNumber (n) :
    global Accumulator
    firstnumber = Accumulator*n
    while firstnumber >= 10 :
        firstnumber = firstnumber/10
    firstnumber = math.modf(firstnumber)[1]
    Accumulator = firstnumber
    return Accumulator
def main() :
    N = int(input())
    firstnumberlist = numpy.array([int(FirstNumber(i)) for i in range(2,N+1)])
    freq = numpy.bincount(firstnumberlist)
    return freq
if __name__ =='__main__' :
    Accumulator = 1
    FirstNumberFreq = main()