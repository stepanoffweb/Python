﻿#First video I present to Mickle: ROOT WINDOW

from tkinter import*# Импортируем ВСЕ содержимое модуля для удобства работыв (не придется постоянно указывать принадлежность методов (tkinter.Tk()))

root= Tk()# Создаем экземпляр класса? Tk() - Главное\ корневое окно, содержащее все остальные необходимые тебе элементы
root.geometry('800x600+200+150')#Придаем необходимые размеры и располагаем в удобном месте экрана ('dx x dy + x + y')
root.title('Helloo, Mickle!')# Заменяем стандартный заголовок окна Tk на свой
root.resizable(True, False)#Делаем окно фиксированного размера, либо изменяемым по одной из осей, непонятные слова можно заменить цифрами False - 0, True - 1 (1, 0)
root.configure( bg= 'black')# сюда можно добавлять по ходу дела все, что забыл в начале


root.mainloop()# Запускаем бесконечный цикл для отображения окна с виджетами