import tkinter as tk
from random import random

def button_clicked():
    button['text'] = button['bg'] # показываем предыдущий цвет кнопки
    bg = '#%0x%0x%0x' % (int(random()*16), int(random()*16), int(random()*16))
    button['bg'] = bg
    # button['activebackground'] = bg

root = tk.Tk()

button = tk.Button(root, command=button_clicked, width = 30)
button.pack()

root.mainloop()