from tkinter import*

def btnClick(num):
	global operator#WTF - Why it within the function? its GLOBAL! 
	operator= operator+ str(num)
	textInput.set(operator)
	
def btnClearDysplay():
	global operator
	operator= ""
	textInput.set("")
	
def btnEqualsInput():
	global operator
	sumup= str(eval(operator))
	textInput.set(sumup)
	operator= ""




cal= Tk()
cal.title("SuperCalc")
operator= ""# WTF - see above

textInput= StringVar()#Is the variable strongly defined by tkinter???
textBox= Entry(cal, font= ('arial', 20, 'bold'), textvariable= textInput, bd= 10, insertwidth= 4, bg= 'powder blue', justify= 'right').grid(columnspan= 4)


btn7= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= '7', command=lambda:  btnClick ('7')).grid( row=1, column=0)
btn8= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= '8' , command=lambda:  btnClick('8')).grid( row=1, column=1)
btn9= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= '9', command=lambda:  btnClick ('9')).grid(row=1, column=2)
Addition= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= '+', command=lambda:  btnClick('+') ).grid(row=1, column=3 )

#=====================================================================
btn4= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= '4', command=lambda:  btnClick('4') ).grid( row=2, column=0)
btn5= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= '5', command=lambda:  btnClick('5') ).grid( row=2, column=1)
btn6= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= '6', command=lambda:  btnClick ('6')).grid(row=2, column=2)
Substruction= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= ' -', command= btnClick('-') ).grid(row=2, column=3)
#========================================================================
btn3= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= '3', command=lambda:  btnClick ('3')).grid( row=3, column=0)
btn2= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= '2', command=lambda:  btnClick('2') ).grid( row=3, column=1)
btn1= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= '1', command= lambda: btnClick('1') ).grid(row=3, column=2)
Multiply= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= ' *' , command= lambda: btnClick('*')).grid(row=3, column=3)
#======================================================================
btn0= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= '0', command= lambda: btnClick('0')).grid( row=4, column=0)
btnClear= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= 'C', command= btnClearDysplay ).grid( row=4, column=1)
btnEquals= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= '=', command= btnEqualsInput).grid(row=4, column=2)
Devide= Button(cal, padx= 16, pady= 16, bd= 6, fg= 'black', bg= 'powder blue', font= ('arial', 20, 'bold'), text= ' /', command= lambda: btnClick('/')).grid(row=4, column=3)


cal.mainloop()
##Without lambda did not work...WHY?
#NOW IT DOES NOT WORK!!! Try it, try )))- there are some mistakes--> finde them.