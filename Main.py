import pygame

pygame.init() #Starting PyGame

#Windows settings
WIDTH, HEIGHT = 640, 480
background_color = (255,255,255)

window = pygame.display.set_mode([WIDTH, HEIGHT]) #Set window size
pygame.display.set_caption("Snake Game") #Set window title

while True:
    for event in pygame.event.get(): #Get PyGame events
        if event.type == pygame.QUIT:
            quit()

    window.fill(background_color) #Painting background color

    pygame.display.update() #Updating screen
