﻿''' Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.
Входные данные: Текст как строка (юникод).
Выходные данные: Секретное сообщение как строка или пустая строка.
Предусловие: 0 < len(text) ≤ 1000
all(ch in string.printable for ch in text)  '''
import re
def find_message(text):
	return  ''.join(re.findall(r'[A-Z]+', text))












if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")