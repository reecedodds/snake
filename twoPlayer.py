import pygame
import random
import settings
import messages
import snakeProperties

pygame.init()

# Initialize the display for two player
display = pygame.display.set_mode((settings.display_width, settings.display_height))

clock = pygame.time.Clock()


def two_Player_Loop():
    """Create the loop for the two player game, will run until both players are dead."""
    # Knowing when the game is over and should close
    game_over = False
    game_close = False

    #Knowing when either players have died
    snake1Dead = False
    snake2Dead = False

    #Starting points for both players
    x1 = settings.display_width / 2 - 10
    y1 = settings.display_height / 2
    x2 = settings.display_width / 2 + 10
    y2 = settings.display_height / 2

    x1_change = 0
    y1_change = 0
    x2_change = 0
    y2_change = 0

    snake_list = []
    snake2_list = []
    snake_length = 1
    snake2_length = 1
    snakeProperties.snake_speed = 30
    snakeProperties.snake2_speed = 30

    # Creating the food diameters
    foodx = round(random.randrange(0, settings.display_width - snakeProperties.snake_block) / 10) * 10
    foody = round(random.randrange(0, settings.display_height - snakeProperties.snake_block) / 10) * 10
    food2x = round(random.randrange(0, settings.display_width - snakeProperties.snake_block) / 10) * 10
    food2y = round(random.randrange(0, settings.display_height - snakeProperties.snake_block) / 10) * 10

    winner = False

    while not game_over:
        # Will run until the game should close, when the winner will be announced
        while game_close:
            display.fill(settings.black)
            messages.message(display, "You lost! Press Q to Quit or C to play again", settings.white, 200)
            if winner == True:
                messages.message(display, "Player 1 is WINNER!", settings.white, 50)
            else:
                messages.message(display, "Player 2 is WINNER!", settings.white, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        snakeProperties.snake_speed = 15
                        snakeProperties.snake2_speed = 15
                        two_Player_Loop()
        # Player movements
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
                if event.key == pygame.K_a:
                    x2_change = -10
                    y2_change = 0
                if event.key == pygame.K_d:
                    x2_change = 10
                    y2_change = 0
                if event.key == pygame.K_w:
                    x2_change = 0
                    y2_change = -10
                if event.key == pygame.K_s:
                    x2_change = 0
                    y2_change = 10
        # Check if player 1 leaves the screen
        if x1 >= settings.display_width or x1 < 0 or y1 >= settings.display_height or y1 < 0:
            winner = True
            snake1Dead = True
        # Check if player 2 leaves the screen
        if x2 >= settings.display_width or x2 < 0 or y2 >= settings.display_height or y2 < 0:
            winner = False
            snake2Dead = True

        x1 += x1_change
        y1 += y1_change
        x2 += x2_change
        y2 += y2_change
        display.fill(settings.black)
        # Draw food for both snakes
        pygame.draw.rect(display, settings.yellow,
                         [foodx, foody, snakeProperties.snake_block, snakeProperties.snake_block])
        pygame.draw.rect(display, settings.white,
                         [food2x, food2y, snakeProperties.snake_block, snakeProperties.snake_block])

        snake_head = [x1, y1]
        snake2_head = [x2, y2]
        snake_list.append(snake_head)
        snake2_list.append(snake2_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        if len(snake2_list) > snake2_length:
            del snake2_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                winner = True
                snake1Dead = True
        for x in snake2_list[:-1]:
            if x == snake2_head:
                winner = False
                snake2Dead = True
        # Determine who won based on points
        if snake1Dead and snake2Dead:
            if snake_length > snake2_length:
                winner = True
            else:
                winner = False
            game_close = True
        snakeProperties.current_snake(display, settings.green, snakeProperties.snake_block, snake_list)
        snakeProperties.current_snake(display, settings.blue, snakeProperties.snake2_block, snake2_list)
        messages.current_score(display, snake_length - 1, 0)
        messages.current_score(display, snake2_length - 1, 300)

        pygame.display.update()
        # Checks if a snake has ate food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, settings.display_width - snakeProperties.snake_block) / 10) * 10
            foody = round(random.randrange(0, settings.display_height - snakeProperties.snake_block) / 10) * 10
            snake_length += 1
            snakeProperties.snake_speed += 1
        if x2 == food2x and y2 == food2y:
            food2x = round(random.randrange(0, settings.display_width - snakeProperties.snake2_block) / 10) * 10
            food2y = round(random.randrange(0, settings.display_height - snakeProperties.snake2_block) / 10) * 10
            snake2_length += 1
            snakeProperties.snake2_speed += 1

        clock.tick(snakeProperties.snake_speed)
        clock.tick(snakeProperties.snake2_speed)

    pygame.quit()
    quit()
