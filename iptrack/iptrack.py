requests
import re
from bs4 import BeautifulSoup
ip=input("Object IP:")
url="https://restapi.amap.com/v3/ip?"
key="key=ef1e6f74e7cd20615949b27dfdf8ffc5"
obip="ip="+ip
output="output=xml"
web=url+obip+'&'+output+"&"+key
answer=BeautifulSoup(requests.get(web).text,'lxml')
cat={1:'status',2:'info',3}
