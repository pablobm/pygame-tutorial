import random
import pygame

NUM_CIRCLES = 100

class Circle:
    pass

circle_list = []
i = 0
while i < NUM_CIRCLES:
    circle = Circle()
    circle.x = random.randint(0, 800)
    circle.y = random.randint(0, 600)
    circle.radius = random.randint(5, 50)
    circle_list.append(circle)
    i += 1

pygame.init()
screen = pygame.display.set_mode([800, 600])

for circle in circle_list:
    pygame.draw.circle(screen, [255, 255, 255], [circle.x, circle.y], circle.radius)
pygame.display.flip()
