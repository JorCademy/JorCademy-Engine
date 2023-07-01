import pygame
from pygame.locals import *

__calls_down_event = {}
__calls_up_event = {}


def handle_input(game_event: pygame.event):
    if not (game_event.type == KEYDOWN or game_event.type == KEYUP):
        return

    if game_event.key >= 33 and game_event.key<=126:
        key = chr(game_event.key)
    else:
        key = key_to_str(game_event.key)

    if game_event.type == KEYDOWN:
        __notify_key_down(key)
    elif game_event.type == KEYUP:
        __notify_key_up(key)



def key_to_str(key: int) -> str:
    if key is 32:
        return "space"
    #TODO
    return "other"


def key_down_event(key: str, function):
    if key in __calls_down_event:
        __calls_down_event[key] += function
    else:
        __calls_down_event[key] = [function]


def key_up_event(key: str, function):
    if key in __calls_up_event:
        __calls_up_event[key] += function
    else:
        __calls_up_event[key] = [function]
        

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

