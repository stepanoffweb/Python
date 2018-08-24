'''Exercise 9 
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
Extras:
    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
Discussion
Concepts for this week:
    Modules
    Random numbers
    User input'''
import random# можно ли импорт вставлять в определение своей функции?
	
def compare(x, y):
	if x>y:
		return 'Too low!'
	elif x<y:
		return 'Too high!'
	else:
		return 'Yes! Exectly right!!!'
count= 0		
while 1:
	x= random.randint(1,9)
	gamer= input('Number from 1 to 9, please \n')
	if gamer== 'exit':
		break
	else:
		y= int(gamer)
		count+=1
		print(x)
		print(compare(x, y))
print('Game is over!', count, 'times trying')