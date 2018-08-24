 # Input:сообщение как строка (только маленькие буквы и пробелы)
# Output: Тот же самый текст, но зашифрованный используя шифр Цезаря где каждая буква исходного текста заменяется другой, которая находится на определенном расстоянии в алфавите. Например, ("a b c", 3) == "d e f" 
# Предусловия:
# 0 < text < 50
# -26 < delta < 26 (длинна алфавита)(a= 97, z= 122)
# Как это используется: В криптографии, для сохранения важной информации, для сохранения секретности переписки.
delta= 0
pattern= ([x for x in range(97, 123)])*3
text = ''
text2= []

def main(text, delta):
	text= list(text)
	text2= []
	for i in text:
		i= ord(i)
		if i in pattern:
			n= pattern.index(i,26, 53)
			i= pattern[n + delta]
			i = chr(i)
		else: i= chr(i)
		text2.append(i)
	return ''.join(text2)

if __name__=='__main__':
	main(text, delta)

	assert main("a b c", 3) == "d e f"
	assert main("a b c", -3) == "x y z"
	assert main("simple text", 16) == "iycfbu junj"
	assert main("important text", 10) == "swzybdkxd dohd"
	assert main("state secret", -13) == "fgngr frperg"
	print("Coding complete? Click 'Check' to earn cool rewards!")

# import string
# def to_encrypt(text, delta):
    # n=''.join([str(string.ascii_lowercase[(string.ascii_lowercase.find(text[x])+delta)%26]) 
        # if string.ascii_lowercase.find(text[x])>=0 else str(' ') 
        # for x in range(len(text))])
    # return str(n)

