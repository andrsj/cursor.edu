import tkinter as tk
import tkinter.ttk as ttk
import time

root = tk.Tk()
pb = ttk.Progressbar(root, length=100)
pb.pack()
pb.step(75)
# pb.start(75)
# pb.stop(75)
root.mainloop()