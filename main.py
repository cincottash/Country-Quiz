from answerKey import *
from setup import *
import time

def clearText():
	pygame.draw.rect(canvas, (182, 220, 243), (850, 919, 900, 30))

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

	for country in worldCountriesShuffled:
		
		displayText("Click on {}".format(country))

		validInput = False
		numAttempts = 0
		while(validInput == False):
			#run until pressed skip or guessed the correct country
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP:
					#getting pos of the mouse when its clicked
					pos = pygame.mouse.get_pos()
					selectedCountryColor = canvas.get_at(pos)
					
					#First check if we pressed the skip button
					if(selectedCountryColor == colors["SKIP"]):
						displayText("skipping...")
						validInput = True
						correctCountryColor = key[country]
						revealCountry(correctCountryColor, colors["BLACK"])
					elif(selectedCountryColor == colors["EXIT"]):
						displayText("quitting...")
						exit(0)
					elif(selectedCountryColor == colors["RETRY"]):
						main()
					else:

						if(selectedCountryColor == key[country]):
							displayText("Correct!")
							validInput = True
							if(numAttempts == 0):
								revealCountry(selectedCountryColor, colors["GREEN"])
							elif(numAttempts == 1):
								revealCountry(selectedCountryColor, colors["YELLOW"])
							else:
								revealCountry(selectedCountryColor, colors["RED"])
						else:
							for possibleCountry in worldCountries:
								if(key[possibleCountry] == selectedCountryColor):
									displayText("That's {}, try again, click on {}".format(possibleCountry, country))
							numAttempts += 1
	exit(0)

def main():
	gameLoop()

if __name__ == '__main__':
	main()