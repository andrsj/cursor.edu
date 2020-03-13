import tkinter as tk

def window_deleted():
    print(u'Окно закрыто')
    root.quit() # явное указание на выход из программы

root = tk.Tk()
root.title(u'Пример приложения')
root.geometry('500x400+300+200') # ширина=500, высота=400, x=300, y=200
root.protocol('WM_DELETE_WINDOW', window_deleted) # обработчик закрытия окна
root.resizable(True, False) # размер окна может быть изменён только по горизонтали
root.mainloop()