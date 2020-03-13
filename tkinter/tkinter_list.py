import tkinter as tk


root = tk.Tk()
listbox1 = tk.Listbox(root, height = 5, width = 15, selectmode = tk.EXTENDED)
listbox2 = tk.Listbox(root, height = 5, width = 15, selectmode = tk.SINGLE)
list1 = [
    u"Москва",
    u"Санкт-Петербург",
    u"Саратов",
    u"Омск"
]
list2 = [
    u"Канберра",
    u"Сидней",
    u"Мельбурн",
    u"Аделаида"
]

for i in list1:
    listbox1.insert(tk.END,i)
for i in list2:
    listbox2.insert(tk.END,i)

listbox1.pack()
listbox2.pack()

root.mainloop()