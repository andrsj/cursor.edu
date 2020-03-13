
# Python code to illustrate 
# Decorators with parameters in Python 

def decorator(*args, **kwargs):
    print("Inside decorator")
    def inner(func):
        print("Inside inner function")
        print("I like", kwargs['like'])
        return func
    return inner

@decorator(like="geeksforgeeks")
def func():
    print("Inside actual function")

if __name__ == '__main__':
    print("Start")
    func()
