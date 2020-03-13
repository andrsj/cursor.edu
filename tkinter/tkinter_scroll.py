import tkinter as tk


root = tk.Tk()

text = tk.Text(root, height = 5, width = 60)
text.pack(side = 'left')

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side = 'left',fill = tk.Y)

# Connecting
scrollbar['command'] = text.yview
text['yscrollcommand'] = scrollbar.set

root.mainloop()