import pygame

BLACK = [0, 0, 0]

pygame.init()
screen = pygame.display.set_mode([800, 600])

class Actor:
    pass

actor1 = Actor()
actor1.x = 100
actor1.y = 100
actor1.image = pygame.image.load("python.png")

actor2 = Actor()
actor2.x = 600
actor2.y = 100
actor2.image = pygame.image.load("python.png")

actor_list = [actor1, actor2]

count = 0
while count < 300:
  screen.fill(BLACK)
  for actor in actor_list:
      actor.y = actor.y + 1
      screen.blit(actor.image, [actor.x, actor.y])
  pygame.display.flip()
  count = count + 1
