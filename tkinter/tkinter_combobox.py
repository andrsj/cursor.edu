import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

frame = tk.Frame(root)
frame.grid()

combobox = ttk.Combobox(frame, values = [u"ОДИН",u"ДВА",u"ТРИ"], height = 3)
#frame - задает родительский виджет, на его территории будет располагаться Combobox
#values - задает набор значений, которые будут содержаться в Combobox изначально
#height - задает высоту выпадающего списка. Если число элементов списка меньше 11, то можно не задавать.

combobox.set(u"ОДИН")
combobox.grid(column = 0, row = 0)

root.mainloop()