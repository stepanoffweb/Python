'''Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
Extras:    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
           Go back and do Exercise 5 using sets, and write the solution for that in a different function.
Concepts for this week:    Sets
	In mathematics, a set is a collection of elements where no element is repeated. This becomes useful because if you know your data is stored in a set, you are guaranteed to have unique elements.'''
import random	

list_char= [chr(random.randint(90, 122)) for i in range(100)]
def unic(list1):
	return list(set(list1))
	
print(list_char)
print(unic(list_char))