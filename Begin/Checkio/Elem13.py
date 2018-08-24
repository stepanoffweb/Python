''' Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
Входные данные: Строка со словами (str).
Выходные данные: Ответ как логическое выражение (bool), True или False. 
Предусловия: Исходная строка содержит только слова и/или числа. Смешанных слов нет (перемешанные цифры и буквы).
0 < len(words) < 100 
'''
def checkio(text):
	text= text.split()
	count=0
	for word in text:
		if word.isalpha():
			count+=1
			if count== 3:
				return True
		else:
			count=0
	return False

    # count = 0
    # for word in words.split():
        # count = (count + 1)*word.isalpha()
        # if count == 3: return True
    # else: return False# избыточное !!!! и НЕПРОСТОЕ - FOR/ ELSE???!!!







if __name__ == '__main__':
	assert checkio("Hello World hello") == True, "Hello"
	assert checkio("He is 123 man") == False, "123 man"
	assert checkio("1 2 3 4") == False, "Digits"
	assert checkio("bla bla bla bla") == True, "Bla Bla"
	assert checkio("Hi") == False, "Hi"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")