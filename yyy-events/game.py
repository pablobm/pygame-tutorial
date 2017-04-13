import pygame

BLACK = [0, 0, 0]

pygame.init()
screen = pygame.display.set_mode([800, 600])

class Actor:
    pass

player = Actor()
player.x = 100
player.y = 100
player.image = pygame.image.load("python.png")

keep_running = True
while keep_running:
    pending_events = pygame.event.get()
    for event in pending_events:
        if event.type == pygame.QUIT:
            keep_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -= 5
            elif event.key == pygame.K_RIGHT:
                player.x += 5
            elif event.key == pygame.K_UP:
                player.y -= 5
            elif event.key == pygame.K_DOWN:
                player.y += 5

    screen.fill(BLACK)
    screen.blit(player.image, [player.x, player.y])
    pygame.display.flip()
