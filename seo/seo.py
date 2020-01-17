import requests
from lxml import etree
#import sys
Web = 'http://seo.chinaz.com/'
Content = {}
def WebResolution ():
    try:
        Response = requests.get(Web+'bing.com')
        Response.raise_for_status()
    except:
        return print('website cannot be connected or seoweb donot working')
    else:
        Response.encoding = Response.apparent_encoding
        HTML = etree.HTML(Response.text)
        return HTML
def ContentResolution(HTMLResponse):
    try:
        if (HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[2]/div[2]/div[3]/a/text()')) :
            Content['IP'] = HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[2]/div[2]/div[3]/a/text()')
        else:
            Content['IP'] = HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[3]/div[2]/div[3]/a/text()')
        Content['IP'] = str(Content['IP'])[5:-2]
        if (HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[5]/div[2]/div[1]/a/text()')) :
            Content['备案号'] = HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[5]/div[2]/div[1]/a/text()')
        else:
            Content['备案号'] = HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[4]/div[2]/div[1]/a/text()')
        if (HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[4]/div[2]/div[2]/strong/text()')):
            Content['性质'] = HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[4]/div[2]/div[2]/strong/text()')
        else:
            Content['性质'] = HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[5]/div[2]/div[2]/strong/text()')
        if (HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[4]/div[2]/div[3]/strong/text()')):
            Content['名称'] = HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[4]/div[2]/div[3]/strong/text()')
        else:
            Content['名称'] = HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[5]/div[2]/div[3]/strong/text()')
        if (HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[4]/div[2]/div[4]/strong/text()')):
            Content['审核时间'] = HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[4]/div[2]/div[4]/strong/text()')
        else:
            Content['审核时间'] = HTMLResponse.xpath('//*[@id="seoinfo"]/div/ul/li[5]/div[2]/div[4]/strong/text()')
        return Content
    except:
        return print('Content is unexcepted')
Html = WebResolution()
Content = ContentResolution(Html)
print(Content)