'''написать функцию, которая представит человека по переданным параметрам.
Входные данные: Два аргумента строка(str) и положительное число(int)
Output: Строка(str).
Example:
say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"'''


def greating(name, age):
	return "Hi. My name is {} and I'm {} years old".format(name, age)

print(greating('Alex', 32))