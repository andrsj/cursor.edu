import tkinter as tk


def hide_show():
    if label["text"] != "LOL":
        label["text"] = "LOL"
    else:
        label["text"] = ""

    # if label.winfo_viewable():
    #     label.grid_remove()
    # else:
    #     label.grid()

root = tk.Tk()

label = tk.Label(text = u'LOL')
label.grid()
button = tk.Button(command = hide_show, text = u"Спрятать/показать")
button.grid()

root.mainloop()