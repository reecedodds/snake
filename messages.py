import settings

def message(display, msg, color, y_coor):
    """Displays a message using font_style"""
    mesg = settings.font_style.render(msg, True, color)
    display.blit(mesg, [settings.display_width / 6, y_coor])


def message_to_screen(display, mes, font, color, x_dis, y_dis):
    """Displays a message to a precise location on the screen"""
    mesg = font.render(mes, True, color)
    display.blit(mesg, [x_dis, y_dis])


def current_score(display, score, x_coor):
    """Displays the score based is a position based on an x-coordinate"""
    value = settings.score_font.render(f"Your Score : {score}", True, settings.white)
    display.blit(value, [x_coor, 0])
