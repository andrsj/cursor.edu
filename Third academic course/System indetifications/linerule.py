from random import random
from matplotlib import pyplot as plt
import math


class Linerule:
    def __init__(self, coords:tuple, count:int = 10, eps:float = 0.1, speed:float = 0.7):
        self.eps = eps
        self.coords = coords
        self.count = count
        self.speed = speed
        self.weights = [random(), random(), random()]

        self.points1 = [(self.coords[0][0] + random(), self.coords[0][1] + random()) for i in range(self.count)]
        self.points2 = [(self.coords[1][0] + random(), self.coords[1][1] + random()) for i in range(self.count)]

    def Sum(self, xy:tuple) -> float:
        return sum([xy * w for xy,w in zip(xy,self.weights)]) + self.weights[-1]

    def sigmoid(self, xy:tuple) -> float:
        return 1 / (1 + math.exp( -self.Sum(xy)))

    def sigmoid_dx(self, xy:tuple) -> float:
        return math.exp( - (self.Sum(xy))) / ((1 + math.exp( - (self.Sum(xy)))) ** 2)

    def Eps(self, T:float, xy:tuple) -> float:
        return 0.5 * (self.sigmoid(xy) - T) ** 2 <= self.eps

    def delta(self, T:float, xy:tuple) -> float:
        return (self.sigmoid(xy) - T) * self.sigmoid_dx(xy)

    def learn(self, T:float, xy:tuple):
        if self.Eps(T,xy): return False
        else:
            self.weights[0] -= xy[0] * self.speed * self.delta(T,xy)
            self.weights[1] -= xy[1] * self.speed * self.delta(T,xy)
            self.weights[2] -= self.speed * self.delta(T,xy)
            return True

    def learn_all(self):
        # k = 0
        # while True:
        #     for i in range(self.count):
        #         k += self.learn(0,self.points1[i])
        #         k += self.learn(1,self.points2[i])
        #     if k == 0: break
        #     k = 0


        k = 0
        while True:
            for i,j in zip(self.points1,self.points2):
                k += self.learn(0,i)
                k += self.learn(1,j)
            if k == 0: break
            k = 0


        # study = True
        # while study:
        #     for i,j in zip(self.points1,self.points2):
        #         one = self.learn(0,i)
        #         two = self.learn(1,j)
        #     if not (one or two): break
        
        
        
        print(self.weights)


    def koef(self):
        return ( - (self.weights[0] / self.weights[1]), - (self.weights[2] / self.weights[1]) )

    def display(self):
        plt.plot([x for x,y in self.points1],[y for x,y in self.points1],"ob")
        plt.plot([x for x,y in self.points2],[y for x,y in self.points2],"or")
        k1,k2 = self.koef()
        minx = min([x for x,y in self.points1] + [x for x,y in self.points2]) - 1
        maxx = max([x for x,y in self.points1] + [x for x,y in self.points2]) + 1
        plt.plot([minx,maxx],[minx * k1 + k2, maxx * k1 + k2], color = 'c')
        plt.grid()
        plt.show()

    def result(self):
        print(self.weights)
        self.learn_all()
        self.display()



if __name__ == "__main__":
    line = Linerule(coords = ((3,3),(1,2)), count = 15, eps = 0.05, speed = 0.8)
    line.result()
