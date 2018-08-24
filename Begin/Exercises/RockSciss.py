def matching():
	''' S>P, P>R, R>S'''

	gamer1 = str(input('Gamer1,take S, R or P !\n'))
	gamer2 = str(input('Gamer2, take S, R or P !\n'))
	case1= 'Gamer1  won!'
	case2 = 'Gamer2  won!'
	case3= 'Nothing! Go on!!!'
	
	if gamer1 in ('S', 'R', 'P') and gamer2 in ('S', 'R', 'P'):
		if gamer1=='S':
			if gamer2=='R':
				return case2
			elif gamer2== 'P':
				return case1
			else :
				return case3
		elif gamer1== 'R':
			if gamer2== 'S':
				return case1
			elif gamer2== 'P':
				return case2
			else :
				return case3
		elif gamer1== 'P':
			if gamer2== 'R':
				return case1
			elif gamer2== 'S':
				return case2
			else :
				return case3
	else:
		return 'Attention!! Your input is wrong!'
	
print(matching())
# РАБОТАЕТ, НО ПОЛНОЕ ГОВНО:у чурки вариант взрыв мозга на основе модуля числа...