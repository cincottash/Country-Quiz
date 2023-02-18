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
			if(pixelColor[0] == countryColor[0] and pixelColor[1] == countryColor[1] and pixelColor[2] == countryColor[2]):
				canvas.set_at((x, y), newColor)

def gameLoop(worldCountriesShuffled, canvas):

	numCorrect = 0

	for country in worldCountriesShuffled:
		
		displayText(f"Click on {country}", colors["BLACK"], canvas)

		validInput = False
		numAttempts = 0
		while(validInput == False):
			#run until pressed skip or guessed the correct country
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP:
					#getting pos of the mouse when its clicked
					pos = pygame.mouse.get_pos()
					selectedColor = canvas.get_at(pos)
					
					#First check if we pressed the skip button
					if((selectedColor == colors["SKIP"]) or (selectedColor == colors["TEXTCOLORSKIP"])):
						displayText("Skipping...", colors["BLACK"], canvas)
						validInput = True
						correctCountryColor = key[country]
						revealCountry(correctCountryColor, colors["BLACK"], canvas)
					elif((selectedColor == colors["EXIT"]) or (selectedColor == colors["TEXTCOLOREXIT"])):
						displayText("Quitting...", colors["BLACK"], canvas)
						exit(0)
					elif(selectedColor == colors["RETRY"] or (selectedColor == colors["TEXTCOLORRETRY"])):
						main()
					else:

						if(selectedColor == key[country]):
							displayText("Correct!", colors["BLACK"], canvas)
							validInput = True
							if(numAttempts == 0):
								revealCountry(selectedColor, colors["GREEN"], canvas)
								numCorrect += 1
							elif(numAttempts == 1):
								revealCountry(selectedColor, colors["YELLOW"], canvas)
							else:
								revealCountry(selectedColor, colors["RED"], canvas)
						else:
							for possibleCountry in worldCountries:
								if(key[possibleCountry] == selectedColor):
									displayText(f"That's {possibleCountry}, try again, click on {country}", colors["BLACK"], canvas)
							if((selectedColor == colors["RED"]) or selectedColor == colors["GREEN"] or selectedColor == colors["YELLOW"]):
								displayText(f"You already clicked that country, try again, click on {country}", colors["BLACK"], canvas)
							numAttempts += 1
	displayText(f"Game over!! You got {numCorrect}/{len(worldCountries)} correct on the first try", colors["BLACK"], canvas)
	
	
	while(True):
		for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP:
					#getting pos of the mouse when its clicked
					pos = pygame.mouse.get_pos()
					selectedColor = canvas.get_at(pos)

					if((selectedColor == colors["EXIT"]) or (selectedColor == colors["TEXTCOLOREXIT"])):
						displayText("quitting...", colors["BLACK"], canvas)
						exit(0)
					elif(selectedColor == colors["RETRY"] or (selectedColor == colors["TEXTCOLORRETRY"])):
						main()

def main():
	worldCountriesShuffled, canvas = setup()
	gameLoop(worldCountriesShuffled, canvas)

if __name__ == '__main__':
	main()