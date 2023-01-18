from pico2d import *

frame = 0


class CharacterManager:
    pass


class Dog(CharacterManager):

    def __init__(self):
        self.image = load_image("bird1.png")

    def draw(self):
        global frame
        self.image.clip_draw(frame * 32, 0, 32, 32, 200, 200, 128, 128)
        frame = (frame + 1) % 2
        delay(0.5)


class Cat(CharacterManager):
    pass
