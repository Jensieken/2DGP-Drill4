from pico2d import *

open_canvas()

walk = load_image('SamuraiGirl_Walk.png')
run = load_image('SamuraiGirl_Run.png')
jump = load_image('SamuraiGirl_Jump.png')
attack = load_image('SamuraiGirl_Attack1.png')
attack2 = load_image('SamuraiGirl_Attack2.png')

def act_walk():
    frame = 0
    for x in range(320, 800, 10):
        clear_canvas()
        walk.clip_draw(frame * 165, 0, 165, 130, x + 165 // 2, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

    pass

def act_run():
    frame = 0
    for x in range(320, 800, 20):
        clear_canvas()
        run.clip_draw(frame * 165, 0, 165, 130, x + 165 // 2, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    pass

def act_jump():
    frame = 0
    for x in range(320, 800, 20):
        clear_canvas()
        jump.clip_draw(frame * 165, 0, 165, 130, x + 165 // 2, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    pass

def act_attack():
    pass

while True:
    for _ in range(5):
        act_walk()
    delay(1)
    for _ in range(5):
        act_run()
    delay(1)
    for _ in range(5):
        act_jump()
    delay(1)
    for _ in range(5):
        act_attack()
    delay(1)

close_canvas()