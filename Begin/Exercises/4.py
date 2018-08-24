'''
Exercise 4 Divisors
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, IT IS A NUMBER THAT DIVIDES EVENLY INTO ANOTHER NUMBER. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
 '''
 
 #Циклом делим на каждую))))
number = int(input('Give me a number!!!  '))
print([i for i in range(1, number+1) if number%i==0])#List Comprehension
'''divisors = []
for i in range(1, number+1):
		if number%i==0:
			#divisors.append(i)    		
			#lambda divisors: divisors.append(i)
			print(i)'''

#РАЗОБРАТЬСЯ С ЛЯМБДОЙ - КАК ПЕРЕДАТЬ АРГУМЕНТ не создавая выходную переменную заранее (divisors)