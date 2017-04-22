import pygame

class Actor:
    pass

BLACK = [0, 0, 0]

pygame.init()
screen = pygame.display.set_mode([800, 600])

logo = Actor()
logo.image = pygame.image.load("python.png")
logo.x = 0
logo.y = 0

count = 0
while count < 600:
  screen.fill(BLACK)
  logo.y = count
  logo.x = count * 1.25
  screen.blit(logo.image, [logo.x, logo.y])
  pygame.display.flip()
  count = count + 1
