# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 19:03:30 2019

@author: 78616
"""

import requests
from lxml import etree
BasicWeb = 'https://cn.bing.com/'
RequestsHeaders={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
Response = requests.get(BasicWeb,headers=RequestsHeaders)
Response.encoding = Response.apparent_encoding
Content = etree.HTML(Response.text)
rawXpath = Content.xpath('//@data-ultra-definition-src')
