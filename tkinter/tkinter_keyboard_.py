import tkinter as tk

def print_char(event):
	label1.configure(text = event.char)

root = tk.Tk()
root.title("tkinter")

label1 = tk.Label(root, width = 12, font = ("Ubuntu",100))
label1.pack()

for i in range(65,123):
	root.bind(chr(i),print_char)

root.mainloop()