import tkinter as tk

class Question:

    def __init__(self, main):
        self.entry1 = tk.Entry(main, width = 10, font = 15)
        self.button1 = tk.Button(main, text = "  Check  ")
        self.label1 = tk.Label(main, width = 20, font = 15)

        self.entry1.grid(row = 0, column = 0)
        self.button1.grid(row = 0, column = 1)
        self.label1.grid(row = 0, column = 2)

        self.button1.bind("<Button-1>",self.answer)

    def answer(self, event):
        txt = self.entry1.get()

        try:
            if int(txt) > 18:
                self.label1["text"] = "Cool"
            else:
                self.label1["text"] = "Bad"
        except ValueError:
            self.label1["text"] = "No int"

root = tk.Tk()
root.title = "Class Question"
q = Question(root)

root.mainloop()