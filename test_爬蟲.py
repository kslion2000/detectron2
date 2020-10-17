from bs4 import BeautifulSoup
import requests
import codecs
import json

r1=requests.get(
	"https://108thmr.tibame.com/course/37/mission/1784")
r1.encoding="utf8"
c1 = BeautifulSoup(r1.text ,"html.parser")
print(c1)