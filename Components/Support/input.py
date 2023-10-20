from slitherzenith import *

# Nintendo Switch Pro controller
SWITCH_A = 0
SWITCH_B = 1
SWITCH_X = 2
SWITCH_Y = 3
SWITCH_MINUS = 4
SWITCH_PLUS = 6
SWITCH_D_UP = 11
SWITCH_D_DOWN = 12
SWITCH_D_LEFT = 13
SWITCH_D_RIGHT = 14

click_delay = 10
click_timer = 0
clickable = True


def move_right_key_pressed():
    return (is_key_down("d") or
            is_key_down('right') or
            is_nintendo_switch_pro_button_down(SWITCH_D_RIGHT))


def move_left_key_pressed():
    return (is_key_down("a") or
            is_key_down('left') or
            is_nintendo_switch_pro_button_down(SWITCH_D_LEFT))


def jump_key_pressed():
    return (is_key_down("w") or
            is_key_down('up') or
            is_key_down('space') or
            is_nintendo_switch_pro_button_down(SWITCH_A) or
            is_nintendo_switch_pro_button_down(SWITCH_B))


def attack_key_pressed():
    return (is_key_down("shift") or
            is_nintendo_switch_pro_button_down(SWITCH_Y))


def skip_key_pressed():
    return (is_key_down("space") or
            is_nintendo_switch_pro_button_down(SWITCH_X))


def return_key_pressed():
    return (is_key_down("return") or
            is_nintendo_switch_pro_button_down(SWITCH_A))


def pause_key_pressed():
    return (is_key_down("esc") or
            is_nintendo_switch_pro_button_down(SWITCH_X))