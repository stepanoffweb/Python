''' Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива. Не забудьте, что первый элемент массива имеет индекс 0.
Для пустого массива результат всегда 0 (ноль).
Входные данные: Список (list) целых чисел (int).
Выходные данные: Число как целочисленное (int)
Предусловия: 0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)'''
def checkio(list_int):
	return sum([x for x in list_int[::2]])*list_int[-1] if list_int else 0#sum(iterable, start=0, /). Return the sum of a 'start' value (default: 0) plus an iterable of numbers. When the iterable is empty, return the start value.


#return sum(array[::2]) * array[-1] if array else 0








if __name__ == '__main__':
	assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
	assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
	assert checkio([6]) == 36, "(6)*6=36"
	assert checkio([]) == 0, "An empty array = 0"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")