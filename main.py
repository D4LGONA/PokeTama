import pico2d
import title_state
import game_framework

WIDTH, HEIGHT = 400, 400

pico2d.open_canvas(WIDTH, HEIGHT)
game_framework.run(title_state)
pico2d.close_canvas()