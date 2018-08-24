'''написать функцию, которая принимает положительное целое число и возвращает:
"Fizz Buzz", если число делится на 3 и 5;
"Fizz", если число делится на 3;
"Buzz", если число делится на 5;
Число, как строку для остальных случаев.
Входные данные: Число, как целочисленное (int).
Выходные данные: Ответ, как строка (str). 
Предусловия: 0 < number ≤ 1000 '''
def checkio(num):
	if num%5==0:
		if num%3==0:
			return 'Fizz Buzz'
		return 'Buzz'
	elif num%3==0:
		return 'Fizz'
	else:
		return str(num)

#return "Fizz Buzz" if number % 15 == 0 else "Fizz" if number % 3 == 0 else "Buzz" if number % 5 == 0 else str(number)

#return max(str(number),'Fizz '*(number % 3 == 0)+'Buzz'*(number % 5 == 0)).strip()









if __name__ == '__main__':
	assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
	assert checkio(6) == "Fizz", "6 is divisible by 3"
	assert checkio(5) == "Buzz", "5 is divisible by 5"
	assert checkio(7) == "7", "7 is not divisible by 3 or 5"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
