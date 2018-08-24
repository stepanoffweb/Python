''' Дан массив с положительными числами и число N. Вы должны найти N-ую степень элемента в массиве с индексом N. Если N за границами массива, тогда вернуть -1. Не забывайте, что первый элемент имеет индекс 0.
Входные значения: Два агумента. Массив как список целых и число как целое.
Выходные значения: Целое число. 
'''
def index_power(list_int, num):
	return list_int[num]**num if len(list_int)>=num else -1

    # try: return array[n] ** n
    # except IndexError: return -1










if __name__ == '__main__':
	assert index_power([1, 2, 3, 4], 2) == 9, "Square"
	assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
	assert index_power([0, 1], 0) == 1, "Zero power"
	assert index_power([1, 2], 3) == -1, "IndexError"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
