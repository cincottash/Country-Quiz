import pygame

pygame.init()
clock = pygame.time.Clock()

canvasWidth = 1920
canvasHeight = 1080

#used to reset the screen after each update
background = pygame.image.load("assets/world.png")

canvas = pygame.display.set_mode((canvasWidth, canvasHeight))

def update():
	canvas.blit(background, (0,0))
	pygame.display.update()

	#Checking if the mouse was pressed
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP:
			#getting pos of the mouse when its clicked
			pos = pygame.mouse.get_pos()
			#find the pixel color value at that location
			color = canvas.get_at(pos)
			print(color)
def main():
	while True:
		update()

if __name__ == '__main__':
	main()