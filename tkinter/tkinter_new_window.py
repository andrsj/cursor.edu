import tkinter as tk

root = tk.Tk()
root.title("LMAO")
root.geometry("200x150")
root.iconbitmap("python.ico")

def open_window():
    top = tk.Toplevel()
    top.title("LOL")
    top.geometry("200x150")
    top.iconbitmap("python.ico")
    label = tk.Label(top, text = "LOL", font = ("Ubuntu",20))
    label.pack()
    btn2 = tk.Button(top, text = "Close", font = ("Ubuntu",20), command = top.destroy)
    btn2.pack()
    top.mainloop()

btn1 = tk.Button(root, text = "Open", font = ("Ubuntu",20), command = open_window)
btn1.pack()
btn2 = tk.Button(root, text = "Close", font = ("Ubuntu",20), command = root.destroy)
btn2.pack()

root.mainloop()