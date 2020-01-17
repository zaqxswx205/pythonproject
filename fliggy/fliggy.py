# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:38:57 2019

@author: 78616
"""
import requests
from bs4 import BeautifulSoup
import re
def GetURLResponse(Web):
    try:
        Response = requests.get(Web)
        Response.raise_for_status()
        Response.encoding = Response.apparent_encoding
        r = BeautifulSoup(Response.text,'html.parser')
        return r
    except:
        print(Response.raise_for_status())
def ResignTravelProduct(Html):
    Content = [i.string for i in Html.find_all('div',class_='item-title')]
    Price = [re.findall('\d+',repr(i)) for i in Html.find_all('div',class_='pi-price')]
    if len(Content) == len(Price):
        Travel = {i:j for i,j in zip(Content,Price)}
        return Travel
    else:
        print('爬取出现问题，请观察Content和Price')
if "_name_ == '_main_'":
    Web = "https://www.fliggy.com"
    Html = GetURLResponse(Web)
    Travel = ResignTravelProduct(Html)