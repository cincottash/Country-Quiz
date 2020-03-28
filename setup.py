from globals import *
from countries import *
import pygame
import random

worldCountriesShuffled = random.sample(worldCountries, len(worldCountries))


#used to reset the screen after each update
background = pygame.image.load("assets/world.png")

canvas = pygame.display.set_mode((canvasWidth, canvasHeight))

pygame.init()
canvas.blit(background, (0,0))
#skip button
pygame.draw.rect(canvas, colors["RED"],(895,919,50,60))
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render("Skip", False, colors["BLACK"])
canvas.blit(textsurface, (899, 953))
pygame.display.update()

