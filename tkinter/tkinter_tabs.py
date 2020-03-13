import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('300x150')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Первая')
tab_control.add(tab2, text='Вторая')

lbl1 = tk.Label(tab1, text='Вкладка 1')
lbl1.grid(column=0, row=0)
lbl2 = tk.Label(tab2, text='Вкладка 2')
lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

window.mainloop()