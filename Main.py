import pygame, random

pygame.init() #Starting PyGame

#Game settings
size = [640, 480]
background_color = (255,255,255)
FPS = 15

window = pygame.display.set_mode(size) #Set window size
pygame.display.set_caption("Snake Game") #Set window title

#Snake
snakeSize = 10
snakeColor = (0,0,0) #Black
snakePos = [0, 0] #Pos = position
#0 = UP
#1 = DOWN
#2 = LEFT
#3 = RIGHT
snakeDir = 5 #Dir = direction
snakeBodySize = 2
snakeBody = []

#Apple
appleSize = 10
appleColor = (255,0,0)
applePos = [] #Pos = position

#Generate a random number
def randomApplePos():
    a = random.randint(0, 63)
    b = random.randint(0, 47)

    return [a * 10, b * 10]

applePos = randomApplePos()

def snakeMovimentation():
    if snakeDir == 0:
        snakePos[1] -= 10
    elif snakeDir == 1:
        snakePos[1] += 10
    elif snakeDir == 2:
        snakePos[0] -= 10
    elif snakeDir == 3:
        snakePos[0] += 10

#Looping of game
while True:
    for event in pygame.event.get(): #Get PyGame events
        if event.type == pygame.QUIT:
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snakeDir != 1:
                snakeDir = 0
            elif event.key == pygame.K_DOWN and snakeDir != 0:
                snakeDir = 1
            elif event.key == pygame.K_LEFT and snakeDir != 3:
                snakeDir = 2
            elif event.key == pygame.K_RIGHT and snakeDir != 2:
                snakeDir = 3

    window.fill(background_color) #Painting background color

    #Snake
    snakeBody.append([snakePos[0], snakePos[1]]) #Add the first square to the snake

    #Draws the whole body of the snake
    for i in range(len(snakeBody)):
        pygame.draw.rect(window, snakeColor, [snakeBody[i][0], snakeBody[i][1], snakeSize, snakeSize]) #Drawing square (snake) in the screen

    snakeMovimentation()
    snakeBody[-1][0] = snakePos[0] #Add movement (X) to the snake's head
    snakeBody[-1][1] = snakePos[1] #Add movement (Y) to the snake's head

    #Limits the snake to grow infinitely
    #Try removing this code snippet
    if len(snakeBody) > snakeBodySize:
        del snakeBody[0]

    #Apple
    pygame.draw.rect(window, appleColor, [applePos[0], applePos[1], appleSize, appleSize]) #Drawing square (apple) in the screen
    
    #Collision
    if (snakePos[0] == applePos[0] and snakePos[1] == applePos[1]):
        applePos = randomApplePos()
        snakeBodySize += 1        

    pygame.time.Clock().tick(FPS) #Set FPS
    pygame.display.update() #Updating screen
    