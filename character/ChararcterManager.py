from pico2d import *


class CharacterManager:
    pass


class Dog(CharacterManager):
    def __init__(self):
        self.image = load_image("dog.png")

    def draw(self):
        self.image.draw(200, 200)


class Cat(CharacterManager):
    pass
