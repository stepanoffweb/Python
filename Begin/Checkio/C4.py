'''Вам предлагается некоторый текст, который может содержать осмысленные слова. Вы должны подсчитать количество таких слов в этом тексте. Слово может стоять отдельно, а может присутствовать как часть другого слова. Регистр букв не имеет значения. Слова даны в нижнем регистре и не повторяются. Если слово встречается в тексте несколько раз, оно должно быть посчитано только один раз.
Вход: Два аргумента. Текст как строка (юникод в Python 2) и слова в виде множества (set) строк (юникод в Python 2).
Выход: Количество слов в тексте в виде целого числа.  
	Как это используется: Python удобный и мощный язык для обработки текстовых данных. В этой задаче приводится всего лишь простой пример инструментов для поиска в тексте, которые вы можете разрабатывать.
Предусловия:
0 < len(text) ≤ 256
all(3 ≤ len(w) and w.islower() and w.isalpha for w in words) 
def howmany(text, words):
	if 0 < len(text) <= 256:
		chank= text.split(' ')
		count=0
		for word in words:
			if len(chank)>= len(word):
				for char in chank:
					if char== word[0]:
						for i in word:
							if words[i]!=chank[chank.index(char)+word.index(i)]:# compare last chars consequently?
								break
							else:
								count+=1
		return count

with open('test.txt', 'r') as f:
	text1=  f.read().lower()
	words1= list({"sum", "hamlet", "infinity", "anything"})
print(howmany(text1, words1))

matches= list(words)
pattern= re.compile(r' ')# как передать в шаблон элементы итерации
count= len(pattern.findall(text))
'''
def count_words(text, words):
	import re
	text= text.lower()
	#print(text)
	matches= list(words)
	count=0

	for i in matches:
		pattern= re.compile(i)
		if pattern.search(text):
			count+=1
	return count
'''
Вар1
if word.lower() in text.lower():# оказывается if in работает как шаблон поиска абсолютного совпадения по строке!!!
            word_count +=1
Вар2
return len([w for w in words if w in text.lower()])# !!!
Вар3
return sum(w in text.lower() for w in words)
'''

print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")