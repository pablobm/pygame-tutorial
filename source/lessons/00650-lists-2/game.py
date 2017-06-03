import pygame

BLACK = [0, 0, 0]

pygame.init()
screen = pygame.display.set_mode([800, 600])

class Actor:
    pass

actor_list = []
count = 0
while count < 20:
  actor = Actor()
  actor.x = count * 37
  actor.y = count * 13
  actor.image = pygame.image.load("python.png")
  actor_list.append(actor)
  count = count + 1

count = 0
while count < 300:
  screen.fill(BLACK)
  for actor in actor_list:
      actor.y = actor.y + 1
      screen.blit(actor.image, [actor.x, actor.y])
  pygame.display.flip()
  count = count + 1
