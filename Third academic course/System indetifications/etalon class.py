import matplotlib.pyplot as plt
from random import uniform as uni
import math


def distance(a:tuple, b:tuple):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

class Etalon:

    def __init__(self, coords:tuple, count:int = 10, eps:float = 1):
        """
        Coords -> ((x,y),(x,y))
        Count -> default = 10
        eps -> default = 1"""
        if len(coords) > 2:
            raise("So much points")
        self.eps = eps
        self.coords = coords
        self.count = count

        self.points1 = [(self.coords[0][0] + uni(-self.eps, self.eps), self.coords[0][1] + uni(-self.eps, self.eps)) for i in range(self.count)]
        self.points2 = [(self.coords[1][0] + uni(-self.eps, self.eps), self.coords[1][1] + uni(-self.eps, self.eps)) for i in range(self.count)]
    
    @property
    def points(self):
        """
        ALL points
        """
        return self.points1 + self.points2

    @property
    def training_pack(self):
        """
        Calculate 80% train points pack
        """
        return self.points1[:int(len(self.points1) * 0.8)] + self.points2[:int(len(self.points2) * 0.8)]
    
    @property
    def exam_pack(self):
        """
        Calculate 20% exam points pack
        """
        return self.points1[int(len(self.points1) * 0.8):] + self.points2[int(len(self.points2) * 0.8):]

    @property
    def etalon1(self):
        """
        Calculate first etalon
        """
        return (sum([x for x,y in self.training_pack[:int(len(self.training_pack) / 2)]]) / (len(self.training_pack)/2), sum([y for x,y in self.training_pack[:int(len(self.training_pack) / 2)]]) / (len(self.training_pack)/2))

    @property
    def etalon2(self):
        """
        Calculate second etalon
        """
        return (sum([x for x,y in self.training_pack[int(len(self.training_pack) / 2):]]) / (len(self.training_pack)/2), sum([y for x,y in self.training_pack[int(len(self.training_pack) / 2):]]) / (len(self.training_pack)/2))

    def display(self, clusster:bool, train_or_exam:bool, etalons:bool, result:bool):
        '''
        clusster - display points depending on the cluster [True or False]
        train_or_exam - mark train [True] points pack or exam [False]
        etalons - display etalons [True] or dosnt [False]
        result - display exam points depending on the cluster by etalons
        '''
        plt.figure(figsize = (12,6.4))

        if not clusster:
            plt.plot([x for x,y in self.points],[y for x,y in self.points],"ob")
        else:
            plt.plot([x for x,y in self.points1],[y for x,y in self.points1],"ob")
            plt.plot([x for x,y in self.points2],[y for x,y in self.points2],"oc")

        if train_or_exam:
            plt.plot([x for x,y in self.training_pack],[y for x,y in self.training_pack],".r")
        else:
            plt.plot([x for x,y in self.exam_pack],[y for x,y in self.exam_pack],".r")
        
        if etalons:
            plt.scatter(self.etalon1[0], self.etalon1[1], c = 'green', marker = "s", zorder = 9)
            plt.scatter(self.etalon2[0], self.etalon2[1], c = 'green', marker = "s", zorder = 9)
        
        plt.grid()

        if result:
            for i in self.result():
                marker = "+" if i[1] else "x"
                plt.scatter(i[0][0], i[0][1], marker = marker, s = 100, c = "#F6650C", zorder = 10)
        plt.show()

    def result(self):
        """
        List of points and class [False - first | True - second]
        """
        return [(i, distance(i,self.coords[0]) > distance(i,self.coords[1])) for i in self.exam_pack]



if __name__ == '__main__':
    e = Etalon(((1,1),(3,3)),100,1.1)
    print(Etalon.display.__doc__)
    e.display(True,True,False,False)
    e.display(True,True,True,False)
    e.display(True,True,True,True)