# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:07:27 2019

@author: 78616
"""
import re
pattern = re.compile(r'39212830112')
Figure = 100
Sign = 1
while (Sign):
   b = 10**(Figure+10)
   x1 = b*4//5
   x2 = b// -239
   Sum = x1+x2
   for i in range(3,2*Figure,2):
      x1 //= -25
      x2 //= -57121
      Tempx = (x1+x2) // i
      Sum += Tempx
   pai = Sum*4
   pai //= 10**10
   paistring=str(pai)
   result=paistring[-100:]
   print(result)
   print(Figure)
   Figure+=100
   match=pattern.search(result)
   if match:
       Sign=0