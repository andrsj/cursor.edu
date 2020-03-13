import pygame

pygame.init()

XY = 500
border = 5
win = pygame.display.set_mode((XY,XY))

pygame.display.set_caption("Cude")

x,y,width,height,speed = (50,400,20,20,5)
# delay = 50
clock = pygame.time.Clock()
tick = 60
run = True

win.fill((255,255,255))

jump = False
jumpCount = 10 

while run:
	# pygame.time.delay(delay)
	clock.tick(tick)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x > 0 + border:
		x -= speed
	if keys[pygame.K_RIGHT] and x < XY - border - width:
		x += speed
	if not(jump):
		# if keys[pygame.K_UP] and y > 0 + border:
		# 	y -= speed
		# if keys[pygame.K_DOWN] and y < XY - border - height:
		# 	y += speed
		if keys[pygame.K_SPACE]:
			jump = True
	else:
		if jumpCount >= -10:
			if jumpCount < 0:
				y += (jumpCount ** 2) / 2
				jumpCount -= 1
			else:
				y -= (jumpCount ** 2) / 2
				jumpCount -= 1
		else:
			jump = False
			jumpCount = 10

	win.fill((255,255,255))
	pygame.draw.rect(win, (127,127,127), (x,y,width,height))
	pygame.display.update() 



	if keys[pygame.K_ESCAPE]:
		pygame.quit()
		run = False

pygame.quit()	