''' Дано положительное число как строка и основание системы счисления для него. Ваша функция должна конвертировать это число в десятичную систему счисления. Основание системы счисления меньше 37 и больше 1. В задаче используются цифры и буквы A-Z внутри строчного представления числа.
Будьте осторожны со случаями, когда число нельзя сконвертировать. Для примера: "1A" не может быть сконвертировано при основании системы счисления 9. В этих случаях ваша функция должна возвращать -1. 
 Вх. данные: Два аргумента. Число как строка (str) и основание системы счисления как целочисленное (int).
Вых. данные: Сконвертированное число как целочисленное (int).
Предусловия:
re.match("\A[A-Z0-9]\Z", str_number)
0 < len(str_number) ≤ 10
2 ≤ radix ≤ 36 
'''
def checkio(num, base):
	try: return int(num, base)
	except ValueError:	return  -1
#other2dec = lambda n, other:  sum([(int(v) * other**i) for i, v in enumerate(list(str(n))[::-1])])

    # wynik=0;
    # k=len(str_number)-1
    # abc="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # error=False
    # for i in str_number:
        # if abc.find(i)!=-1 and abc.find(i)<radix:
            # liczba=abc.find(i)        
            # wynik+=liczba*pow(radix,k)
            # k-=1
        # else: error=True
    # if error : wynik=-1
    # return wynik


'''
>>> help(__builtins__.int)
Help on class int in module builtins:

class int(object)
 |  int(x=0) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4'''
if __name__ == '__main__':
	assert checkio("AF", 16) == 175, "Hex"
	assert checkio("101", 2) == 5, "Bin"
	assert checkio("101", 5) == 26, "5 base"
	assert checkio("Z", 36) == 35, "Z base"
	assert checkio("AB", 10) == -1, "B > A = 10"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")