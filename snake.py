


import pygame

import random

import time


def draw_apple(apple_X,apple_Y):
    pygame.draw.rect(display, apple_color, pygame.Rect(apple_X, apple_Y,10,10))
def generate_apple():
    apple_X= random.randint(1,180) * 10
    apple_Y= random.randint(1,90) * 10
    return apple_X, apple_Y
def collision_with_apple(snake_head, apple_X, apple_Y, grow):
    if snake_head[0] == apple_X and snake_head[1] == apple_Y:
        apple_X, apple_Y = generate_apple()
        grow = True
        pygame.display.set_caption("Slug Game")
    return apple_X, apple_Y, grow
def collision_with_boundaries(snake_head):

   
    if snake_head[0] >=display_width or snake_head[0] < 0 or snake_head[1] >=display_height or snake_head[1] < 0:
        return 1
    return 0
def collision_with_self(snake_head, snake_position):
    for position in snake_position[1:]:
        if snake_head[0] == position[0] and snake_head[1] == position [1]:
            return 1
    return 0


def generate_snake(snake_head, snake_position, button_direction, grow):

    
    if button_direction == 1:
        snake_head[0] += 10
    elif button_direction == 0:
        snake_head [0] -= 10
    elif button_direction == 2:
        snake_head [1] += 10    
    elif button_direction ==3:
        snake_head [1] -= 10
    snake_position.insert(0,list(snake_head))
    if grow != True:
        snake_position.pop()
    return snake_position

def display_snake(snake_position):

   
    for position in snake_position:
        pygame.draw.rect(display, player_color, pygame.Rect(position[0],position[1],10,10))

def play_game(snake_head, snake_position, button_direction):

    crashed = False
    grow = False
    apple_X, apple_Y = generate_apple()
    score = 0
    while crashed is not True:

        for event in pygame.event.get():

            
            if event.type == pygame.QUIT:
                crashed = True                                                      
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                button_direction = 0
            elif event.key == pygame.K_RIGHT:
                button_direction = 1
            elif event.key == pygame.K_UP:
                button_direction = 3
            elif event.key == pygame.K_DOWN:
                button_direction = 2        
        
        
        snake_position = generate_snake(snake_head, snake_position, button_direction, grow)
        grow = False

       
        display.fill(window_color)
        display_snake(snake_position)
        draw_apple(apple_X, apple_Y)
        pygame.display.update()
        apple_X, apple_Y, grow = collision_with_apple(snake_head, apple_X, apple_Y, grow)
       
       
        if collision_with_boundaries(snake_head) == 1:
            crashed = True
        if collision_with_self(snake_head, snake_position) == 1:
            crashed = True
        
        clock.tick(20)
        


if __name__ == "__main__":

   

    display_width = 1900

    display_height = 1000

    player_color = (168,153,255)

    window_color = (0,0,0)

    clock=pygame.time.Clock()
    
    apple_color = (241,3,3)
    

    

    snake_head = [250,250]

    snake_position = [[250,250],[240,250],[230,250],[220,250]]


     

    pygame.init()

    

   

    display = pygame.display.set_mode((display_width,display_height))

    display.fill(window_color)

    pygame.display.set_caption("Slug Game")

    pygame.display.update()

    

  

    play_game(snake_head, snake_position, 1)



    pygame.quit()