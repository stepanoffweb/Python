'''Разбить строку по нескольким разделителям'''
import re

line = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";", ",", " ").
res = re.split(r'[;,\s]', line)
print (res)
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']