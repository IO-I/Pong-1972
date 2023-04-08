import pygame
WIDTH = 700
HEIGHT = 550
ballW = 30
ballH = 30
black = (0,0,0)
white = (255,255,255)
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Data's Pong at {FPS} fps")
pygame.init()
clock = pygame.time.Clock()
running = True
ballXStart = int(WIDTH/2)
ballYStart = int(HEIGHT/2)
ballSpeed = -2
score = [0,0]
winner = 0
state = 0
startSquareW = 10
pongSquareW = 15
GameGoing = True
diff = 0

zero = [[1,1,1,1],
        [1,0,0,1],
        [1,0,0,1],
        [1,0,0,1],
        [1,0,0,1],
        [1,0,0,1],
        [1,1,1,1]]

one = [[0,0,0,1],
       [0,0,0,1],
       [0,0,0,1],
       [0,0,0,1],
       [0,0,0,1],
       [0,0,0,1],
       [0,0,0,1]]

two = [[1,1,1,1],
       [0,0,0,1],
       [0,0,0,1],
       [1,1,1,1],
       [1,0,0,0],
       [1,0,0,0],
       [1,1,1,1]]

three = [[1,1,1,1],
         [0,0,0,1],
         [0,0,0,1],
         [0,1,1,1],
         [0,0,0,1],
         [0,0,0,1],
         [1,1,1,1]]

four = [[1,0,0,1],
        [1,0,0,1],
        [1,0,0,1],
        [1,1,1,1],
        [0,0,0,1],
        [0,0,0,1],
        [0,0,0,1]]

five = [[1,1,1,1],
        [1,0,0,0],
        [1,0,0,0],
        [1,1,1,1],
        [0,0,0,1],
        [0,0,0,1],
        [1,1,1,1]]

six = [[1,1,1,1],
       [1,0,0,0],
       [1,0,0,0],
       [1,1,1,1],
       [1,0,0,1],
       [1,0,0,1],
       [1,1,1,1]]

seven = [[1,1,1,1],
         [0,0,0,1],
         [0,0,0,1],
         [0,0,0,1],
         [0,0,0,1],
         [0,0,0,1],
         [0,0,0,1]]

eight = [[1,1,1,1],
         [1,0,0,1],
         [1,0,0,1],
         [1,1,1,1],
         [1,0,0,1],
         [1,0,0,1],
         [1,1,1,1]]

nine = [[1,1,1,1],
        [1,0,0,1],
        [1,0,0,1],
        [1,1,1,1],
        [0,0,0,1],
        [0,0,0,1],
        [0,0,0,1]]

numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

pong = [[1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1],
        [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],
        [1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,0,1,0,0,0],
        [1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,1,1],
        [1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,1],
        [1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],
        [1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1]]

toStart = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0],
           [0,1,1,0,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1],
           [1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0],
           [1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,1,1,1,0,1,0,0,1,0],
           [1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0],
           [0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,0,1,1]]

toContinue = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0],
              [0,1,1,0,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1],
              [1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0],
              [1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,0,1,0,0,1,0],
              [1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0],
              [0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,0,1,1]]

won = [[1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1],
       [1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],
       [0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1],
       [0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,1],
       [0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1],
       [0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1],
       [0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,1]]

playerFig = [[1,1,1,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1],
             [1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1],
             [1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1],
             [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0],
             [1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
             [1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,0,1,0,0,1]]

computerFig = [[0,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1],
               [1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
               [1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
               [1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1],
               [1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0],
               [1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
               [0,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,0,1,0,0,1]]

diffMap = [[1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,1,1,1,0,1,1,0,1,1,1,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,1,0,1,0,0,1,0,0,1,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0]]

def screenLines():
    global HEIGHT
    global WIDTH
    global black
    global running
    lineH = 1
    for i in range(int(HEIGHT/lineH)):
        pygame.draw.rect(screen, black, pygame.Rect(0, i*2, WIDTH, lineH))

def displayScore(playerScore, computerScore):
    playerIndex = playerScore
    computerIndex = computerScore
    squareDia = 8
    compOffsetX = 550
    compOffsetY = 30
    playerOffsetX = 200
    playerOffsetY = 30
    global winner

    if computerScore <= 9:
        for j in range(len(numbers[computerIndex])):
            for i in range(len(numbers[computerIndex][j])):
                if numbers[computerIndex][j][i] == 1:
                    pygame.draw.rect(screen, white, pygame.Rect(i*squareDia+compOffsetX, j*squareDia+compOffsetY, squareDia, squareDia))
    elif computerScore > 9:
        for j in range(len(numbers[1])):
            for i in range(len(numbers[1][j])):
                if numbers[1][j][i] == 1:
                    pygame.draw.rect(screen, white, pygame.Rect(i*squareDia+compOffsetX-squareDia*6, j*squareDia+compOffsetY, squareDia, squareDia))
        for j in range(len(numbers[computerIndex%10])):
            for i in range(len(numbers[computerIndex%10][j])):
                if numbers[computerIndex%10][j][i] == 1:
                    pygame.draw.rect(screen, white, pygame.Rect(i*squareDia+compOffsetX, j*squareDia+compOffsetY, squareDia, squareDia))
    
    if playerScore <= 9:
        for j in range(len(numbers[playerIndex])):
            for i in range(len(numbers[playerIndex][j])):
                if numbers[playerIndex][j][i] == 1:
                    pygame.draw.rect(screen, white, pygame.Rect(i*squareDia+playerOffsetX, j*squareDia+playerOffsetY, squareDia, squareDia))
    elif playerScore > 9:
        for j in range(len(numbers[1])):
            for i in range(len(numbers[1][j])):
                if numbers[1][j][i] == 1:
                    pygame.draw.rect(screen, white, pygame.Rect(i*squareDia+playerOffsetX-squareDia*6, j*squareDia+compOffsetY, squareDia, squareDia))
        for j in range(len(numbers[playerIndex%10])):
            for i in range(len(numbers[playerIndex%10][j])):
                if numbers[playerIndex%10][j][i] == 1:
                    pygame.draw.rect(screen, white, pygame.Rect(i*squareDia+playerOffsetX, j*squareDia+compOffsetY, squareDia, squareDia))       

    if computerScore == 15:
        winner = "comp"
        return(True)
    if playerScore == 15:
        winner = "play"
        return(True)
    return(winner)

def drawMid():
    global WIDTH
    global white
    y = 8
    for i in range(22):
        pygame.draw.rect(screen, white, pygame.Rect(int(WIDTH/2)-2, y, 4, 9))
        y+=25

class Paddle:
    global HEIGHT
    global diff
    def __init__(self, x, y, w, h, type):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.type = type
    
    def move(self):
        global ballYStart
        if self.type == "player":
            mouseY = pygame.mouse.get_pos()[1] - player.h/2
            if mouseY <= 1:
                self.y = 1
                return(self.y)
            if mouseY >= HEIGHT-self.h:
                self.y = HEIGHT-self.h
                return(self.y)
            if mouseY < HEIGHT and mouseY > 0:
                self.y = mouseY
                return(self.y)
            
        if self.type == "computer":
            self.y = (ball.y - int(self.h/2)) * diff
            return(self.y)
            
    def draw(self):
        pygame.draw.rect(screen, white, pygame.Rect(self.x, self.y, self.w, self.h))

class Ball:
    def __init__(self, x, y, w, xspeed, yspeed):
        self.x = x
        self.y = y
        self.w = w
        self.xspeed = xspeed
        self.yspeed = yspeed
    
    def move(self):
        global WIDTH
        global HEIGHT
        global ballXStart
        global ballYStart
        global score
        global ballSpeed
        self.x += self.xspeed
        self.y += self.yspeed

        if self.y <= 0:
            self.yspeed *= -1

        if self.y >= HEIGHT - self.w:
            self.yspeed *= -1

        if self.x >= enemy.x + enemy.w/2:
            self.x = ballXStart
            self.y = ballYStart
            self.xspeed = ballSpeed
            self.yspeed = ballSpeed
            score[0]+=1
        if self.x <= player.x - player.w/2:
            self.x = ballXStart
            self.y = ballYStart
            self.xspeed = ballSpeed
            self.yspeed = ballSpeed
            score[1]+=1
        if self.x <= player.x + player.w and self.y <= player.y + player.h and self.y >= player.y:
            self.xspeed *= 1.07
            self.yspeed *= 1.07
            self.x += 1
            self.xspeed *= -1

        if self.x >= enemy.x - enemy.w and self.y <= enemy.y + enemy.h and self.y >= enemy.y:
            self.xspeed *= 1.07
            self.yspeed *= 1.07
            self.xspeed *= -1
        
        return(self.x, self.y, score)

    def draw(self):
        pygame.draw.rect(screen, white, pygame.Rect(self.x, self.y, self.w, self.w))

player = Paddle(10, int(HEIGHT/2), 10, 50, "player")
enemy = Paddle(WIDTH-20, int(HEIGHT/2), 10, 50, "computer")
ball = Ball(int(WIDTH/2), int(HEIGHT/2), 10, ballSpeed, -ballSpeed)

def renderText(array, xFactor, yFactor, w, h):
    for j in range(len(array)):
        for i in range(len(array[j])):
            if array[j][i] == 1:
                pygame.draw.rect(screen, white, pygame.Rect(i*w+xFactor, j*h+yFactor, w, h))

while GameGoing:
    if state == 0:
        inMenu = True
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    inMenu = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inMenu = False
                        endScreen = False
                        state = 1
                    if event.key == pygame.K_1:
                        diff = 0.94
                    if event.key == pygame.K_2:
                        diff = 0.97
                    if event.key == pygame.K_3:
                        diff = 0.99 
                    if diff == 0:
                        diff = 0.96
                                   
        screen.fill(black)
        renderText(pong, pongSquareW+((WIDTH/2)-len(pong*pongSquareW)*1.55), pongSquareW+(HEIGHT/2)/3, pongSquareW, pongSquareW)
        renderText(toStart, startSquareW+((WIDTH/2)-len(toStart*startSquareW)*3.4), startSquareW+(HEIGHT/2), startSquareW, startSquareW)
        renderText(diffMap, startSquareW/2+((WIDTH/2)+130), startSquareW/2+(HEIGHT/1.45), startSquareW/2, startSquareW/2)
        screenLines()
        pygame.display.flip()

    if state == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        state = 0
                        
            screen.fill(black)
            drawMid()
            ball.move()
            ball.draw()
            player.move()
            player.draw()
            enemy.move()
            enemy.draw()
            displayScore(score[0], score[1])
            if displayScore(score[0], score[1]) == True:
                running = False
                state = 2
                endScreen = True
            screenLines()
            clock.tick(FPS)
            pygame.display.flip()

    if state == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    endScreen = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        endScreen = False
                        running = True
                        state = 1
                        score = [0,0]
                        break
                  
            screen.fill(black)
            renderText(won, startSquareW+((WIDTH/2)-len(won*startSquareW)*1.5), startSquareW+(HEIGHT/2), startSquareW, startSquareW)
            if winner == "comp":
                renderText(computerFig, startSquareW+((WIDTH/2)-len(computerFig*startSquareW)*3.4), startSquareW+(HEIGHT/4), startSquareW, startSquareW)
            if winner == "player":
                renderText(playerFig, startSquareW+((WIDTH/2)-len(playerFig*startSquareW)*3), startSquareW+(HEIGHT/4), startSquareW, startSquareW)
            renderText(toContinue, startSquareW+((WIDTH/2)-len(toContinue*startSquareW)*4.3), startSquareW+(HEIGHT/1.3), startSquareW, startSquareW)
            screenLines()
            pygame.display.flip()
pygame.quit()
