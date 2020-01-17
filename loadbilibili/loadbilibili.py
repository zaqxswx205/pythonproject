# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 10:23:44 2019

@author: 78616
"""



import requests
from lxml import etree
import urllib
import cv2


BasicWeb = 'https://cn.bing.com/'
RequestsHeaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
Localpath = "C:/Users/78616/Documents/pythonproject/loadbilibili/IMG.jpg"


def WebResolution (ObjectWeb,Headers):
    try:
        Response = requests.get(ObjectWeb,headers=Headers)
        Response.raise_for_status()
    except:
        return print('website cannot be connected ')
    else:
        Response.encoding = Response.apparent_encoding
        HTML = etree.HTML(Response.text)
        return HTML



if __name__ == '__main__':
    HTML = WebResolution(BasicWeb,RequestsHeaders)
    ImgWeb = ''.join(BasicWeb)+''.join(HTML.xpath('//@data-ultra-definition-src'))
    urllib.request.urlretrieve(ImgWeb,Localpath)
    cv2.imshow(ImgWeb,cv2.imread(Localpath))
    cv2.waitKey(0)
    cv2.destroyAllWindows()