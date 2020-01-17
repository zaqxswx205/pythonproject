import requests
from lxml import etree
BasicWeb = 'https://cn.bing.com/search?q='
class MakeRequests :
    RequestsHeaders={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    def __init__(self,Requests):
        self.Requests = Requests
        try : 
            self.Response = requests.get(self.Requests,headers=self.RequestsHeaders,timeout=5)
            self.Response.raise_for_status ()
        except requests.exceptions.ConnectionError as err:
            print ('Network problem')
        except requests.exceptions.HTTPError as err :
            print ('HTTP request returned an unsucessful status code')
        except requests.exceptions.Timeout as err :
            print ('A request times out')
    def ResolutionContent (self):
        self.Response.encoding =  self.Response.apparent_encoding
        self.Content = etree.HTML(self.Response.text)
        self.rawXpath = self.Content.xpath('//ol[@id="b_results"]/li[@class="b_algo"]//h2')
        return [ self.rawXpath[i].xpath('string(.)') for i in range(0,len(self.rawXpath)-1) ]
BasicKeyword = input('Please input keyword:')
PrefixKeyword = [ BasicWeb+BasicKeyword+'&qs=n&sp=-1'+'&pq='+BasicKeyword+'&first='+str(i) for i in range(0,int(input('Please input quantity of page:'))*10,10) ]
Results = [ MakeRequests(PrefixKeyword[i]).ResolutionContent() for i in range(0,len(PrefixKeyword)) ]
[ [ print("{}".format(Results[j][i])) for i in range(0,len(Results[0])) ] for j in range(0,len(Results)) ]