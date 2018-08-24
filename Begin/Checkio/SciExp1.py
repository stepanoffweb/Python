''' Даны две строки со словами, разделенными запятыми. Попробуйте найти что общего между этими строками. Слова внутри каждой строки не повторяются.
Ваша функция должна находить все слова, которые появляются в обеих строках. Результат должен быть представлен, как строка со словами разделенными запятыми и отсортированными в алфавитном порядке.
Вх. данные: Два аргумента как строки (str).
Вых. данные: Общие слова как строка (str). 
'''
def checkio(str1, str2):
	return ','.join(sorted(list(set(str1.split(',')).intersection(set(str2.split(','))))))

# Насколько это нормально - преобразовывать в set  и обратно строку в две ступени??
=========================================================================================
# def checkio(first, second):
    # first_set, second_set = set(first.split(",")), set(second.split(","))
    # common = first_set.intersection(second_set)
    # return ",".join(sorted(common))




if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
print('Good boy, go ahead!')