''' Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми. В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова. Все строки даны в нижнем регистре.
Входные данные: Последовательность строк, как кортеж строк (юникод).
Выходные данные: Текст, как строка. 
'''
import re
def left_join(tuple_strings):
	return ','.join([(re.sub(r'right', r'left', string)) for string in tuple_strings])# вырвал гланды через жопу автогеном

#    return ','.join(phrases).replace('right', 'left')

#left_join=lambda p:",".join(p).replace("right","left")











if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
	assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
	assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
	assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
	assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")