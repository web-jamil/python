import random
import math
import pygame

#game setup
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animal Hangman!")

#variables used for the buttons
radius = 20
gapSize = 15

#colors
black = (89, 89, 89)
lightBlue = (199, 213, 224)
yellow = (254, 248, 220)

#list for the buttons used
letters = [] 
startX = round((WIDTH - (radius * 2 + gapSize) * 13) / 2)
startY = 400
#ascii letter value for capital A
A = 65
#loop used to maintain the buttons on the screen into rows
for i in range(26):
    #used to gather the two letter rows
    x = startX + gapSize * 2 + ((radius * 2 + gapSize) * (i % 13))
    y = startY + ((i // 13) * (gapSize + radius * 2))
    letters.append([x,y, chr(A + i), True])

#font used for game
lettersFont = pygame.font.SysFont('Helvetica', 30)

#hangman pictures used
images = []
#loop cycles through the images for each point in hangman based on pic name
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#stage in where the hangman is
hangmanLife = 0
#list of words
wordList = ["COW", "HORSE", "DOG", "HIPPO", "LEOPARD", "BEAR", "WHALE", "BUMBLEBEE", "CHIMPANZEE", "ELEPHANT", "FLAMINGO", "GREYHOUND", "HUMMINGBIRD", "KANGAROO", "LADYBUG", "MONKEY", "NARWHAL", "OCTOPUS", "PANTHER", "RACCOON", "RATTLESNAKE", "SALAMANDER", "ZEBRA"]
words = random.choice(wordList)
guess = []


FPS = 60
clock = pygame.time.Clock()
run = True

def drawings():
    #background color
    win.fill((lightBlue))

    #displaying the word onto the screen
    wordDisplayed = ""
    for letter in words:
        if letter in guess:
            wordDisplayed += letter + " "
        else:
            wordDisplayed += "_ "
    text = lettersFont.render(wordDisplayed, 1, black)
    win.blit(text, (400, 200))



    #button colors
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, black, (x, y), radius, 3)
            text = lettersFont.render(ltr, 1, black)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
        
    #location of hangman image
    win.blit(images[hangmanLife], (100, 100))
    pygame.display.update()

while run:
    clock.tick(FPS)

    drawings()
    
    #this event is used to close the application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    #taking in position of the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            #tracking mouse input for the button clicks
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                #distance between mouse positions
                    distance = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    #removal of the button after selection
                    if distance < radius:
                        letter[3] = False
                        #display words onto screen if in word
                        guess.append(ltr)
                        #adding limbs onto hangman figure if incorrect
                        if ltr not in words:
                            hangmanLife += 1
    #if the user guesses correctly or not
    wins = True
    for letter in words:
        if letter not in guess:
            wins = False
            break

    if wins:
        win.fill(lightBlue)
        text = lettersFont.render("You guessed correctly!", 1, yellow)
        #display in the middle of the screen
        win.blit(text, (WIDTH/2 - text.get_width()/ 2, HEIGHT / 2 - text.get_height()/ 2))
        pygame.display.update()
        pygame.time.delay(5000)
        break

    if hangmanLife == 6:
        win.fill(lightBlue)
        text = lettersFont.render("You did not guess correctly.", 1, yellow)
        #display in the middle of the screen
        win.blit(text, (WIDTH/2 - text.get_width()/ 2, HEIGHT / 2 - text.get_height()/ 2))
        pygame.display.update()
        pygame.time.delay(5000)
        break


pygame.quit
