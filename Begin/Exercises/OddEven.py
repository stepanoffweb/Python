def odd_even(num):
	if num%2==0:
		print('Even')
		if num%4==0:
			print('And divides evenly on 4.')
	else:
		print('Odd')

def check(num, checker):
	if num%checker==0:
		print("Numbers are devided evenly.")
	else :
		print("Numbers aren't devided evenly.")

num = int(input("Give a number! "))
checker = int(input("And another one "))	
#odd_even(int(input("Give a number! ")))

odd_even(num)
check(num, checker)
