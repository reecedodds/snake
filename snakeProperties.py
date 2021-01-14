import pygame

pygame.init()


# Current size of the snake
def current_snake(display, color, snake_block, snake_list):
    """Draws the current snake"""
    for x in snake_list:
        pygame.draw.rect(display, color, [x[0], x[1], snake_block, snake_block])


# Snake attributes
snake_speed = 15
snake2_speed = 15
snake_block = 10
snake2_block = 10
