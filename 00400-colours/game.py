import pygame

BLACK = [0, 0, 0]

pygame.init()
screen = pygame.display.set_mode([800, 600])
image = pygame.image.load("python.png")

count = 0
while count < 1000:
  screen.fill(BLACK)
  screen.blit(image, [count, 0])
  pygame.display.flip()
  count = count + 1
