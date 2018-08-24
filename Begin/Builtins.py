#zip (list1, list2)
list1= ['Bob', 'Rob', 'Dolboeb']
list2= [23, 46, 66]

for x, y in zip (list1, list2):
	print(x, y)# автоматически переводит y в str 
#print(x +'=' +y )НЕ РАБОТАЕТ

#enumerated list
list_items= ['Bob', 'Rob', 'Dolboeb']
for i, item in enumerate(list_items, start= 1):
	print(i, item)

	
#работа с кортежами...есть вопросы
x, y = y, x#swap без дополнительного (временного) хранилища

#поиск элемента контейнера? (list/ dict/ set?/ str?)
key= 'Ivan'
my_dict= {'Bob': 13, 'Rob': 54, 'Dolboeb': 398}
'''
if key in my_dict:
	value= my_dict[key]
else:
	value= 'Noexist'

'''
value= my_dict.get('key', 'Noexist') #- те же яйца в профиль, с проверкой
print(value)

#вывод в терминал текстового файла
f= open('PATH')
for line in f:
	print(line)
	f.close()
'''
with open('PATH') as f:
	for line in f:
		print(line)#оставляет необрезанными переносы строк и добавляет свои
#print(line, end='')???
#print(f.read())???
'''
#ПОЧЕМУ НЕ ВХОДЯТ В BUILTINS - TRY/ EXCEPT, IF/ELSE...???
