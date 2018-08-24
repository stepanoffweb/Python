'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
Practice functions!'''
def fib(num):
	list_fib= []
	for i in range(num):
		if i==0 or i==1:
			list_fib.append(1)
		else:
			list_fib.append(list_fib[i-1] + list_fib[i-2])		
	return list_fib
	
print(fib(int(input('Give a number, please!\n'))))