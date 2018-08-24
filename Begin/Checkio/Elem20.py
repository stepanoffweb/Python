''' Ваше задание здесь создать функцию, которая получает массив(tuple) и возвращает набор с 3 элементами - [0,2, -2].
Входные данные: Набор длинной не менее 3 элементов.
Выходные данные: Набор элементов. '''
def easy_unpack(some_tuple):
	return tuple([some_tuple[0], some_tuple[2], some_tuple[-2]])
---------------------------------------------------------------------
#from operator import itemgetter
#easy_unpack = itemgetter(0, 2, ~1)
------------------------------------------------





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')