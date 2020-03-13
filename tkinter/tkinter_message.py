import tkinter as tk
from tkinter import messagebox as message


root = tk.Tk()

btn1 = tk.Button(root, text = "Info", font = ("Ubuntu", 20), command = lambda: message.showinfo("ShowInfo","Info"))
btn1.grid(row = 0, column = 0, sticky = "ew")

btn2 = tk.Button(root, text = "Warning", font = ("Ubuntu", 20), command = lambda: message.showwarning("ShowWarning","Warning!"))
btn2.grid(row = 1, column = 0, sticky = "ew")

btn3 = tk.Button(root, text = "Error", font = ("Ubuntu", 20), command = lambda: message.showerror("ShowError","Error!"))
btn3.grid(row = 2, column = 0, sticky = "ew")

root.mainloop()