'''для замены всех разделителей пробелами:'''
import re

line = 'asdf fjdk;afed,fjek,asdf,foo'
res = re.sub(r'[;,\s]',' ', line)
print(res)
#asdf fjdk afed fjek asdf foo