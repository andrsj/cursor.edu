import time
import random
import timeit


def time_dec(func):
    def wrapper():
        now = time.monotonic()
        func()
        end = time.monotonic()
        print(f"Time: {end - now} msec")
    return wrapper

# def decor_with_param(times):
#     def inner(func):
#         func()
#     return inner

# @time_dec
def generate_list_with_random_values_using_comprehesion():
    '''
    Generate values in range from 1 to 100 using comprehesion
    Length = 10000
    '''
    return [random.randint(0,100) for _ in range(10000)]

# @time_dec
def generate_list_with_random_values_using_cicle():
    '''
    Generate values in range from 1 to 100 using cicle
    Length = 10000
    '''
    arr = []
    for _ in range(10000):
        arr.append(random.randint(0,100))
    return arr

if __name__ == '__main__':
    t = timeit.Timer(
        'generate_list_with_random_values_using_comprehesion()', 
        'from __main__ import generate_list_with_random_values_using_comprehesion'
    )
    time = t.timeit(100)
    print(f"Time: {time}")

    tt = timeit.Timer(
        'generate_list_with_random_values_using_cicle()', 
        'from __main__ import generate_list_with_random_values_using_cicle'
    )
    time = tt.timeit(100)
    print(f"Time: {time}")


#HW LOGGING