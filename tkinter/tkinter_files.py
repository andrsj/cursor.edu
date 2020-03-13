import tkinter as tk
import tkinter.filedialog as files


def open_file():
    openfile = files.askopenfilename()
    f = open(openfile,"r")
    text.insert(tk.END, f.read())
    f.close()

def save_file():
    savefile = files.asksaveasfilename()
    final_text = text.get(1.0,tk.END)
    f = open(savefile,"w")
    f.write(final_text)
    f.close()

# def exit_app():
#     root.quit()


root = tk.Tk()

main_menu = tk.Menu(root)
root.configure(menu = main_menu)

fisrt_item = tk.Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = "File", menu = fisrt_item)

fisrt_item.add_command(label = "Open", command = open_file)
fisrt_item.add_command(label = "Save", command = save_file)
# fisrt_item.add_command(label = "Exit", command = exit_app)
fisrt_item.add_command(label = "Exit", command = root.quit)

text = tk.Text(root, width = 40, height = 20, font = 15)
text.pack(expand = tk.YES, fill = tk.BOTH)


root.mainloop()