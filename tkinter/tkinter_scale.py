import tkinter as tk

root = tk.Tk()

def getV(root):
    a = scale1.get()
    print("Значение: ", a)

scale1 = tk.Scale(root, orient = tk.HORIZONTAL, length = 300, from_ = 50, to = 80,
tickinterval = 5, resolution = 5)
button1 = tk.Button(root, text=u"Получить значение")
scale1.pack()
button1.pack()
button1.bind("<Button-1>",getV)
root.mainloop()