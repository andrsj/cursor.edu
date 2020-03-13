import tkinter as tk


root = tk.Tk()

tk.Button(root, text = '1').pack(side = 'left')
tk.Button(root, text = '2').pack(side = 'top')
tk.Button(root, text = '3').pack(side = 'right')
tk.Button(root, text = '4').pack(side = 'bottom')
tk.Button(root, text = '5').pack(fill = 'both')

root.mainloop()