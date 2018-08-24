﻿''' Дан массив чисел (float или/и int). Вам нужно найти разницу между самым большим (максимум) и самым малым (минимум) элементом. Ваша функция должна уметь работать с неопределенным количеством аргументов. Если аргументов нет, то функция возвращает 0 (ноль).
Числа с плавающей точкой представлены в компьютерах как двоичная дробь. Результат проверяется с точностью до третьего знака, как ±0.001
Прочитайте о том как работать с переменым числом аргументов.
Вх. данные: Переменное число аргументов как числа (int, float).
Вых. данные: Разница между максимумом и минимумом как число (int, float). 
В этой задаче вы научитесь как работать с неопределенным числом аргументов.
Предусловия: 0 ≤ len(args) ≤ 20
all(-100 < x < 100 for x in args)
all(isinstance(x, (int, float) 100 for x in args) '''
def checkio(*nums):	
	return max(list(nums))- min(list(nums)) if len(nums)!=0 else 0


#checkio = lambda *args: max(args) - min(args) if len(args) > 1 else 0

#return max(args) - min(args) if args else 0








if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")