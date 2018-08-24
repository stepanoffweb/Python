'''Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list that are smaller than that number given by the user.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 345]
res = []

def less_then(list_int, num):
	for i in list_int:
		if i < num:
			res.append(i)
	return res

print(less_then(a, num = int(input("Give me a number "))))


