import pygame

pygame.init()
screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("iprio")
clock = pygame.time.Clock()

# Character
player_x = 60
player_y = 250
player_w = 25
player_h = 40
# 
speed = 5

# แรงโน้มถ่วงการกระโดด
velocity_y = 0
gravity = 0.8
jump_power = -15
on_ground = False
jump_count = 0
GROUND_Y = 600
MAX_JUMPS = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
         # กระโดด
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if jump_count < MAX_JUMPS:
                    velocity_y = jump_power
                    jump_count += 1
                    on_ground = False
              


    keys = pygame.key.get_pressed()

    # เดินซ้ายขวา
    if keys[pygame.K_LSHIFT]:
        speed = 10
    else:
        speed = 5
    if keys[pygame.K_d]:
        player_x += speed
    if keys[pygame.K_a]:
        player_x -= speed



    velocity_y += gravity
    player_y += velocity_y

    # เช็คชนพื้น
    if player_y >= GROUND_Y:
        player_y = GROUND_Y
        velocity_y = 0
        on_ground = True
        jump_count = 0

    #   กันหลุดขอบจอ ซ้ายขวา
    if player_x < 0:
        player_x = 0
    if player_x > 1400 - player_w:
        player_x = 1400 - player_w

    screen.fill((201, 255, 255))
    pygame.draw.rect(screen, (35, 161, 81), (player_x, player_y, player_w, player_h))
    pygame.display.flip()
    clock.tick(60)

# pygame.time.delay(5000)
pygame.quit()



