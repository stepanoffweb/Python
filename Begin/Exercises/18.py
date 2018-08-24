'''	Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.'''
import random

'''num1 = ''.join(str(random.sample(range(0, 9), 4)))#[7, 3, 5, 6]
print(type(num1))'''


def main(num):
	guess_num=1
	num2= str(input('Give a 4-digit number: '))
	while num2!= num1:
		cow= 0
		bull=0
		i=0
		for dig in num1:
			if num2[i] in num1:# проверка наличия в коллекции(любой?)
				if dig== num2[i]:
					cow+=1
				else:
					bull+=1				
			i+=1# вапрос: при любом условии пока в цикле?-да!
		print('Your score is: {0} cows, {1} bulls.'.format(cow, bull))
		num2= str(input('Give a 4-digit number: '))
		guess_num+=1
	print('Game over with {} guesses!!'.format(guess_num))
		

num1= ''.join(['%s' %random.randint(0, 9) for x in range(4)])
print(num1)

if __name__ == '__main__':
	main(num1)