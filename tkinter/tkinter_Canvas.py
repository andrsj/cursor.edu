import tkinter as tk


root = tk.Tk()


c1 = tk.Canvas(root, width = 500, height = 500, bg = "#FFF")
c1.pack()

c1.create_line(250,0,250,500, width = 3, fill = "#F00", arrow = tk.LAST)
c1.create_line(0,250,500,250, width = 3, fill = "#00F", arrow = tk.BOTH)

c1.create_rectangle(10,10,240,240, fill = "#0F0", outline = "#000")
c1.create_polygon(260,10,490,10,375.5,115,260,240,490,240, fill = "orange", smooth = 0, outline = "#000")
c1.create_oval(10,260,240,490, fill = "yellow", outline = "black", width = 3)

c1.create_arc(260,260,300,300, start = 0, extent = 270, fill = "#00C")
c1.create_arc(380,380,450,450, start = 0, extent = 270, outline = "#F0F", width = 3, style = "arc")

c1.create_text(275,330, text = "TKinter - \nprograms with UI\nand other items", font = ("Ubuntu", 15),
anchor = "w", justify = "center", fill = "black")


root.mainloop()