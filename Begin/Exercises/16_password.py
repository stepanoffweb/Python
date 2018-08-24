'''Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
Extra:    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.'''
def passw(complex):
	import random
	list_liters= [chr(random.choice([random.randint(97, 122), random.randint(48, 57), random.randint(65, 90)])) for i in range(12)]
	return ''.join([random.choice(list_liters) for i in range(complex)])



if __name__ == __name__:
	print(passw(int(input('How many symbols do you want?\n'))))
# либо мы пихаем в базу готовый список литералов для random.choice(), либо на заданнЫХ интервалах собираем строку random.randint() и обрабатываем ее chr(). Как задать несколько интервалов интов?  