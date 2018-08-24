import random

for i in range(10):
	print(random.normalvariate(3, 2))
	
a= [random.randint(1, 100) in range(10)]
print(a)
a = [random.randint(1, 100) for i in range(20) ]# попытка List Comprehension
print(a)
a= 22,33,44,55,66
print(type(a), a)
print(random.choice(a))
print(random.choice(22,33,44,55,66))#TypeError: choice() takes 2 positional arguments but 6 were given WTF!!!