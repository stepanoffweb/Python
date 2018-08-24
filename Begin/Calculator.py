from tkinter import*

cal = Tk()
cal.title("Calculator")
operator=""
text_Input=StringVar()

txtDisplay = Entry(cal, font= ('arial', 20, 'bold'), textVariable= text_Input, bd= 30, insertwidth= 4, bg='powder blue', justify= 'right').grid(columnspan= 4) #WE CAN RUN IT ALREADY - IT GIVE A ENTRY WINDOW		


btn7= Button(cal, padx= 16, bd= 8, fg= 'black', font= ('arial', 20, 'bold'), 
			text= "7").grid(row=1, column= 0)
btn8= Button(cal, padx= 16, bd= 8, fg= 'black', font= ('arial', 20, 'bold'), 
			text= "7").grid(row=1, column= 1)
btn9= Button(cal, padx= 16, bd= 8, fg= 'black', font= ('arial', 20, 'bold'), 
			text= "7").grid(row=1, column= 2)
Addition= Button(cal, padx= 16, bd= 8, fg= 'black', font= ('arial', 20, 'bold'), 
			text= "+").grid(row=1, column= 3)

#WE HAVE A FIRST ROW OF BUTTONS
#====================================================================================







cal.mainloop()
