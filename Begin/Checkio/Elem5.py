'''Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий:
    Начальный и конечный маркеры всегда разные
    Если нет ни конечно ни начального маркеров, то просто вернуть всю строку
    Если нет начального маркера, то началом считать начало строки
    Если нет конечного маркера, то концом считать конец строки
    Если конечный маркер стоит перед начального, то вернуть пустую строку
Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
Output: Строка.
Как это использутеся: может использоваться для парсинга небольшой верстки
Предусловия: не может быть более одного маркера одного типа'''


def between_markers(in_str, m1, m2):
    if m1 in in_str and m2 in in_str:
        if m2 in in_str.split(m1)[0]:
            return ''
        else:
            return in_str.split(m1)[1].split(m2)[0]
    elif m1 not in in_str:
        return in_str.split(m2)[0]
    elif m2 not in in_str:
        return in_str.split(m1)[1]
    else:
        return in_str


# start = text.find(begin) + len(begin) if begin in text else None
# stop = text.find(end) if end in text else None
# return text[start:stop]



# def between_markers(text: str, begin: str, end: str) -> str:
    # index_begin = text.find(begin)
    # index_begin = index_begin+ len(begin) if index_begin!= -1 else 0 
    # index_end = text.find(end)
    # index_end = index_end if index_end != -1 else len(text)
    # return text[index_begin : index_end]

    # begin = begin if text.find(begin)!=-1 else ''
    # end = end if text.rfind(end)!=-1 else ''
    # return text[text.find(begin)+len(begin): text.rfind(end)]




assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
assert between_markers("<head><title>My new site</title></head>",
                       "<title>", "</title>") == "My new site", "HTML"
assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
print('Wow, you are doing pretty good. Time to check it!')
