import matplotlib.pyplot as plt
from random import uniform as uni
from matplotlib.widgets import TextBox
import random
import math


initial_text = "0,0"

def distance(a:tuple, b:tuple):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


if __name__ == '__main__':
    coords = ((1,1),(2,2))
    eps = 0.5
    count = 100
    points1 = [(coords[0][0] + uni(-eps, eps), coords[0][1] + uni(-eps, eps)) for i in range(count)]
    points2 = [(coords[1][0] + uni(-eps, eps), coords[1][1] + uni(-eps, eps)) for i in range(count)]

    p1 = random.choice(points1)
    p2 = random.choice(points2)

    plt.plot([x for x,y in points1+points2],[y for x,y in points1+points2],"ob")
    plt.plot([p1[0],p2[0]],[p1[1],p2[1]], 'og')

    for i in points1 + points2:
        to = p1 if distance(i,p1) < distance(i,p2) else p2
        plt.annotate('', xy=to, xytext=i ,arrowprops=dict(facecolor='black', arrowstyle="-", alpha=0.3))

    plt.grid()
    # plt.show()




    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)

    plt.plot([p1[0],p2[0]],[p1[1],p2[1]], 'og')

    def submit(text):
        text = text.split(',')
        x,y = float(text[0]),float(text[1])
        to = p1 if distance([x,y],p1) < distance([x,y],p2) else p2
        ax.annotate('', xy=to, xytext=[x,y] ,arrowprops=dict(facecolor='black', arrowstyle="-|>", alpha=0.3))
        c = 'b' if distance([x,y],p1) < distance([x,y],p2) else 'y'
        ax.scatter(x,y,color = c)
        plt.draw()

    axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
    text_box = TextBox(axbox, '', initial=initial_text)
    text_box.on_submit(submit)
    
    ax.grid()
    plt.show()