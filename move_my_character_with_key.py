from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('my_character.png')


def handle_events():
    global running, dir, right_left_move

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                right_left_move = True
            elif event.key == SDLK_LEFT:
                dir -= 1
                right_left_move = True
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            if event.key == SDLK_LEFT:
                dir += 1

running = True
right_left_move = False
x = 800 // 2
y = 600 // 2
frame = 0
dir = 0

while running:
    clear_canvas()
    ground.draw(400, 100)
    character.clip_draw(frame * 60, 180, 60, 60, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if  right_left_move:
        x += dir * 5
    delay(0.05)

close_canvas()

