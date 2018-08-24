'''На вход Вашей функции будет передано одно предложение. Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.
Обратите внимание на то, что не все исправления необходимы. Если предложение уже заканчивается на точку, то добавлять еще одну не нужно, это будет ошибкой
Входные аргументы: Строка (A string).
Выходные аргументы: Строка (A string).
Предусловия: В начале и конце нет пробелов, текст состоит только из пробелов, a-z A-Z , и . '''

def correct_sentence(sentence):
	sentence = sentence.split(' ')
	sentence[0]= sentence[0].capitalize()
	sentence= ' '.join(sentence)
	print(sentence)
	if sentence[-1]!= '.':
		sentence += '.'
	return sentence

# def correct_sentence(text: str) -> str:
    # text = text[0].upper()+text[1:]
    # if(text[-1] != "."):
        # text += "."
    # return text


# def correct_sentence(text: str) -> str:   
    # return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")

assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("hi") == "Hi."
assert correct_sentence("welcome to New York") == "Welcome to New York."#"Welcome to new york."
    
print("Coding complete? Click 'Check' to earn cool rewards!")
