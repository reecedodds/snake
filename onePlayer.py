import pygame
import random
import settings
import messages
import snakeProperties

pygame.init()

# Creates the one player main display
display = pygame.display.set_mode((settings.display_width, settings.display_height))

clock = pygame.time.Clock()

def game_loop():
    """Loop that will take place until the game is over."""
    # To determine if the game is over and if it should close
    game_over = False
    game_close = False

    # Starting point of the X and Y coord's
    x1 = settings.display_width / 2
    y1 = settings.display_height / 2

    x1_change = 0
    y1_change = 0

    # Every coord in the snake and the length
    snake_list = []
    snake_length = 1

    # Creating food diameters
    foodx = round(random.randrange(0, settings.display_width - snakeProperties.snake_block) / 10) * 10
    foody = round(random.randrange(0, settings.display_height - snakeProperties.snake_block) / 10) * 10

    while not game_over:
        while game_close:
            # Setting the game over screen
            display.fill(settings.black)
            messages.message(display, "You lost! Press Q to Quit or C to play again", settings.white, 100)
            pygame.display.update()

            # Determine if the user wants to play again or close the application
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        settings.snake_speed = 15
                        game_loop()

        # Detecting input from the user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10

        # Determine if the user has left the screen
        if x1 >= settings.display_width or x1 < 0 or y1 >= settings.display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        display.fill(settings.black)

        # Drawing food
        pygame.draw.rect(display, settings.yellow, [foodx, foody, snakeProperties.snake_block, snakeProperties.snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        #Displaying current score
        snakeProperties.current_snake(display, settings.green, snakeProperties.snake_block, snake_list)
        messages.current_score(display, snake_length - 1, 0)

        pygame.display.update()

        # Determine if the food has been eaten
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, settings.display_width - snakeProperties.snake_block) / 10) * 10
            foody = round(random.randrange(0, settings.display_height - snakeProperties.snake_block) / 10) * 10
            snake_length += 1
            snakeProperties.snake_speed += 1

        clock.tick(snakeProperties.snake_speed)

    pygame.quit()
    quit()



