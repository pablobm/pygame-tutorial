import pygame

BLACK = [0, 0, 0]

pygame.init()
screen = pygame.display.set_mode([800, 600])
image = pygame.image.load("python.png")

count = 0
keep_running = True
while keep_running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      #keep_running = False
      exit(0)

  screen.fill(BLACK)
  screen.blit(image, [count, 0])
  pygame.display.flip()
  count = count + 1
