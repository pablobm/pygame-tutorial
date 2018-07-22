import random
import pygame

BLACK = [0, 0, 0]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_STARS = 200

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

class Star:
    pass

star_list = []
i = 0
while i < NUM_STARS:
    new_star = Star()
    new_star.x = random.randint(0, 800)
    new_star.y = random.randint(0, 600)
    new_star.size = random.randint(1, 3)
    new_star.speed = random.randint(1, 3)
    new_star.brightness = random.randint(0, 255)
    star_list.append(new_star)
    i += 1

def move_x(sprite, change):
    sprite.x = sprite.x + change

def move_y(sprite, change):
    sprite.y = sprite.y + change

class Sprite:
    pass

player = Sprite()
player.image = pygame.image.load("python.png")
player.x = 100
player.y = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit(0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move_x(player, -5)
    if keys[pygame.K_RIGHT]:
        move_x(player, 5)
    if keys[pygame.K_DOWN]:
        move_y(player, 5)
    if keys[pygame.K_UP]:
        move_y(player, -5)

    for star in star_list:
        if star.y > 600:
            star.y = 0
            star.x = random.randint(0, 800)
        else:
            star.y = star.y + star.speed

    screen.fill(BLACK)

    for star in star_list:
        color = [star.brightness, star.brightness, star.brightness]
        position = [star.x, star.y]
        pygame.draw.circle(screen, color, position, star.size)

    screen.blit(player.image, [player.x, player.y])

    pygame.display.flip()
