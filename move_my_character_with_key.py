from pico2d import *

wight, height = 1280, 1024
open_canvas(wight, height)

character = load_image('Char_Move.png')
ground = load_image('TUK_GROUND.png')

running = True
x, y = wight // 2, height // 2
frameX, frameY = 0, 320
dirX, dirY = 0, 0

def handle_events():
    global running, dirX, dirY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
            elif event.key == SDLK_LEFT:
                dirX += 1
            elif event.key == SDLK_UP:
                dirY -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1
                
while running:
    clear_canvas()
    
    ground.draw(wight // 2, height // 2)
    character.clip_draw(frameX * 160, frameY, 160, 320, x, y, 80, 160)
    
    update_canvas()
    handle_events()
    
    if dirX > 0:
        frameY = 960
    elif dirX < 0:
        frameY = 640
    elif dirY > 0:
        frameY = 0
    elif dirY < 0:
        frameY = 320

    if dirX == 0:
        frameX = (frameX + 1) % 3
    else :
        frameX = (frameX + 1) % 4
        
    x += dirX * 10
    y += dirY * 10
    
    if x < 40:
        x = 40
    elif x > wight - 40:
        x = wight - 40
    if y < 80:
        y = 80
    elif y > height - 80:
        y = height - 80

    delay(0.1)
    
close_canvas()
