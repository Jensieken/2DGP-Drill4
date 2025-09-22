from pico2d import *

open_canvas()

walk = load_image('SamuraiGirl_Walk.png')

frame = 0
for x in range(0, 800, 10):
    clear_canvas()
    walk.clip_draw(frame * 100, 0, 100, 100, x + 50, 90)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()