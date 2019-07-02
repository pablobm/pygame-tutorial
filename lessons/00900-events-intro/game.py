import pygame
import math

BLACK = [0, 0, 0]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
image = pygame.image.load("python.png")

count = 0
while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit(0)

  screen.fill(BLACK)

  angle = count/100.0
  x = SCREEN_WIDTH/2 - image.get_width()/2 + 100*math.sin(angle)
  y = SCREEN_HEIGHT/2 - image.get_height()/2 + 100*math.cos(angle)
  screen.blit(image, [x, y])

  pygame.display.flip()
  count = count + 1
