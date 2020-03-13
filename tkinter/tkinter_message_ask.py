import tkinter as tk
import tkinter.messagebox as message


def ask_question(event):
    answer = message.askquestion("Ask question","First")
    label1.configure(text = answer)

def ask_ok(event):
    answer = message.askokcancel("AskOkCancel","Second")
    label2.configure(text = answer)

def ask_yes_no(event):
    answer = message.askyesno("AskYesNo","3th")
    label3.configure(text = answer)

def ask_rc(event):
    answer = message.askretrycancel("AskRetryCancel","4th")
    label4.configure(text = answer)

def ask_ync(event):
    answer = message.askyesnocancel("AskYesNoCancel","5th")
    label5.configure(text = answer)

root = tk.Tk()


##################
btn1 = tk.Button(root, text = "Ask question", font = ("Ubuntu",20), width = 12)
btn1.grid(row = 0, column = 0, sticky = "ew")

label1 = tk.Label(root, font = ("Ubuntu",20), width = 12)
label1.grid(row = 0, column = 1)

btn1.bind("<Button-1>",ask_question)


###################
btn2 = tk.Button(root, text = "Ask Ok|Cancel", font = ("Ubuntu",20), width = 12)
btn2.grid(row = 1, column = 0, sticky = "ew")

label2 = tk.Label(root, font = ("Ubuntu",20), width = 12)
label2.grid(row = 1, column = 1)

btn2.bind("<Button-1>",ask_ok)


###################
btn3 = tk.Button(root, text = "Ask Yes|NO", font = ("Ubuntu",20), width = 12)
btn3.grid(row = 2, column = 0, sticky = "ew")

label3 = tk.Label(root, font = ("Ubuntu",20), width = 12)
label3.grid(row = 2, column = 1)

btn3.bind("<Button-1>",ask_yes_no)


###################
btn4 = tk.Button(root, text = "Ask Retry|Cancel", font = ("Ubuntu",20))
btn4.grid(row = 3, column = 0, sticky = "ew")

label4 = tk.Label(root, font = ("Ubuntu",20), width = 12)
label4.grid(row = 3, column = 1)

btn4.bind("<Button-1>",ask_rc)


###################
btn5 = tk.Button(root, text = "Ask Yes|No|Cancel", font = ("Ubuntu",20))
btn5.grid(row = 4, column = 0, sticky = "ew")

label5 = tk.Label(root, font = ("Ubuntu",20), width = 12)
label5.grid(row = 4, column = 1)

btn5.bind("<Button-1>",ask_ync)

##################
root.mainloop()