import json
from urllib.request import urlopen

#url= 'http://www.bloomberg.com/quote/SPX:IND'
with urlopen('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json') as response:
	print((response))#<http.client.HTTPResponse object at 0x0000000002F480F0>
	source= response.read()
data= json.loads(source)
# Здесь парсинг и выборка

with open('Yahoo.json', 'w') as f:
	json.dump(data, f, indent= 2)

''' Задача: слить с сайта в json формате данные, выбрать необходимые поля(ключи) и сохранить в файл.'''