from pico2d import *



open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('real_my_sprite.png')


def handle_events():
    global running, dir, right_left_move, up_down_move, framey, down, up, right, left

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                framey = 0
                dir += 1
                right_left_move = True
            elif event.key == SDLK_LEFT:
                framey = 2
                dir -= 1
                right_left_move = True
            elif event.key == SDLK_UP:
                framey = 1
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
                right = True
                left = False
                up = False
                down = False
            if event.key == SDLK_LEFT:
                dir += 1
                right_left_move = False
                right = False
                left = True
                up = False
                down = False
            if event.key == SDLK_UP:
                dir -= 1
                up_down_move = False
                right = False
                left = False
                up = True
                down = False
            if event.key == SDLK_DOWN:
                dir += 1
                up_down_move = False
                right = False
                left = False
                up = False
                down = True

running = True
right_left_move = False
up_down_move = False
left = False
right = False
up = False
down = True

x = 800 // 2
y = 600 // 2
framex = 0
framey = 7
dir = 0

while running:
    clear_canvas()
    ground.draw(400, 100)
    character.clip_draw(framex * 90, framey * 97, 90, 97, x, y)
    update_canvas()
    handle_events()
    if  right_left_move:
        framex = (framex + 1) % 10
        x += dir * 10
        if x <= 0 or x >= 800:
            x -= dir * 10
    elif  up_down_move:
        framex = (framex + 1) % 10
        y += dir * 10
        if y <= 0 or y >= 600:
            y -= dir * 10
    elif down:
        framey = 7
        framex = (framex + 1) % 3
    elif up:
        framey = 5
        framex = (framex + 1) % 1
    elif right:
        framey = 4
        framex = (framex + 1) % 3
    elif left:
        framey = 6
        framex = (framex + 1) % 3
    delay(0.05)

close_canvas()

