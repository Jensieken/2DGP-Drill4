from pico2d import *

open_canvas()

walk = load_image('SamuraiGirl_Walk.png')
run = load_image('SamuraiGirl_Run.png')
jump = load_image('SamuraiGirl_Jump.png')
attack = load_image('SamuraiGirl_Attack1.png')
attack2 = load_image('SamuraiGirl_Attack2.png')

def act_walk():
    frame = 0
    for x in range(400, 800, 10):
        clear_canvas()
        walk.clip_draw(frame * 165, 0, 165, 130, x + 165 // 2, 150, 300, 300)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

    pass

def act_run():
    pass

def act_jump():
    pass

def act_attack():
    pass

act_walk()

close_canvas()