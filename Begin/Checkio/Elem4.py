'''Даны 2 строки. Необходимо найти индекс второго вхождения второй строки в первую.
Разберем самый первый пример, когда необходимо найти второе вхождение "s" в слове "sims". Если бы нам надо было найти ее первое вхождение, то тут все просто: с помощью функции index или find мы можем узнать, что "s" – это самый первый символ в слове "sims", а значит индекс первого вхождения равен 0. Но нам необходимо найти вторую "s", а она 4-ая по счету. Значит индекс второго вхождения (и ответ на вопрос) равен 3.
Input: Две строки (String).
Output: Int or None
'''
def second_index(str1, str2):
	try:
		n= str1.index(str2)
	except:
		return None#str1.index(str2)
	try:
		str1= str1[n+1:]
		return str1.index(str2)+ n+ 1
	except:
		return None


#return (None if (text.count(symbol)<2) else text.find(symbol,text.find(symbol,0)+1))

def second_index(text: str, symbol: str):
    try:
        return text.index(symbol, text.index(symbol) + 1)
    except ValueError:
        return None












assert second_index("sims", "s") == 3, "First"
assert second_index("find the river", "e") == 12, "Second"
assert second_index("hi", " ") is None, "Third"
assert second_index("hi mayor", " ") is None, "Fourth"
assert second_index("hi mr Mayor", " ") == 5, "Fifth"
print('You are awesome! All tests are done! Go Check it!')

