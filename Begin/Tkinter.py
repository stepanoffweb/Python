from tkinter import*

root= Tk()
root.geometry('800x600+200+150')
root.title('First window')


#Create Main menu with drop menues with all of the dialog windows
def new_window():
	pass
	
def exit_app():
	pass


main_menu= Menu(root)
root.configure(menu= main_menu)
first_drop= Menu(main_menu)
main_menu.add_cascade(label= 'File', menu= first_drop)
first_drop.add_command(label= 'New', command= new_window)
first_drop.add_separator()
first_drop.add_command(label= 'Exit', command= exit_app)

'''btn1= Button(main_menu, text= 'File', bg= 'black', bg= 'white', font= 'arial 12 bond')
btn1.bind(<'Button1'>, open_file)'''























mainloop()