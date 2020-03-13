import matplotlib.pyplot as plt
import numpy as np

import sys
def progressBar(value, endvalue, bar_length=20):

    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()

img = plt.imread("photo.jpg")
k = 1/10

arr = [
    [1,1,1],
    [1,2,1],
    [1,1,1]
]


im = []
for i in range(len(img)):
    px = []
    for j in range(len(img[0])):
        px.append([0,0,0])
    im.append(px)

im = np.array(im)

for i in range(1,len(img) - 1):
    for j in range(1,len(img[0]) - 1):
        for k in range(3):
            a = k * (
                (arr[0][0] * img[i-1][j-1][k] + arr[0][1] * img[i-1][j][k] + arr[0][2] * img[i-1][j+1][k]) +
                (arr[1][0] * img[i][j-1][k] + arr[1][1] * img[i][j][k] + arr[1][2] * img[i][j+1][k]) +
                (arr[2][0] * img[i+1][j-1][k] + arr[2][1] * img[i+1][j][k] + arr[2][2] * img[i+1][j+1][k])
            )
            im[i][j][k] = a if a <= 255 else 255
            progressBar(i, len(img) -2 , 100)

plt.imshow(im)
plt.show()