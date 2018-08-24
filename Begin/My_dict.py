#Пытаем Dictionaries вместе со списками
phone_book = {
  'john' : ['John', 'Pijon', 'pijon@mail.cu', '8-921-007'],
  'piter' : ['Peter', 'Piper', 'piter@gmail.ru', '8-909-123']
  }
  
print(phone_book['piter'])
print(['john'],[0])
print(phone_book['john'][2])

piter_number= 'piter'[3]
#print(phone_book['john'][2], piter_number) #Как в одной строчке задать >1 ключ-значениe????
#print(phone_book['john'][2], ['piter'][2]) - не работает!!!





my_phone_book= {
  'bob': ['Robert', 'Gordon', 'robert@gmail.com', '8-921-007-6137'],
  'nina': ['Nina', 'Ivanovna', 'nina@mail.ru', '8-909-675-3435']
  }
print(my_phone_book['nina'][2])
print(['bob'])
print(my_phone_book['bob'])
