# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:36:05 2019

@author: 78616
"""
import numpy as np
import LinerFun
ChainVariable=[0x67452301,0xefcdab89,0x98badcfe,0x10325476]
Context='abcdefghigklmnopqrstuvwxyz'.encode('utf-8')
ContextBin=''.join([bin(Context[i]).replace('0b','') for i in range(len(Context))])
if len(ContextBin)%512!=448:
   Suffix='1'+'0'*(448-(len(ContextBin)%512)-1)
ContextBinLength=bin(len(ContextBin)).replace('0b','')
ContextBin+=Suffix+'0'*(64-len(ContextBinLength))+ContextBinLength
ContextBlockIndex=np.arange(int(len(ContextBin)/512)*32*16).reshape(int(len(ContextBin)/512),32,16)
  