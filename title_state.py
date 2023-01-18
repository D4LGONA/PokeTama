import game_framework
import home_state
from pico2d import *

image = None


def enter():
    global image
    image = load_image('title.png')


def exit():
    global image
    del image


def update():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(home_state)


def draw():
    clear_canvas()
    image.draw(200, 200)
    update_canvas()