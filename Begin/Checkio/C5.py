'''необходимо найти длину самой длинной подстроки, которая состоит из одинаковых букв. Например, строка "aaabbcaaaa" состоит из четырех подстрок с одинаковыми буквами "aaa", "bb","c" и "aaaa". Последняя подстрока является самой длинной, что и делает ее ответом.
Входные данные: Строка.
Выходные данные: Целое число. 
НЕ ПЕРЕБОРОМ!!!'''
def long_repeat(str_text):
	if len(str_text)!= 0:
		char = str_text[0]
		count=1
		count_max= 1
		for i in str_text[1:]:
			if i== char:
				count+=1
			else:
				char= i
				if count>= count_max:
					count_max= count
					count= 1
					if count> count_max:
						count_max= count	
		return count_max
	else:
		return 0
	

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
'''
Вар1
from itertools import groupby
def long_repeat(line):
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)
Вар2
long_repeat=lambda l:len(l)and max(map(len,dict(__import__('re').findall(r'((.)\2*)',l))))
Вар3
def long_repeat(line):
    return len(line) and 1+long_repeat(''.join(u for u,v in zip(line,line[1:]) if u==v))

'''
