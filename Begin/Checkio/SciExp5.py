''' You have a device that uses a Seven-segment display to display 2 digit numbers. However, some of the segments aren't working and can't be displayed.
You will be given information on the lit and broken segments. You won't know whether the broken segment is lit or not. You have to count and return the total number that the device may be displaying.
The input is a set of lit segments (the first argument) and broken segments (the second argument).
    Uppercase letters represent the segments of the first out two digit number.
    Lowercase letters represent the segments of the second out two digit number.
    topmost: 'A(a)', top right: 'B(b)', bottom right: 'C(c)', bottommost: 'D(d)', bottom left: 'E(e)', top left: 'F(f)', middle: 'G(g)'
'''
def seven_segment(in_set1, in_set2):
	dict1= {0:{'A', 'B', 'C', 'D', 'E', 'F'}, 1:{'B', 'C'}, 2: {'A', 'B', 'G', 'E', 'D'}, 3:{'A', 'B','C', 'D', 'G'}, 4:{'F', 'G', 'B', 'C'}, 5:{'A', 'F', 'G', 'C', 'D'}, 6:{'A', 'F', 'G', 'C', 'D', 'E'}, 7:{'A', 'B', 'C'}, 8:{'A', 'F', 'G', 'C', 'D', 'E', 'B'}, 9:{'A', 'F', 'G', 'C', 'D', 'B'}}
	dict2= {0:{'a', 'b', 'c', 'd', 'e', 'f'}, 1:{'b', 'c'}, 2: {'a', 'b', 'g', 'e', 'd'}, 3:{'a', 'b', 'c', 'd', 'g'}, 4:{'f', 'g', 'b', 'c'}, 5:{'a', 'f', 'g', 'c', 'd'}, 6:{'a', 'f', 'g', 'c', 'd', 'e'}, 7:{'a', 'b', 'c'}, 8:{'a', 'f', 'g', 'c', 'd', 'e', 'b'}, 9:{'a', 'f', 'g', 'c', 'd', 'b'}}
	set1= {x for x in in_set1 if x.isupper()}
	set1_2= {x for x in in_set2 if x.isupper()}
	set2= {x for x in in_set1 if x.lower()}
	set2_2= {x for x in in_set2 if x.lower()}
	dig1= 0
	dig2= 0
	for val in dict1.values():# берем комбинации сегментов поциферно
		if val== set1:# сравниваем их с набором горящих сегментов
			dig1+=1
		maybe1= set()# собирать комбинации из всех битых сегментов последовательно
		for c in set1_2:
			if set1.add(c)== val:# если добавить к горящим этот сегмент
				dig1+=1
			maybe1= maybe1.add(c)
			if set1.update(maybe1)== val:# если добавить комбинацию с этим сегментом
				dig1+=1
			set1_2.remove(c)# "отработанный" сегмент не должен участвовать в последующих комбинациях
		
		
		
	for val in dict2.values():
		if val== set2:
			dig2+=1
		maybe2= set()
		for c in set2_2:
			if set2.add(c)== val:
				dig2+=1
			maybe2= maybe2.add(c)
			if set2.update(maybe2)== val:
				dig2+=1
			set2_2.remove(c)
	# print(dig1, dig2)
	return dig1*dig2









if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
