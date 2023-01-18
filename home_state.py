import game_framework
from pico2d import *
import character.ChararcterManager

bg = None
Character = None

def enter():
    global bg
    global Character
    bg = load_image('title.png')
    Character = character.ChararcterManager.Dog()


def exit():
    global bg
    global Character
    del bg
    del Character


def update():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def draw():
    clear_canvas()
    bg.draw(200, 200)
    Character.draw()

    update_canvas()