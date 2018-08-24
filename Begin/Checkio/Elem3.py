''' Дана строка и нужно найти ее первое слово.
При решении задачи обратите внимание на следующие моменты:
    В строке могут встречатся точки и запятые
    Строка может начинаться с буквы или, к примеру, с пробела или точки
    В слове может быть апостроф и он является частью слова
    Весь текст может быть представлен только одним словом и все
Входные параметры: Строка.
Выходные параметры: Строка.
Пример:
first_word("Hello world") == "Hello"
first_word("greetings, friends") == "greetings"
How it is used: first word is a command in command line
Precondition: text can contain a-z A-Z , . '
'''


def first_word(string1):
    string1= string1.replace('.', ' ')
    string1= string1.replace(',', ' ')
    string1 = string1.strip()
    string2 = string1.split(' ')[0]
    #print(string2)
    return string2

# import re
# def first_word(text: str) -> str:
    # text = text.strip(',. ?!')
    # text_splited = re.split('[\s,.]', text)
    # return text_splited[0]

#return text.replace('.',' ').replace(',',' ').lstrip(' ').split(' ')[0]

# import re
# def first_word(text: str) -> str:
    # return re.search("([\w']+)", text).group(1)



assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word("Hello.World") == "Hello"
print("Coding complete? Click 'Check' to earn cool rewards!")
