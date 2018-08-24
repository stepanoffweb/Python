''' Количество слов в тексте в виде целого числа.
Пример: text= ("how", "are", "you", "hello") --> 3'''

import re

text= "How aresjfhdsHowkfhskd you?"
pattern= re.compile(r'How')
matches= pattern.finditer(text)
for match in matches: print(match)
# <_sre.SRE_Match object; span=(0, 3), match='How'>
# <_sre.SRE_Match object; span=(13, 16), match='How'> 
listentries= re.findall(r'How', text)
print(listentries)# ['How', 'How']

