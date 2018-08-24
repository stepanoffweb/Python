import requests
import csv
import json

source = requests.get('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json').text
# source = source.read()AttributeError: 'Response' object has no attribute 'read'
print(source)
print(type(source))  # <class 'str'>

outputFile = open("Yahoo.csv", 'a', encoding='utf-8')  # load csv file
# data = json.loads(source)TypeError: the JSON object must be str, bytes or bytearray, not 'Response'
output = csv.writer(outputFile)  # create a csv.writer
print(output.writerow(source[0].keys()))
for row in source:
    output = csv.writer(outputFile)  # create a csv.write
    output.writerow(source[0].keys())
for row in source:
    output.writerow(row.values())  # values row
