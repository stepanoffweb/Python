''' Вх. данные: Пароль как строка.
Вых. данные: Безопасность пароля в виде булевого значения (bool) или любого типа данных, который может быть сконвертирован и представлен как булево значение (True или False) 
Предусловия:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64 '''
def matching(passw):
# (matching(str))--> bool
	num = {i for i in range(48, 58)}
	capital= {i for i in range(65, 91)}
	lower= {i for i in range(97, 123)}
	#разбираем str(passw) на set и ищем   пересечение с заданными областями
	if len(passw)>=10 and len(passw)<=64:
		p= {ord(i) for i in passw}
		return not p.isdisjoint(num) and not p.isdisjoint(capital) and not p.isdisjoint(lower)
	else:
		return False
#print(matching(str(input("Your password, please "))))
'''
Одной строкой регулярки!
import re
# Вариант1
def checkio(data):
    # (?=) is positive lookahead. Use this construction to make sure the enclosed pattern exists
    return bool(re.search(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{10,}$', data))

# Вар2
def checkio(data):
    return True if re.search("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$", data) and len(data) >= 10 else False

# Вар3
def checkio(passw):
    digits = [dig for dig in passw if dig.isdigit()]
    uppers = [upp for upp in passw if upp.isupper()]
    lowers = [low for low in passw if low.islower()]
    return True if len(digits) and len(uppers) and len(lowers) and (len(passw) >= 10) else False




'''