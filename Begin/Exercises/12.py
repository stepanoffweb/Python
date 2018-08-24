'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
Concepts to practice
    Lists and properties of lists
    List comprehensions (maybe)'''
import random

list_int = [random.randint(1, 100) for r in range(10)]
def stripped(list1):
	return list((list1[0], list1[-1]))# Внимание!! обрабатываем tuple!! 

print(list_int)
print(stripped(list_int))
