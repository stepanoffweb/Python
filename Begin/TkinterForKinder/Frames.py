#Second video I present to Mickle: Frame

from tkinter import*

root= Tk()
root.geometry('800x600+200+150')
root.title('Helloo, Mickle!')
root.resizable(1, 0)
root.configure( bg= 'black')

frame1= Frame(root, bg= 'red', height= 50)
frame2= Frame(root, bg= 'blue', width= 100, height= 50)
frame3= Frame(root, bg= 'yellow', width= 50, height= 50)
frame4= Frame(root, bg= 'purple')
frame1.pack(fill= X)
frame2.pack()
frame3.pack()
frame4.pack(side= BOTTOM, fill= BOTH)










root.mainloop()