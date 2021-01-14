import pygame
import onePlayer
import settings
import twoPlayer
import messages

pygame.init()

# Initializing the intro display, will be the first thing the user see's
introDisplay = display = pygame.display.set_mode((settings.display_width, settings.display_height))

# Setting the title of the game in the window
pygame.display.set_caption("Reece's Snake Game")


def intro():
    """Introduction view, used as a way to ask the user what game mod they would like to play."""
    while True:
        # For every event that takes place
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            # Starts a game mode based on which button was pressed on the intro view
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 70 + 140 > mouse[0] > 70 and 300 + 40 > mouse[1] > 300:
                    onePlayer.game_loop()
                if 400 + 140 > mouse[0] > 400 and 300 + 40 > mouse[1] > 300:
                    twoPlayer.two_Player_Loop()

        # To know the current position of the cursor
        mouse = pygame.mouse.get_pos()

        # Creating the two buttons, once hovered they will change colour
        if 70 + 140 > mouse[0] > 70 and 300 + 40 > mouse[1] > 300:
            pygame.draw.rect(introDisplay, settings.red, [70, 300, 140, 40])
        else:
            pygame.draw.rect(introDisplay, settings.green, [70, 300, 140, 40])

        if 400 + 140 > mouse[0] > 400 and 300 + 40 > mouse[1] > 300:
            pygame.draw.rect(introDisplay, settings.red, [400, 300, 140, 40])
        else:
            pygame.draw.rect(introDisplay, settings.blue, [400, 300, 140, 40])

        # Adding text to the buttons
        messages.message_to_screen(introDisplay, "Welecome to Snake!", settings.score_font, settings.white, 0, 0)
        messages.message_to_screen(introDisplay, "Created by Reece Dodds", settings.score_font, settings.white, 0, 50)
        messages.message_to_screen(introDisplay, "1-Player", settings.small_text, settings.white, 95, 310)
        messages.message_to_screen(introDisplay, "2-Player", settings.small_text, settings.white, 425, 310)

        # updates the frames of the game
        pygame.display.update()

    pygame.quit()
    quit()

intro()
