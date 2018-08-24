''' RockScissorsPaper'''

def matching():
	gamer1= 'Bob'
	gamer2= 'Rob'
	Key1= str(input('Take S, R or P..\n'))
	Key2= str(input('Take! \n'))
	para= (Key1, Key2)
	game= {Key1: gamer1, Key2: gamer2}
		
	if para== ('S', 'R') or para==('R', 'S'):
		return game['R']
	if para== ("S", "P") or para==('P', 'S'):
		return game['S']
	if para== ("P", "R") or para==('R', 'P'):
		return game['P']
	else:
		return 'Nobody '#тупо отсекает любой некорректный ввод
print('Winner is ', matching())

'''#Долго зависал на операторах в условии: хотел сгруппировать if para==(('S', 'R')or('R','S'))но это не работает(
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert manching('A1213pokl') == False, "1st example"
    assert manching('bAse730onE4') == True, "2nd example"
    assert manching('asasasasasasasaas') == False, "3rd example"
    assert manching('QWERTYqwerty') == False, "4th example"
    assert manching('123456123456') == False, "5th example"
    assert manching('QwErTy911poqqqq') == True, "6th example"
print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")'''