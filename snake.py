import pygame
import time
import random

#Define colours
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (105,105,105)

def main():

    #Initializes the imported pygame modules
    pygame.init()
    #Creates the display and updates the program
    display_width = 800
    display_height = 600
    display = pygame.display.set_mode((display_width, display_height))
    #Sets the title of the game
    pygame.display.set_caption('Snake Game')
    #Value to determine terminating conditions
    game_over = False
    #The starting values of the snake
    x = display_width/2
    y = display_height/2
    #The change of direction when an input is made
    x_change = 0
    y_change = 0
    #Clock variable
    clock = pygame.time.Clock()
    #Size of one snake block and snake speed
    snake_block = 10
    snake_speed = 25
    #Increasing snake size
    snake_List = []
    snake_length = 1
    #Generate Food
    foodx = int(round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0)
    foody = int(round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0)

    while not game_over:
        #Checking if the user exits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            #Determine the snake movement based on the input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block

        #Update the x and y values
        x += x_change
        y += y_change
        x = int(x)
        y = int(y)
        #Border collision ends the game
        if x >= (display_width - snake_block) or x < snake_block or y >= (display_height - snake_block) or y < snake_block:
            game_over = True
        #Ensures that each time the snake is redrawn and not elongated
        draw_screen(display, display_width, display_height)
        #Draws food location
        pygame.draw.rect(display, blue, [foodx, foody, snake_block, snake_block])
        #Snake head location
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)

        #If the snake moves but does not eat food, the snake will not get bigger
        if len(snake_List) > snake_length:
            del snake_List[0]

        #If you move backwards into yourself
        for coords in snake_List[:-1]:
            if coords == snake_Head:
                game_over = True

        draw_snake(display, snake_block, snake_List)
        draw_score(display, snake_length-1)

        #Create new food
        if x == foodx and y == foody:
            foodx = int(round(random.randrange(20, display_width - 2 * snake_block) / 10.0) * 10.0)
            foody = int(round(random.randrange(20, display_height - 2 * snake_block) / 10.0) * 10.0)
            snake_length += 1

        #Next Frame
        clock.tick(snake_speed)

    #Displays End Screen
    draw_endscreen(display, display_width, display_height, snake_length)

def draw_screen(display, width, height):

    block_size = 10
    display.fill(black)

    for border_block in range(0, width, block_size):
        pygame.draw.rect(display, grey, [border_block, 0, block_size, block_size])
        pygame.draw.rect(display, grey, [border_block, height - block_size, block_size, block_size])

    for border_block in range(0, height, block_size):
        pygame.draw.rect(display, grey, [0, border_block, block_size, block_size])
        pygame.draw.rect(display, grey, [width - block_size, border_block, block_size, block_size])

def draw_snake(display, snake_block, snake_list):
    for coords in snake_list:
        pygame.draw.rect(display, green, [coords[0], coords[1], snake_block, snake_block])

def draw_score(display, score):
    white = (255,255,255)
    score_font = pygame.font.SysFont("arialblack", 20)
    value = score_font.render("Your Score: " + str(score), True, white)
    display.blit(value, [10, 10])

    pygame.display.update()

def draw_endscreen(display, width, height, snake_length):
    display.fill((0, 0, 0))
    font_style = pygame.font.SysFont("arialblack", 25)
    end_msg = font_style.render("Game Over: Press C-Play Again or Q-Quit", True, white)
    display.blit(end_msg, [int(width / 8), int(height / 2)])
    draw_score(display, snake_length - 1)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                if event.type == pygame.QUIT or event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    main()

if __name__ == "__main__":
    main()
