import tkinter as tk
import time


def button_clicked():
    button['text'] = time.strftime('%H:%M:%S')

root = tk.Tk()

button = tk.Button(root)
button.configure(text=time.strftime('%H:%M:%S'), command=button_clicked)
button.pack()

root.mainloop()