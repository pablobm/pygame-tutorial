import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])
image = pygame.image.load("python.png")

count = 0
while count < 100:
  screen.fill([0, 0, 0])
  screen.blit(image, [count, 0])
  pygame.display.flip()
  count = count + 1
