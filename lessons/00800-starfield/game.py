import random
import pygame

BLACK = [0, 0, 0]
NUM_STARS = 200

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

pygame.init()
screen = pygame.display.set_mode([800, 600])

count = 0
while count < 1000:
  screen.fill(BLACK)
  for star in star_list:
      color = [star.brightness, star.brightness, star.brightness]
      position = [star.x, star.y]
      pygame.draw.circle(screen, color, position, star.size)
      if star.y > 600:
          star.y = 0
          star.x = random.randint(0, 800)
      else:
          star.y = star.y + star.speed

  pygame.display.flip()
  count = count + 1
