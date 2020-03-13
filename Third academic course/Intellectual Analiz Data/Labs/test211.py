import math
import random
from matplotlib import pyplot as plt
# За допомогою однонейронної мережі реалізувати класифікатор 
# вхідного потоку даних на два класи, які задані фіксованим набором векторів
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#Задаємо центри кластерів
def gen_vec():
    a = []
    b = []
    # генеруємо по десять векторів з кожного класу
    for i in range(10):
        a.append([3 + random.uniform(0 ,1), 3 + random.uniform(0, 1)])
        b.append([1 + random.uniform(0, 1), 1 + random.uniform(0, 1)])
    return a, b

#суматор
def suma(x, w):
    s = 0
    for j in range(len(x)):
        s += w[j] * x[j]
    s += w[2]
    return s

#сигмоїдальна функція активації
def f_out(s):
    return 1 / (1 + math.exp(- (s)))

#похідна сигмоїдальна функція активації
def f_out_dx(s):
    return math.exp(- (s)) / ((1 + math.exp(- (s))) ** 2)

#Похибка середньократичним відхиленням на кожному кроці
def eps(t, out):
    return 0.5 * (out - t)**2

#Похибка на похідну сигмоїдальна функція активації
def delta(t, out, s):
    return (out - t) * f_out_dx(s)

#Навчання
def iter_f(i, t, arr, w):
    #Зважена сума
    s = suma(arr[i], w)

    #Функція активації
    out = f_out(s)
    e = eps(t, out) # похибка

    #Перевірка значення похибки
    if e <= 0.1:
        return 0

    d = delta(t, out, s)
    n = 0.7 # швидкість навчання

    #Підбирання ваг
    w[0] -= n * d * arr[i][0]
    w[1] -= n * d * arr[i][1]
    w[2] -= n * d
    return 1

def main():
    # Вхідні дані
    arr_a, arr_b = gen_vec()
    #генерування початкових ваг
    arr_w = [random.random(), random.random(), random.random()]
    
    kilk = 0
    while True: # коефіцієнт відстані
        for i in range(len(arr_a)):
            kilk += iter_f(i, 0, arr_a, arr_w)
            kilk += iter_f(i, 1, arr_b, arr_w)
        if kilk == 0:
            break
        kilk = 0

    #Графічний вивід
    koef = [- (arr_w[1] / arr_w[0]), - (arr_w[2] / arr_w[0])]# коефіцієнт прямої
    arr1 = []
    arr2 = []

    a = 1.0 

    while a <= 4.0:
        arr1.append(a)
        arr2.append(a * koef[0] + koef[1])
        a += 1

    ax1.clear()
    ax1.plot(arr1, arr2, color="blue")

    for i in range(10):
        # ax1.plot(arr_a[i][0], arr_a[i][1], "ro", color="green")
        ax1.scatter(arr_a[i][0], arr_a[i][1], color="green")
        # ax1.plot(arr_b[i][0], arr_b[i][1], "ro", color="red")
        ax1.scatter(arr_b[i][0], arr_b[i][1], color="red")

    ax1.grid()
    print(arr_w)

def refrash():
    main()
    plt.show()

refrash()
