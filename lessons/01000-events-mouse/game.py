import pygame

BLACK = [0, 0, 0]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

class Sprite:
    pass

sprite = Sprite()
sprite.image = pygame.image.load("python.png")
sprite.x = 100
sprite.y = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        elif event.type == pygame.MOUSEMOTION:
            sprite.x = event.pos[0]
            sprite.y = event.pos[1]

    screen.fill(BLACK)
    screen.blit(sprite.image, [sprite.x, sprite.y])
    pygame.display.flip()
