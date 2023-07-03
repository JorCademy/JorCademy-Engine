import pygame
from pygame.locals import *

__calls_down_event = {}
__calls_up_event = {}


def handle_input(game_event: pygame.event):
    if not (game_event.type == KEYDOWN or game_event.type == KEYUP):
        return
    key = key_to_str(game_event.key)
    print(f"received {key} event")
    if game_event.type == KEYDOWN:
        __notify_key_down(key)
    elif game_event.type == KEYUP:
        __notify_key_up(key)



def key_to_str(key: int) -> str:
    if key >= 33 and key<=126:
        return chr(key)
    elif key == 32:
        return "space"
    elif key == 1073742050:
        return "alt"
    elif key == 1073742048:
        return "ctrl"
    elif key == 1073742049:
        return "shift"
    elif key == 1073741881:
        return "caps"
    elif key == 9:
        return "tab"
    #TODO
    return "other"


def add_key_down_event(key: str, function):
    if key in __calls_down_event:
        __calls_down_event[key].append(function)
    else:
        __calls_down_event[key] = [function]


def add_key_up_event(key: str, function):
    if key in __calls_up_event:
        __calls_up_event[key].append(function)
    else:
        __calls_up_event[key] = [function]


def remove_key_down_event(key: str, function):
    __calls_down_event[key].remove(function)


def remove_key_up_event(key: str, function):
    __calls_up_event[key].remove(function)


def __notify_key_down(key: str):
    if key not in __calls_down_event:
        return
    for f in __calls_down_event[key]:
        f()


def __notify_key_up(key: str):
    if key not in __calls_up_event:
        return
    for f in __calls_up_event[key]:
        f()

