import game_framework
from pico2d import *
import home_state

# Todo: 어떻게 캐릭터의 상태 값을 가져올 것인가?

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
            game_framework.change_state(home_state)


def draw():
    clear_canvas()
    image.draw(200, 200)
    update_canvas()
