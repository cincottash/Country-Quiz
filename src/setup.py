from globals import *
from countries import *
import pygame
import random

def setup():
	worldCountriesShuffled = random.sample(worldCountries, len(worldCountries))
	#used to reset the screen after each update
	background = pygame.image.load("world.png")

	canvas = pygame.display.set_mode((canvasWidth, canvasHeight))

	pygame.init()
	canvas.blit(background, (0,0))

	#skip button
	pygame.draw.rect(canvas, colors["SKIP"],(850,919,50,60))

	myfont = pygame.font.SysFont('Comic Sans MS', 24)
	textsurface = myfont.render("Skip", False, colors["TEXTCOLORSKIP"])

	canvas.blit(textsurface, (859, 955))

	#Exit button
	pygame.draw.rect(canvas, colors["EXIT"],(910,919,50,60))

	myfont = pygame.font.SysFont('Comic Sans MS', 24)
	textsurface = myfont.render("Exit", False, colors["TEXTCOLOREXIT"])

	canvas.blit(textsurface, (920, 955))

	#Replay button
	pygame.draw.rect(canvas, colors["RETRY"],(970,919,50,60))

	myfont = pygame.font.SysFont('Comic Sans MS', 24)
	textsurface = myfont.render("Retry", False, colors["TEXTCOLORRETRY"])

	canvas.blit(textsurface, (973, 955))

	pygame.display.update()

	return worldCountriesShuffled, canvas

