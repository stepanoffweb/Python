'''определить, все ли элементы массива равны.
Входные: List.
Выходные: Bool. 
 Precondition: all elements of the input list are hashable '''


def all_the_same(list1):
	if len(list1)>=0:
		return len(set(list1))<=1
	
assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same(['a', 'a', 'a']) == True
assert all_the_same([]) == True
assert all_the_same([1]) == True
print("Coding complete? Click 'Check' to earn cool rewards!")

list1= input('Give a list of hasable')

if __name__ == "__main__":
	all_the_same(list1)

#return len(set(elements)) == 1 if elements else True
#return len(e) < 2 or eval('=='.join(repr(i) for i in e)) #креативненько
#e=lambda e:len(set(e))<2




