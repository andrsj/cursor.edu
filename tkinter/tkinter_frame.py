import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root,bg='green',bd=5)
frame2 = tk.Frame(root,bg='red',bd=5)

button1 = tk.Button(frame1,text=u'Первая кнопка')
button2 = tk.Button(frame2,text=u'Вторая кнопка')

frame1.pack()
frame2.pack()
button1.pack()
button2.pack()

root.mainloop()