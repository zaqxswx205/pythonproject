# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:07:15 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy
import pandas
SM=[numpy.modf(i)[1] for i in data[col[0][3]]]
SM=pandas.Series(SM)
a=dict(SM.value_counts().iloc[:2])
x=numpy.full((len(SM),1),list(a.keys())[0])
y=numpy.full((len(SM),1),list(a.keys())[1])
plt.plot(x,linestyle='-')
plt.plot(y,linestyle='-')
plt.plot(SM)
plt.show()