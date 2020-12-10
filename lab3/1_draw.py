# This is a sample Python script 'Draw a car'
import pygame
from pygame.draw import *

# Pygame module initialization
pygame.init()


def draw_wheel(x, y):
    """This function draws the wheel at coordinates (x, y)"""
    circle(screen, (47, 79, 79), (x, y), 50, 20)
    circle(screen, (176, 196, 222), (x, y), 30, 25)
    circle(screen, (0, 0, 0), (x, y), 60, 10)
    circle(screen, (0, 0, 0), (x, y), 5)


# Create window
FPS = 30
screen = pygame.display.set_mode((500, 500))

# Painting body car
rect(screen, (0, 128, 128), (25, 300, 450, 100))
polygon(screen, (0, 128, 128), [(150, 300), (250, 200), (400, 200), (450, 300)])
polygon(screen, (173, 216, 230), [(175, 290), (250, 210), (350, 210), (350, 290)])
polygon(screen, (173, 216, 230), [(375, 210), (390, 210), (425, 290), (375, 290)])
polygon(screen, (0, 0, 0), [(175, 290), (250, 210), (350, 210),
                            (350, 325), (300, 375), (175, 375)], 5)     # Door
rect(screen, (255, 255, 255), (25, 315, 25, 25))        # Headlight
rect(screen, (255, 0, 0), (450, 310, 25, 45))           # Rear StopLight
# Painting wheels
draw_wheel(100, 400)
draw_wheel(400, 400)

# Display on screen
pygame.display.update()
clock = pygame.time.Clock()
finished = False

# Tracking events
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
