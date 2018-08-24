'''определить популярность определенных слов в тексте.
На вход вашей функции передается 2 аргумента. Текст и массив слов, популярность которых необходимо определить.
При решении этой задачи обратите внимание на следующие моменты
    Слова необходимо искать во всеx регистрах. Т.е. если необходимо найти слово "one", значит для него будут подходить слова "one", "One", oNe", "ONE" и.т.д. Искомые слова всегда указаны в нижнем регистре
    Если слово не найдено ни разу, то его необходимо вернуть в словаре со значением 0 (ноль)
Входные параметры: Текст и массив искомых слов.
Выходные параметры: Словарь, в котором ключами являются искомые слова и значениями то, сколько раз они встречаются в исходном тексте.
Предусловия: Исходный текст будет состоять из букв английского алфавита в верхнем и нижнем регистре, а также пробелов.  '''
def popular_words(text, words):
	popularity= dict((word, 0) for word in words)
	for word in text.lower().replace('\n', ' ').split(' '):
		if word in words:
			popularity[word] +=1
	return popularity

# def popular_words(text, words):
    # lower_count = text.lower().split().count
    # return {word: lower_count(word) for word in words}
'''only (1) counting is repeated multiple times (inside the comprehension loop), but (2) splitting and (3) bringing to lower case have been applied only once (before the comprehension loop).

in the follow case not only (1) counting, but also (2) splitting and (3) bringing to lower case the whole input text each time we iterate over the list of words…:
lower_count = lambda x: text.lower().split().count(x)
return {word: lower_count(word) for word in words
'''





if __name__ == '__main__':
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
