import pygame

pygame.init()
screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("iprio")
clock = pygame.time.Clock()

# Character
player_x = 60
player_y = 515
player_w = 25
player_h = 40
speed = 5


# แรงโน้มถ่วงการกระโดด
velocity_y = 0
gravity = 0.8
jump_power = -15
on_ground = False
jump_count = 0
GROUND_Y = 600
MAX_JUMPS = 2

platforms = [
    # pygame.Rect(0, 600, 1400, 200),
    pygame.Rect(715, 500, 200, 30),
    pygame.Rect(1115, 475, 200, 30),
    pygame.Rect(630, 100, 50, 800),
    pygame.Rect(530, 475, 100, 20),
    pygame.Rect(425, 230, 100, 20),
#ซ้าย
    pygame.Rect(50, 550, 300, 20),
    pygame.Rect(350, 100, 20, 800),
    pygame.Rect(50, 400, 215, 20),
]



### Function ###
def drawplayer(x, y, w, h):
    """เขียนตัวละคร"""
    pygame.draw.rect(screen, (35, 161, 81), (x, y, w, h))
    
# def move_left_right(x, keys, spd):
#     """เดินซ้ายขวา แล้วส่งตำแหน่ง x ใหม่กลับ"""
#     spd = 10 if keys[pygame.K_LSHIFT] else 5
#     if keys[pygame.K_d]:
#         x += spd
#     if keys[pygame.K_a]:
#         x -= spd
#     return x

def keep_in_screen(x, w, screen_width):
    """กันตัวละครหลุดขอบจอ"""
    if x < 0:
        x = 0
    if x > screen_width - w:
        x = screen_width - w
    return x

def draw_ground():
    pygame.draw.rect(screen, (139, 69, 19), (0, GROUND_Y + player_h, 1400, 200))

def draw_platforms(plat_list):
    for plat in plat_list:
        pygame.draw.rect(screen, (0, 255, 100), plat)

# def check_platform_collision(x ,y, w, h, velocity_y, jump_count, on_ground, plat_list):
#     player_rect = pygame.Rect(x, y, w, h)
#     for plat in plat_list:
#         if player_rect.colliderect(plat):
#             # --
#             if velocity_y > 0:
#                 y = plat.top - h
#                 velocity_y = 0
#                 on_ground = True
#                 jump_count = 0
#             elif velocity_y < 0:
#                 y = plat.bottom
#                 velocity_y = 0
#             # --
#     return y, velocity_y, jump_count, on_ground

def move_x_and_collide(x, y, w, h, keys, plat_list):
    spd = 10 if keys[pygame.K_LSHIFT] else 5
    dx = 0
    if keys[pygame.K_d]:
        dx += spd
    if keys[pygame.K_a]:
        dx -= spd
    
    x += dx
    player_rect = pygame.Rect(x, y, w, h)
    for plat in plat_list:
        if player_rect.colliderect(plat):
            if dx > 0:
                x = plat.left - w
            elif dx < 0:
                x= plat.right
    return x

def move_y_and_collide(x, y, w, h, velocity_y, jump_count, on_ground, plat_list):
    velocity_y += gravity
    y += velocity_y

    on_ground = False
    player_rect = pygame.Rect(x, y, w, h)
    for plat in plat_list:
        if player_rect.colliderect(plat):
            if velocity_y > 0:
                y = plat.top - h 
                velocity_y = 0
                on_ground = True
                jump_count = 0
            elif velocity_y < 0:
                y = plat.bottom
                velocity_y = 0

    if y >= GROUND_Y:
        y = GROUND_Y
        velocity_y = 0
        on_ground = True
        jump_count = 0
    return y, velocity_y, jump_count, on_ground

def jump(velocity_y, jump_count, on_ground):
    if jump_count < MAX_JUMPS:
        velocity_y = jump_power
        jump_count += 1
        on_ground = False
    return velocity_y, jump_count, on_ground

def apply_gravity(y, velocity_y, jump_count, on_ground):
    velocity_y += gravity
    y += velocity_y
    if y >= GROUND_Y:
        y = GROUND_Y
        velocity_y = 0
        on_ground = True
        jump_count = 0
    return y, velocity_y, jump_count, on_ground

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      # กระโดด
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity_y, jump_count, on_ground = jump(velocity_y, jump_count, on_ground)
              
    keys = pygame.key.get_pressed()
    
    # player_x = move_left_right(player_x, keys, speed)
    # player_y, velocity_y, jump_count, on_ground = apply_gravity(player_y, velocity_y, jump_count, on_ground)
    # player_y, velocity_y, jump_count, on_ground = check_platform_collision(player_x, player_y, player_w, player_h, velocity_y, jump_count, on_ground, platforms)
    player_x = move_x_and_collide(player_x, player_y, player_w, player_h, keys, platforms)
    player_y, velocity_y, jump_count, on_ground = move_y_and_collide(player_x, player_y, player_w, player_h, velocity_y, jump_count, on_ground, platforms)
    player_x = keep_in_screen(player_x, player_w, 1400)

    screen.fill((201, 255, 255))
    draw_ground()
    draw_platforms(platforms)
    drawplayer(player_x, player_y, player_w, player_h)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


