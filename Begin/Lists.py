
# spisok = [] - simpler and more common way to create a list
# spisok = list() - unusual way via constructor
# List Comprehension!!! WATCH SOCRATICA!!

list1 = ['History', 'Anatomy']
#list2 = list1 + 'Art'
#print(list2)

list2 = [' of England', 'human']
for a, b in zip(list2, list1):
	print(a, b)
	
my_list= ['One', 'Two', 'Tree']
for index, item in enumerate(my_list, start=1):
	print(index, item)