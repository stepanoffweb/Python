
from tkinter import*

root= Tk()
root.title('Превед, товарисч!!')
root.geometry('650x350+800+200')
#root.resizable(False, False)
#root.configure(menu= , )
toolbar= Frame(root, bg= '#002', bd= 2)
toolbar.pack(fill= BOTH)
frame2= Frame(root, bg= 'white', height=30)
frame2.pack(fill= BOTH)
field= Frame(root, bg= 'red')
field.pack(side= BOTTOM, fill= BOTH)

#label1= Label(frame1, bg= 'blue')
#abel1.pack(expand= YES, fill= BOTH)



root.mainloop() 