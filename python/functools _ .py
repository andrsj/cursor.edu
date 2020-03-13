from functools import partial
mybutton = partial(Button, root, fg=”black”,bg=”white”,font=”times”,size=”12”)
b1 = mybutton(text=”Ok”)            # Викличе Button() з аргументами text i
b2 = mybutton(text=”Cancel”)        # що були передані функції partial вище
b3 = mybutton(text=”Restart”)       #


p.func      # Функція, яка викличеться при виклику об'єкту р
p.args      # ...
p.keywords  # ...