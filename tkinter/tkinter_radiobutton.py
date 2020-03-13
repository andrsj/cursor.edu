import tkinter as tk

root = tk.Tk()
var = tk.IntVar()

rbutton1 = tk.Radiobutton(root ,text = '1', variable = var, value = 1)
rbutton2 = tk.Radiobutton(root ,text = '2', variable = var, value = 2)
rbutton3 = tk.Radiobutton(root ,text = '3', variable = var, value = 3)
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()

root.mainloop()