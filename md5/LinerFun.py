# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:26:35 2019

@author: 78616
"""
def F(x,y,z):
    return (x&y)|((~x)&z)
def G(x,y,z):
    return (x&z)|(y&(~z))
def H(x,y,z):
    return x^y^z
def I(x,y,z):
    return y^(x|(~z))
def FF(a,b,c,d,Mj,s,ti):
    temp=(a+F(b,c,d)+Mj+ti)<<s
    return b+(temp<s)
def GG(a,b,c,d,Mj,s,ti):
    temp=(a+G(b,c,d)+Mj+ti)<<s
    return b+(temp<s)
def HH(a,b,c,d,Mj,s,ti):
    temp=(a+H(b,c,d)+Mj+ti)<<s
    return b+(temp<s)
def II(a,b,c,d,Mj,s,ti):
    temp=(a+I(b,c,d)+Mj+ti)<<s
    return b+(temp<s)