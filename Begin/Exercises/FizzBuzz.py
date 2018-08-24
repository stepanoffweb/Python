'''Напишите программу, которая печатает числа от 1 до 100. Но для кратных трём значений - «Fizz» вместо номера и для кратных пяти - «Buzz». Для чисел, одновременно кратных трём и пяти — «FizzBuzz».'''

for i in range(100):
	if i%3==0 and i%5==0:
		print('FizzBuzz')
	elif i%3==0:
		print('Fizz')
	elif i%5==0:
		print('Buzz')
	else:
		print(i)

#print([i='FizzBuzz' if i%3==0 and i%5==0 elif i%3==0 i='Fizz' elif i%5==0 i='Buzz' else i for i in range(100)])
#Вот как хотелось бы!!!