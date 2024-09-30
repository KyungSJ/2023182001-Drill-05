from pico2d import *

from move_character_with_key import frame

open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('my_character.png')


def handle_events():
    global running, dir, right_left_move, up_down_move, framey

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                framey = 1
                dir += 1
                right_left_move = True
            elif event.key == SDLK_LEFT:
                framey = 2
                dir -= 1
                right_left_move = True
            elif event.key == SDLK_UP:
                framey = 0
                dir += 1
                up_down_move = True
            elif event.key == SDLK_DOWN:
                framey = 3
                dir -= 1
                up_down_move = True
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                right_left_move = False
            if event.key == SDLK_LEFT:
                dir += 1
                right_left_move = False
            if event.key == SDLK_UP:
                dir -= 1
                up_down_move = False
            if event.key == SDLK_DOWN:
                dir += 1
                up_down_move = False

running = True
right_left_move = False
up_down_move = False

x = 800 // 2
y = 600 // 2
framex = 0
framey = 3
dir = 0

while running:
    clear_canvas()
    ground.draw(400, 100)
    character.clip_draw(framex * 60, framey * 60, 60, 60, x, y, 100, 100)
    update_canvas()
    handle_events()
    if  right_left_move:
        framex = (framex + 1) % 8
        x += dir * 10
        if x <= 0 or x >= 800:
            x -= dir * 10
    if  up_down_move:
        framex = (framex + 1) % 8
        y += dir * 10
        if y <= 0 or y >= 600:
            y -= dir * 10
    delay(0.05)

close_canvas()

