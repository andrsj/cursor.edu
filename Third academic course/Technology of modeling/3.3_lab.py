import pygame, math
from pygame import *
from math import *
import matplotlib.pyplot as plt

#Win param
WIN_WIDTH = 900
WIN_HEIGHT = 600
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
SPACE_COLOR = "#000066"
GROUND_COLOR = "brown"
OBJECT_COLOR = "pink"
DOT_COLOR = 'white'

#Erth position
XE = 0
YE = WIN_HEIGHT - WIN_HEIGHT/10

#Erth mass
MO = 5000

#Object param
H = 3.3
RELH = H*150
OBJECT_WIDTH = 20
OBJECT_HEIGHT = 20

#Object position
XO = int(WIN_WIDTH / 3 - OBJECT_WIDTH / 2)
XO1 = int(WIN_WIDTH * 0.66 - OBJECT_WIDTH / 2)
YO = int(WIN_HEIGHT - (RELH + OBJECT_HEIGHT + WIN_HEIGHT/10))

def main():

    #PyGame init
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Model gravity.")

    #Erth init
    bg = Surface((WIN_WIDTH,WIN_HEIGHT))  
    bg.fill(Color(SPACE_COLOR))  
    draw.rect(bg, Color(GROUND_COLOR), (XE, YE, WIN_WIDTH,WIN_HEIGHT/10))  

    #Timer init                     
    timer = pygame.time.Clock()

    #Planet init
    obj = Surface((OBJECT_WIDTH, OBJECT_HEIGHT))
    obj.fill(Color(OBJECT_COLOR))
    draw.rect(obj, Color(OBJECT_COLOR), (XO, YO, OBJECT_HEIGHT, OBJECT_WIDTH))
    obj1 = Surface((OBJECT_WIDTH, OBJECT_HEIGHT))
    obj1.fill(Color(OBJECT_COLOR))
    draw.rect(obj1, Color(OBJECT_COLOR), (XO1, YO, OBJECT_HEIGHT, OBJECT_WIDTH))
    
    #Text init
    text = Surface((100, 50))
    font = pygame.font.Font('freesansbold.ttf', 16) 
    text = font.render('Без опору повітря', True, Color('yellow'), Color(SPACE_COLOR))
    text1 = Surface((100, 50))
    font = pygame.font.Font('freesansbold.ttf', 16) 
    text1 = font.render('З опором повітря', True, Color('yellow'), Color(SPACE_COLOR))
    #Initial object pos, speed and accel
    y0 = YO
    x0 = XO
    y = y0
    vy = 0
    yo = y0
    vyo = 0
    ay = 9.8
    Ay = 0
    m = 75
    k = 3
    T = 0
    DT = 30
    done = False

    screen.blit(bg, (0,0))
    screen.blit(obj, (int(x0), int(y)))
    screen.blit(obj1, (int(XO1), int(yo)))
    screen.blit(text, (int(x0+40), int(y))) 
    screen.blit(text1, (int(XO1+40), int(yo))) 
    pygame.display.update() 

    print('\t YO = ',round(y,3),'\t YO1 = ',round(y,3),'\t YE = ',YE,'\t TE = ',T,'\t DTE = ',DT)
    
    while not done:

        for e in pygame.event.get():
            if e.type == QUIT:
                done = True
                break   
        
        T += DT/1000
        timer.tick(DT)
        vy += ay*(DT/1000)
        y += vy*(DT/1000)/2

        Ay = ay - k*vyo/m
        yo += vyo*(DT/1000)/2
        vyo += Ay*(DT/1000)
        print('V = ',round(vyo,7),'\tAy = ', round(Ay,5))
        
        print('\t YO = ',round(y,3),'\t YO1 = ',round(yo,3),'\t YE = ',YE,'\t TE = ',T,'\t DTE = ',DT)

        if (y + DT*vy/1000 + OBJECT_HEIGHT) > YE:

            dones = False

            while not dones: 
                screen.blit(bg, (0,0))
                screen.blit(obj, (int(x0), int(YE - OBJECT_HEIGHT)))
                screen.blit(text, (int(x0+40), int(YE - OBJECT_HEIGHT)))  

                T += DT/1000
                timer.tick(DT)
                vy += ay*(DT/1000)
                y += vy*(DT/1000)/2
                Ay = ay - k*vyo/m
                yo += vyo*(DT/1000)/2
                vyo += Ay*(DT/1000)
                print('V = ',vyo,' Ay = ', Ay)
                
                print('\t YO = ',round(y,3),'\t YO1 = ',round(yo,3),'\t YE = ',YE,'\t TE = ',T,'\t DTE = ',DT)
                print("Object1 on the ground")

                if (yo + DT*vyo/1000 + OBJECT_HEIGHT) > YE:

                    screen.blit(bg, (0,0))
                    screen.blit(obj, (int(x0), int(YE - OBJECT_HEIGHT)))
                    screen.blit(text, (int(x0+40), int(YE - OBJECT_HEIGHT))) 
                    screen.blit(obj1, (int(XO1), int(YE - OBJECT_HEIGHT)))
                    screen.blit(text1, (int(XO1+40), int(yo))) 
                    pygame.display.update() 

                    Ay = ay - k*vyo/m
                    yo += vyo*(DT/1000)/2
                    vyo += Ay*(DT/1000)
                    print('V = ',vyo,' Ay = ', Ay)

                    print('\t YO = ',round(y,3),'\t YO1 = ',round(yo,3),'\t YE = ',YE,'\t TE = ',T,'\t DTE = ',DT)
                    print("Object2 on the ground")
                    print('End')


                    don = False
                    while not don:

                        T += DT/1000
                        timer.tick(DT)
                        Ay = ay - k*vyo/m
                        yo += vyo*(DT/1000)/2
                        vyo += Ay*(DT/1000)
                        
                        print('V = ',vyo,' Ay = ', Ay)
                        print('\t YO = ',round(y,3),'\t YO1 = ',round(yo,3),'\t YE = ',YE,'\t TE = ',T,'\t DTE = ',DT)
                    
                        if Ay <= 0:


                            dones = True
                            done = True
                            don = True 
                            break
                
                screen.blit(bg, (0,0))
                screen.blit(obj, (int(x0), int(YE - OBJECT_HEIGHT)))
                screen.blit(text, (int(x0+40), int(YE - OBJECT_HEIGHT))) 
                screen.blit(obj1, (int(XO1), int(yo)))
                screen.blit(text1, (int(XO1+40), int(yo))) 
                pygame.display.update() 
        else:
            screen.blit(bg, (0,0))
            screen.blit(obj, (int(x0), int(y)))
            screen.blit(obj1, (int(XO1), int(yo)))
            screen.blit(text, (int(x0+40), int(y))) 
            screen.blit(text1, (int(XO1+40), int(yo))) 
            pygame.display.update() 


if __name__ == "__main__":
    main()