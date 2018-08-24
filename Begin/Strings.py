from sys import getsizeof

my_list= ['One', 'Two', 'Tree']	
my_str= ', '.join(my_list)
print(my_str)
string1= ""
string2= ''
print(getsizeof(string1))
print(type(string1))
print(getsizeof(string2))
'''
str(string3='')
print(getsizeof(string3))'''


print('Hello ' + 'world!')

print('Hello' [1: 3])
print('Hello'[:4])
print('Hello' [:-1])
print('Hello' [-1])
print('Hello'[::-1])
print('Hello'[::-2])

# my_string.index('CHARACTER') 	- ИЩЕМ ИНДЕКС ПЕРВОГО НУЖНОГО ЗНАКА (наприм. разделителя)
data = 'Xbox | 150 | New'
print(data.index('|'))
print(data[5])
product = data[:data.index('|')]
print(product)

# И нарезка строки по разделителям! find() vs index() - методы стринга
print(data.find('|'))# = 5
print(data[:data.find('|', 5)])# S.find(sub[, start[, end]]) -> int

# Делим строку по заданным разделителям
print(data.split('|'))

product1, product2, product3= data.split('|') # Продвинутое параметрирование (словарь?)
print(product1, product2, product3)
product1= 'Hello'
print(product1)
print({product1 : 'Opa!'})