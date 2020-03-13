import tkinter as tk


def new_win():
    win = tk.Toplevel(root)
    label1 = tk.Label(win, text = "Text", font = 20)
    label1.pack()

def exit_app():
    root.destroy()


root = tk.Tk()

main_menu = tk.Menu()
root.configure(menu = main_menu)

first_item = tk.Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = "File", menu = first_item)
first_item.add_command(label = "New", command = new_win)
first_item.add_command(label = "Exit", command = exit_app)

second_item = tk.Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = "Edit", menu = second_item)
second_item.add_command(label = "Item1")
second_item.add_command(label = "Item2")
second_item.add_command(label = "Item3")
second_item.add_separator()
second_item.add_command(label = "Item4")
second_item.add_command(label = "Item5")


tool_bar = tk.Frame(root, bg = "#A1A1A1")
tool_bar.pack(side = tk.TOP, fill = tk.X)

btn1 = tk.Button(tool_bar, text = "  Cut  ")
btn1.grid(row = 0, column = 0, padx = 2, pady = 2)

btn2 = tk.Button(tool_bar, text = "  Copy  ")
btn2.grid(row = 0, column = 1, padx = 2, pady = 2)

btn3 = tk.Button(tool_bar, text = "  Paste  ")
btn3.grid(row = 0, column = 2, padx = 2, pady = 2)


status_bar = tk.Label(root, relief = tk.SUNKEN, anchor = tk.W, text = "Complete")
status_bar.pack(side = tk.BOTTOM, fill = tk.X)



root.mainloop()