''' Вх. данные: Текст для анализа, как строка.
Вых. данные: Наиболее частая буква, как строка. необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a". Убедитесь, что вы не считаeте знаки препинания, цифры и пробелы, а только буквы.
Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e". 
Предусловия:
text содержит только ASCII символы.
0 < len(text) ≤ 105 '''

def checkio(text):
	counted= set()# Для сбора уже пройденных знаков
	paras= {}
	chars= []
	if 0<len(text)<= 10**5:# Проверка длины
	# Проверка на кодировку ASCII 
			text= text.lower()
			#print(text)
			for char in text:
				if ord(char) in range(97, 123):# Проверить на диапазоны [65-90] [97-122]
					for i in text:
						if i == char and i not in counted:
							count= text.count(i)	
							counted.add(i)
							paras[str(i)]= count
							list_items= list(paras.items())
							#print(count)
							#print(counted)
							#print(paras)
							#print(list_items)
	max= list_items[0][1]
	for item in list_items:
		if list_items[list_items.index(item)][1]> max:
			max= list_items[list_items.index(item)][1]
	#print(max)
	# Ищем все пары где второй элемент равен max и проверяем их первый эл-т на min (первая в алфавите)
	for item in list_items:
		if list_items[list_items.index(item)][1]== max:
			chars.append(list_items[list_items.index(item)][0])
	#print(chars)
	min= ord(chars[0])
	for char in chars:
		if ord(char)< min:
			min = ord(chars[chars.index(char)])
	#print(min)
	return chr(min)
#print(checkio(text))
'''
import string
def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
#ПРОСТО ДИКАЯ РАЗНИЦА В СКОРОСТИ ОБРАБОТКИ ВСТРОЕННЫМИ МЕТОДАМИ!!!! Причем корректно обработано требование сравнивать только ASCII.

'''

assert checkio("Hello World!") == "l", "Hello test"
assert checkio("How do you do?") == "o", "O is most wanted"
assert checkio("One") == "e", "All letter only once."
assert checkio("Oops!") == "o", "Don't forget about lower case."
assert checkio("AAaooo!!!!") == "a", "Only letters."
assert checkio("abe") == "a", "The First."
print("Start the long test")
assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
print("The local tests are done.")
