'''Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
Concepts for this week:
    Functions
    Reusable functions
    Default arguments'''
def prime(int1):
	for i in range(1, int1):
		if int1%i==0:
			break
		else:
			return 'is prime'
	return 'is not prime'
	#return if int1%i==0 for i in range(1, int1)
print(prime(int(input('Give a number, please!\n'))))