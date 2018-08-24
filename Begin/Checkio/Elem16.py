''' Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).
Входные данные: Положительное целое число.
Выходные данные: Произведение цифр как целочисленное (int). '''
# def checkio(num):
	# multi= 1
	# for digit in str(num):
		# if digit!='0':
			# multi*= int(digit)
		# else:
			# continue
	# return multi
#-------------------------------------------------------------------------------------------------
    # res = 1
    # for d in str(number):
        # if int(d):
            # res *= i
    # return res
#=============================================================================
# from functools import reduce
# from operator import mul
# def checkio(number):
    # return reduce(mul, (int(x) for x in str(number) if x != '0'))
#===========================================================================
#the same one line code Instead of using reduce function, I write a recursion function.
checkio = lambda n: (n%10 or 1)*checkio(n//10) if n else 1
#------------------------------------------------------------------------------------
from functools import reduce
def checkio(num):
	return reduce(lambda x, y : x*y, [int(digit) in str(num) if digit!= '0'])
======================================================================
checkio = lambda n: eval("*".join(i for i in str(n) if i != '0'))




if __name__ == '__main__':
	assert checkio(123405) == 120
	assert checkio(999) == 729
	assert checkio(1000) == 1
	assert checkio(1111) == 1
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
