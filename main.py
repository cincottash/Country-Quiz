from answerKey import *
from setup import *
import time

def clearText(canvas):
	pygame.draw.rect(canvas, (182, 220, 243), (850, 919, 900, 30))

def displayText(text, color, canvas):
	clearText(canvas)
	myfont = pygame.font.SysFont('Comic Sans MS', 30)
	textsurface = myfont.render(text, False, color)
	canvas.blit(textsurface, textPos)
	pygame.display.update()
	time.sleep(0.25)

def revealCountry(countryColor, newColor, canvas):
	for x in range(canvasWidth):
		for y in range(canvasHeight):
			pixelColor = canvas.get_at((x, y))
			if((pixelColor[0] == countryColor[0]) and (pixelColor[1] == countryColor[1]) and pixelColor[2] == countryColor[2]):
				canvas.set_at((x, y), newColor)

def gameLoop(worldCountriesShuffled, canvas):

	numCorrect = 0

	for country in worldCountriesShuffled:
		
		displayText("Click on {}".format(country), colors["BLACK"], canvas)

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
					if((selectedCountryColor == colors["SKIP"]) or (selectedCountryColor == colors["TEXTCOLORSKIP"])):
						displayText("skipping...", colors["BLACK"], canvas)
						validInput = True
						correctCountryColor = key[country]
						revealCountry(correctCountryColor, colors["BLACK"], canvas)
					elif((selectedCountryColor == colors["EXIT"]) or (selectedCountryColor == colors["TEXTCOLOREXIT"])):
						displayText("Quitting...", colors["BLACK"], canvas)
						exit(0)
					elif(selectedCountryColor == colors["RETRY"] or (selectedCountryColor == colors["TEXTCOLORRETRY"])):
						main()
					else:

						if(selectedCountryColor == key[country]):
							displayText("Correct!", colors["BLACK"], canvas)
							validInput = True
							if(numAttempts == 0):
								revealCountry(selectedCountryColor, colors["GREEN"], canvas)
								numCorrect += 1
							elif(numAttempts == 1):
								revealCountry(selectedCountryColor, colors["YELLOW"], canvas)
							else:
								revealCountry(selectedCountryColor, colors["RED"], canvas)
						else:
							for possibleCountry in worldCountries:
								if(key[possibleCountry] == selectedCountryColor):
									displayText("That's {}, try again, click on {}".format(possibleCountry, country), colors["BLACK"], canvas)
							if((selectedCountryColor == colors["RED"]) or (selectedCountryColor == colors["GREEN"]) or (selectedCountryColor == colors["YELLOW"])):
								displayText("You already clicked that country, try again, click on {}".format(country), colors["BLACK"], canvas)
							numAttempts += 1
	displayText("Game over!! You got {}/{} correct on the first try".format(numCorrect, len(worldCountries)), colors["BLACK"], canvas)
	
	validInput = False
	while(validInput == False):
		for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP:
					#getting pos of the mouse when its clicked
					pos = pygame.mouse.get_pos()
					selectedCountryColor = canvas.get_at(pos)

					if((selectedCountryColor == colors["EXIT"]) or (selectedCountryColor == colors["TEXTCOLOREXIT"])):
						displayText("quitting...", colors["BLACK"], canvas)
						exit(0)
					elif(selectedCountryColor == colors["RETRY"] or (selectedCountryColor == colors["TEXTCOLORRETRY"])):
						main()

def main():
	worldCountriesShuffled, canvas = setup()
	gameLoop(worldCountriesShuffled, canvas)

if __name__ == '__main__':
	main()