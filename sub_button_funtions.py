back_button_x1 = 47
back_button_y1 = 980
back_button_x2 = 118
back_button_y2 = 1052


def is_back_button(x, y):
    if back_button_x1 <= x <= back_button_x2 and back_button_y1 <= y <= back_button_y2:
        return True
    return False


width = 1920
credit_button_x1 = 1309
credit_button_y1 = 0
credit_button_x2 = width
credit_button_y2 = 64


def is_credit_button(x, y):
    if credit_button_x1 <= x <= credit_button_x2 and credit_button_y1 <= y <= credit_button_y2:
        return True
    return False


def next_screen_stack(screen_stack, screen):
    screen_stack.append(screen)
    return screen_stack, screen
    pass
