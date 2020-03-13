import tkinter as tk


root = tk.Tk()

var1 = tk.IntVar()
var2 = tk.IntVar()
check1 = tk.Checkbutton(root ,text=u'1 пункт' ,variable = var1 ,onvalue = 1 ,offvalue = 0)
check2 = tk.Checkbutton(root ,text=u'2 пункт' ,variable = var2 ,onvalue = 1 ,offvalue = 0)

check1.pack()
check2.pack()

root.mainloop()