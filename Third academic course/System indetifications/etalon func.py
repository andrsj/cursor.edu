import matplotlib.pyplot as plt
from random import uniform as uni
import math


def distance(a:tuple, b:tuple):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def train(points1,points2):
    return points1[:int(len(points1) * 0.8)] + points2[:int(len(points2) * 0.8)]

def exam_pack(points1,points2):
    return points1[int(len(points1) * 0.8):] + points2[int(len(points2) * 0.8):]

def etalons(train:list):
    return (
        (
            sum([x for x,y in train[:int(len(train) / 2)]]) / (len(train)/2), 
            sum([y for x,y in train[:int(len(train) / 2)]]) / (len(train)/2)
        ), 
        (
            sum([x for x,y in train[int(len(train) / 2):]]) / (len(train)/2), 
            sum([y for x,y in train[int(len(train) / 2):]]) / (len(train)/2)
        )
    )

def result(coords,exam):
    return [(i, distance(i,coords[0]) > distance(i,coords[1])) for i in exam]

if __name__ == "__main__":
    eps = 1
    count = 100
    coords = ((1,1),(3,3))
    points1 = [(coords[0][0] + uni(-eps, eps), coords[0][1] + uni(-eps, eps)) for i in range(count)]
    points2 = [(coords[1][0] + uni(-eps, eps), coords[1][1] + uni(-eps, eps)) for i in range(count)]

    x = etalons(train(points1,points2))
    plt.plot([x for x,y in points1+points2],[y for x,y in points1+points2],"ob")
    plt.plot([x for x,y in train(points1,points2)],[y for x,y in train(points1,points2)],".r")
    for i in etalons(train(points1,points2)):
        plt.scatter(i[0],i[1], c = 'green', marker = "s")

    for i in result(coords,exam_pack(points1,points2)):
        plt.text(i[0][0],i[0][1],str(i[1]))
    plt.grid()
    plt.show()
