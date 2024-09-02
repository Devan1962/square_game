import pygame
import sys
import random
import time
# Initialize Pygame
pygame.init()
square_x = random.randint(0,820)
square_y = random.randint(10,560)
class EdibleSquare:
    def __init__(self, max_x,max_y, poisonous):
        self.is_eaten = False
        self.x = random.randint(0,max_x)
        self.y = random.randint(0,max_y)
        self.poisonous = poisonous
    def draw(self, screen):
        if self.poisonous:
            draw_colour = (128,0,128)
        else:
            draw_colour = green
        pygame.draw.rect(screen, draw_colour, (self.x,self.y,10,10))
    def check_if_eaten(self, moving_rectangle ):
        x = moving_rectangle[0]
        y = moving_rectangle[1]
        rect_width = moving_rectangle[2]
        rect_height = moving_rectangle[3]
        if self.x >= x and self.x <x +rect_width:
            if self.y >= y and self.y<y+rect_height:
                self.is_eaten = True

        


width, height = 840, 580
squares = []


colours = []
# Set up the display


pygame.display.set_caption('Rectangle game')



# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0,255,0)
# Set up the rectangle
rect_width, rect_height = 60, 40
speed = 2
# Main game loop
running = True
rect_x = 0
rect_y = 0
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)

surface = pygame.display.get_surface()
width, height = surface.get_width(), surface.get_height()
for i in range(10):
    squares.append(EdibleSquare(max_x= width,max_y=height, poisonous=True))
    squares.append(EdibleSquare(max_x= width,max_y=height,poisonous=False))
    squares.append(EdibleSquare(max_x= width,max_y=height,poisonous=False))
    squares.append(EdibleSquare(max_x= width,max_y=height,poisonous=False))
clock = pygame.time.Clock()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("keypressed")
        white = (0,255,255)
    if keys[pygame.K_m]:
        print("Key pressed")
        black = (255,0,0)
    if keys[pygame.K_s]:
        rect_y += speed
    if keys[pygame.K_d]:
        rect_x += speed
    if keys[pygame.K_w]:
        rect_y -= speed
    if keys[pygame.K_a]:
        rect_x -= speed
    if keys[pygame.K_k]:
        rect_height -= 1
        rect_width -= 1
    if keys[pygame.K_1]:
        speed += 0.1
    if keys[pygame.K_2]:
        speed -= 0.1
    if keys[pygame.K_ESCAPE]:
        pygame.display.quit()
        pygame.quit()
        sys.exit()
    if rect_width == 0:
        rect_x = mouse_x
        rect_y = mouse_y
    if rect_y <0:
        rect_y = 0
    if rect_y > height-rect_height:
        rect_y = height-rect_height
    if rect_x <0:
        rect_x = 0
    if rect_x > width-rect_width :
        rect_x = width-rect_width


    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()


    # Clear the screen
    screen.fill(black)

    # Draw the rectangle
    pygame.draw.rect(screen, white, (rect_x, rect_y, rect_width, rect_height))
    # Draw the squares
    not_eaten = []
    for square in squares:
        square.check_if_eaten((rect_x, rect_y, rect_width, rect_height))
        if square.is_eaten and square.poisonous == False:
            rect_height += 3
            rect_width += 3
        elif square.is_eaten and square.poisonous == True:
            rect_height /= 1.5
            rect_width /= 1.5
        else:
            square.draw(screen)
            not_eaten.append(square)

    squares = not_eaten
    new_squares = random.randint(1,100)>99
    new_square_edible = random.randint(1,100)>25

    if new_squares == True:
        squares.append(EdibleSquare(max_x= width,max_y=height,poisonous=not new_square_edible))

   
    if rect_height > 150 and rect_width > 225:
        pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
        my_font = pygame.font.SysFont('Comic Sans MS', 100)
        text_surface = my_font.render(' You win press down arrow to play again', False, (0, 255, 0))
        screen.blit(text_surface, (40,250)) 
        pygame.display.flip()
        running = False
        while not running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = True



    elif rect_height<20 and rect_width<30:
        pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
        my_font = pygame.font.SysFont('Comic Sans MS', 100)
        text_surface = my_font.render(' You lose press down arrow to play again', False, (255, 0, 0))
        screen.blit(text_surface, (40,250)) 
        pygame.display.flip()


    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

        
# Quit Pygame
pygame.quit()
sys.exit()

