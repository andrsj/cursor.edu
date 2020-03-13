import tkinter as tk


def callback(e):
    print(u'Нажата кнопка', e.widget['text'])

root = tk.Tk()

button1 = tk.Button(root, text = '  1  ')
button1.pack()
button2 = tk.Button(root, text = '  2  ')
button2.pack()

root.bind_class('Button', '<1>', callback)

root.mainloop()