import tkinter as tk
import time

def tick():
    label.after(200, tick)
    label['text'] = time.strftime('%H:%M:%S')

root = tk.Tk()
root.geometry('500x400+300+200')

label = tk.Label(font='sans 20')
label.pack()
label.after_idle(tick)

root.mainloop()