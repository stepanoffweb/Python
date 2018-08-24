'''Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
Concepts for this week:    More string things
Python has a lot of interesting things you can do with strings. I will show a few here, but you can see many more methods that may or may not be useful at the official Python documentation about the string format.https://docs.python.org/3.3/library/stdtypes.html?highlight=strings#string-methods
Remember that strings are lists.https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html'''

text= 'Python has a lot of interesting things you can do with strings. I will show a few here, but you can see many more methods that may or may not be useful at the official Python documentation about the string '
def backward(long_string):
	list1= long_string.split(' ')
	list2=[]
	print(list1)
	list1.reverse()
	print(list1)
	for i in list1:
		list2.append(i[::-1])
	print(list2)
	return ' '.join(list1)
print(backward(text))


#my_str= ', '.join(my_list)