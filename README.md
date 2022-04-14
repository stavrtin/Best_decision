Просто респонсы 
--------------------------------------------
# Импортируем библиотеки
from pprint import  pprint
from lxml import html
import requests

url = 'https://sport-dealer.ru/search/?query=Amino+X%2C+435+g'

response = requests.get(url)
dom = html.fromstring(response.text)
dom.xpath('//h1')[0].text
------------------------------------------------


