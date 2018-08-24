import tkinter as tk
from tkinter import ttk#to create a table that keeps data

class Main(tk.Frame):
	def __init__(self, root):#root?
		super().__init__(root)
		self.init_main()#call the func via constructor
		
	def init_main(self):#keep and initialise all the objects of GUI..
		toolbar= tk.Frame(bg= '#d7d8e0', bd= 2)
		toolbar.pack(side= tk.TOP, fill= tk.X)#expose the toolbar
		
		self.add_img= tk.PhotoImage(file= 'add.gif')#The icon for button
		btn_open_dialog= tk.Button(toolbar, text= 'Добавить позицию', command= self.open_dialog, bg= 		'#d7d8e0', bd= 0, compound= tk.TOP, image= self.add_img )
		btn_open_dialog.pack(side= tk.LEFT)
		
		self.tree= ttk.Treeview(self, columns= ('ID', 'description', 'costs', 'total'), height= 15, 
								show= headings)
		self.tree.column('ID', width=30, anchor= ttk.CENTER)
		self.tree.column('ID', width=30, anchor= ttk.CENTER)
		self.tree.column('ID', width=30, anchor= ttk.CENTER)
		self.tree.column('ID', width=30, anchor= ttk.CENTER)
		
		self.tree.heading('ID', text= 'ID')
		self.tree.heading('description', text= 'Наименование')
		self.tree.heading('costs', text= 'Статья расхода\дохода')
		self.tree.heading('total', text= 'Сумма') 

		self.tree.pack()
	def open_dialog(self):
		Child()


class Child(tk.Toplevel):#daughter window with the Input fields , toolbar and icon for button
	def __init__(self):#root |???
		super().__init__(root)
		self.init_child()#call the func via constructor
		
	def init_child(self):#keep and initialise all the objects of GUI..
		self.title("Добавить доходы/расходы")
		self.geometry("400x220+400+300")#???
		self.resizable(False, False)
		
		lable_description= tk.Lable(self, text= 'Наименование: ')
		lable_description.place(x= 50, y= 50)
		lable_select= tk.Lable(self, text= 'Статья дохода\расхода: ')
		lable_select.place(x= 50, y= 80)
		lable_sum= tk.Lable(self, text= 'Сумма: ')
		lable_sum.place(x= 50, y= 110)

		
		self.entry_description= ttk.Entry(self)
		self.entry_description.place(x= 200, y= 50)
		
		self.entry_money= ttk.Entry(self)
		self.entry_money.place(x= 200, y= 110)
		
		self.combobox= ttk.Combobox(self, values= [u'Доход', u'Расход'])
		self.combobox.current(0)
		self.combobox.place(x= 200, y= 80)
		
		self.grab_set()#hook all the events in the application
		self.focus_set()#keeps focus on subwindow


if __name__ =="__main__":
	root= tk.Tk()#main window?
	app = Main(root)
	app.pack()#Why not app=Main(root).pack()???
	root.title("Household keeper")
	root.geometry("650x350+300+200")#???
	root.resizable(False, False)
	root.mainloop()

	
