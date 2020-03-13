from random import random
from math import sqrt
from matplotlib.pyplot import plot, scatter, text, grid, show
def gen_claster(count, args): return [(random()+args[0],random()+args[1]) for _ in range(count)]
def train_pack(a,b): return a[:int(len(a)*0.8)]+b[:int(len(b)*0.8)]
def exam_pack(a,b): return a[int(len(a)*0.8):]+b[int(len(b)*0.8):]
def sum_first(train,i): return sum([x[i] for x in train[:int(len(train)/2)]])/(len(train)/2)
def sum_second(train,i): return sum([y[i] for y in train[int(len(train)/2):]])/(len(train)/2)
def etalons(train): return (sum_first(train,0),sum_first(train,1)),(sum_second(train,0),sum_second(train,1))
def distance(a,b): return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
def result(cord,exam): return [(i, distance(i,cord[0]) > distance(i,cord[1])) for i in exam]
def plot_examp(A,B): plot([i[0] for i in A+B],[j[1] for j in A+B],"ob")
def plot_train(A,B): plot([i[0] for i in train_pack(A,B)],[j[1] for j in train_pack(A,B)],"or")
def plot_etalon(A,B):
    for i in etalons(train_pack(A,B)): text(i[0],i[1],"Etalon claster ("+str(int(i[0]*10)/10)+";"+str(int(i[1]*10)/10)+")"); scatter(i[0],i[1], c = 'orange', marker = "s")
def plot_result(coords,A,B):
    for i in result(coords,exam_pack(A,B)): text(i[0][0],i[0][1],str(i[1]))
def plot_show(): grid(); show()
if __name__ == '__main__': count = 20; coords = (1,1),(3,3); A = gen_claster(count,coords[0]); B = gen_claster(count,coords[1]); plot_examp(A,B); plot_train(A,B); plot_etalon(A,B); '''plot_result(coords,A,B);'''; plot_show();