import pygame
from globals import *
from answerKey import *
from countries import *
import time

pygame.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

#used to reset the screen after each update
background = pygame.image.load("assets/world.png")

canvas = pygame.display.set_mode((canvasWidth, canvasHeight))

def clearText():
	pygame.draw.rect(canvas, (182, 220, 243), (850, 919, 600, 30))

def displayText(text):
	clearText()
	myfont = pygame.font.SysFont('Comic Sans MS', 30)
	textsurface = myfont.render(text, False, colors["BLACK"])
	canvas.blit(textsurface, textPos)
	pygame.display.update()
	time.sleep(1)

def gameLoop():
	canvas.blit(background, (0,0))
	#skip button
	pygame.draw.rect(canvas, colors["RED"],(895,919,50,60))
	myfont = pygame.font.SysFont('Comic Sans MS', 30)
	textsurface = myfont.render("Skip", False, colors["BLACK"])
	canvas.blit(textsurface, (899, 953))
	pygame.display.update()
	


	for i,country in enumerate(worldCountries):
		
		displayText("Click on {}".format(worldCountries[i]))

		validInput = False
		while(validInput == False):
			#run until pressed skip or guessed the correct country
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP:
					#getting pos of the mouse when its clicked
					pos = pygame.mouse.get_pos()
					#print(pos)
					
					#First check if we pressed the skip button
					if((895 < pos[0] < 944) and (949 < pos[1] < 978)):
						displayText("pressed skip")
						#validInput = True
						validInput = True
					else:
						#find the pixel color value at that location
						color = canvas.get_at(pos)
						#print(color)

						if(color == key[country]):
							displayText("Correct!")
							validInput = True
						else:
							displayText("Wrong!")
							displayText("Try again, click on {}".format(worldCountries[i]))
	exit(0)

def main():
	gameLoop()

if __name__ == '__main__':
	main()