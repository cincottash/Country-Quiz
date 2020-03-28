import pygame
from globals import *
from answerKey import *
from countries import *
import time
import random

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
	time.sleep(0.25)

def revealCountry(countryColor, newColor):
	for x in range(canvasWidth):
		for y in range(canvasHeight):
			pixelColor = canvas.get_at((x, y))
			if((pixelColor[0] == countryColor[0]) and (pixelColor[1] == countryColor[1]) and pixelColor[2] == countryColor[2]):
				canvas.set_at((x, y), newColor)

def gameLoop():
	canvas.blit(background, (0,0))
	#skip button
	pygame.draw.rect(canvas, colors["RED"],(895,919,50,60))
	myfont = pygame.font.SysFont('Comic Sans MS', 30)
	textsurface = myfont.render("Skip", False, colors["BLACK"])
	canvas.blit(textsurface, (899, 953))
	pygame.display.update()
	
	worldCountriesShuffled = random.sample(worldCountries, len(worldCountries))

	for i,country in enumerate(worldCountriesShuffled):
		
		displayText("Click on {}".format(worldCountriesShuffled[i]))

		validInput = False
		numAttempts = 0
		while(validInput == False):
			#run until pressed skip or guessed the correct country
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP:
					#getting pos of the mouse when its clicked
					pos = pygame.mouse.get_pos()
					#print(pos)
					
					#First check if we pressed the skip button
					if((895 < pos[0] < 944) and (949 < pos[1] < 978)):
						displayText("skipping...")
						validInput = True
						countryColor = key[country]
						revealCountry(countryColor, colors["BLACK"])
					else:
						#find the pixel color value at that location
						countryColor = canvas.get_at(pos)
						#print(color)

						if(countryColor == key[country]):
							displayText("Correct!")
							validInput = True
							if(numAttempts == 0):
								revealCountry(countryColor, colors["GREEN"])
							elif(numAttempts == 1):
								revealCountry(countryColor, colors["YELLOW"])
							else:
								revealCountry(countryColor, colors["RED"])
						else:
							for country in worldCountries:
								if key[country] == countryColor:
									displayText("That's {},  try again, click on {}".format((country), worldCountriesShuffled[i]))
							numAttempts += 1
	exit(0)

def main():
	gameLoop()

if __name__ == '__main__':
	main()