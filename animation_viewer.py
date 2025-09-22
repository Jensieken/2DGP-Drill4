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
    attack1_widths = [102, 102, 172, 165]
    attack1_height = 130

    attack2_widths = [167, 167, 167]
    attack2_height = 170

    base_x = 400
    base_y = 150  # 바닥 y좌표 (walk 등과 동일하게 맞춤)
    draw_height = 300  # 항상 동일한 크기로 출력
    draw_width = 300

    # 1번 시트 프레임
    for i, width in enumerate(attack1_widths):
        clear_canvas()
        # 발이 바닥에 고정되도록 y좌표 보정
        offset_y = (draw_height // 2) - (attack1_height // 2)
        attack.clip_draw(sum(attack1_widths[:i]), 0, width, attack1_height,
                         base_x, base_y + offset_y, draw_width, draw_height)
        update_canvas()
        delay(0.15)

    # 2번 시트 프레임
    for i, width in enumerate(attack2_widths):
        clear_canvas()
        offset_y = (draw_height // 2) - (attack2_height // 2)
        attack2.clip_draw(sum(attack2_widths[:i]), 0, width, attack2_height,
                          base_x, base_y + offset_y, draw_width, draw_height)
        update_canvas()
        delay(0.15)
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