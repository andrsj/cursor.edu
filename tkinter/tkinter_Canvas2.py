import tkinter as tk


def create_outline(event):
    c1.itemconfigure(oval1, outline = "black", width = 3)

def change_fill(event):
    c1.itemconfigure(oval2, fill = "orange")

def change_size(event):
    c1.coords(oval2, 210,10,390,190)

def move_ovals(event):
    c1.move("ovals", 0, 260)

def clear_all(event):
    c1.delete("all")


root = tk.Tk()

c1 = tk.Canvas(root, width = 400, height = 400, bg = "white")
c1.pack()

oval1 = c1.create_oval(10,10,90,90, width = 0, fill = "#F00", tag="ovals")
oval2 = c1.create_oval(310,10,390,90, width = 0, fill = "#00F", tag="ovals")

c1.tag_bind(oval1, "<Button-1>", create_outline)
c1.tag_bind(oval1, "<Button-3>", move_ovals)
c1.tag_bind(oval2, "<Button-1>", change_fill)
c1.tag_bind(oval2, "<Button-3>", change_size)



root.mainloop()