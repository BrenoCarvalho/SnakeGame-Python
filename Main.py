import pygame, random

pygame.init() #Starting PyGame

#Game settings
size = [640, 480]
background_color = (255,255,255)
FPS = 20
game_loop = True

window = pygame.display.set_mode(size) #Set window size
pygame.display.set_caption("Snake Game") #Set window title

#Snake
snakeSize = 10
snakeColor = (0,0,0) #Black
#0 = UP
#1 = DOWN
#2 = LEFT
#3 = RIGHT
snakeDir = None #Dir = direction
snakeBodySize = 2
snakeBody = [[size[0] / 2, size[1] / 2]]

#Apple
appleSize = 10
appleColor = (255,0,0)
applePos = [] #Pos = position

#Score
score = 0
font = pygame.font.Font(pygame.font.get_default_font(), 24)
text = font.render("Score: " + str(score), True, (0,0,0))

#Generate a random number
def randomApplePos():
    a = random.randint(0, 63)
    b = random.randint(0, 47)

    return [a * 10, b * 10]

applePos = randomApplePos()

def snakeMovimentation():
    if snakeDir == 0:
        snakeBody[0][1] -= 10
    elif snakeDir == 1:
        snakeBody[0][1] += 10
    elif snakeDir == 2:
        snakeBody[0][0] -= 10
    elif snakeDir == 3:
        snakeBody[0][0] += 10

#Looping of game
while game_loop:
    for event in pygame.event.get(): #Get PyGame events
        if event.type == pygame.QUIT:
            game_loop = False
        
        #Get keyboard events and set the direction of the snake
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

    window.blit(text, text.get_rect()) #Add score on the screen

    #Increasing the size of the snake
    if len(snakeBody) < snakeBodySize:
        snakeBody.append(snakeBody[-1])

    #Draws the whole body of the snake
    for bodyPart in snakeBody:
        pygame.draw.rect(window, snakeColor, [bodyPart[0], bodyPart[1], snakeSize, snakeSize]) #Drawing square (snake) in the screen

    snakeMovimentation()

    #Snake body movement
    for i in range(len(snakeBody) - 1, 0, -1):
        snakeBody[i] = (snakeBody[i-1][0], snakeBody[i-1][1])

    #Apple
    pygame.draw.rect(window, appleColor, [applePos[0], applePos[1], appleSize, appleSize]) #Drawing square (apple) in the screen
    
    #Collision
    if (snakeBody[0][0] == applePos[0] and snakeBody[0][1] == applePos[1]):
        snakeBodySize += 1
        score += 1
        text = font.render("Score: " + str(score), True, (0,0,0))
        FPS += 1
        applePos = randomApplePos()

    #If the snake leaves the screen, it shows on the other side
    if snakeBody[0][0] > 640:
        snakeBody[0][0] = -10
    elif snakeBody[0][0] < 0:
        snakeBody[0][0] = 640
    elif snakeBody[0][1] > 480:
        snakeBody[0][1] = -10
    elif snakeBody[0][1] < 0:
        snakeBody[0][1] = 480

    #Collision with one's own body
    for bodyPart in snakeBody[2:]:
        if snakeBody[0][0] == bodyPart[0] and snakeBody[0][1] == bodyPart[1]:
            game_loop = False

    pygame.time.Clock().tick(FPS) #Set FPS
    pygame.display.update() #Updating screen

pygame.quit()
quit()
