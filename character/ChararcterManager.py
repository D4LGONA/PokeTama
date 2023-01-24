from pico2d import *

import character.ChararcterManager


class CharacterManager:
    image = ""  # 캐릭터 이름
    frame = 0  # 이미지 리소스 Y 프레임
    age = 0  # 캐릭터 나이
    name = ""  # 캐릭터 이름
    food = 100
    clean = 100
    fun = 100
    love = 0

    def SetName(self):
        self.name = input()  # 돌아 가는지 확인 해야 함

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 32, 0, 32, 32, 200, 200, 128, 128)
        self.frame = (self.frame + 1) % 2
        delay(0.5)


class Dog(CharacterManager):

    def __init__(self):
        self.image = load_image("bird1.png")
        self.frame = 0

    def SetName(self):
        self.name = input()

    def update(self):
        pass
        # Todo: 얼마 만큼 떨어질 지 정해야 함

    def draw(self):
        self.image.clip_draw(self.frame * 32, 0, 32, 32, 200, 200, 128, 128)
        self.frame = (self.frame + 1) % 2
        delay(0.5)
