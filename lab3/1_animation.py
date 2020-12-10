import pygame
from pygame.draw import *

# Pygame module initialization
pygame.init()
pygame.mixer.init()


def draw_car_body(r, g, b, x, y):
    """This function draws a car of color (rgb) at coordinates (x,y)"""
    rect(screen, (r, g, b), (x - 30, y - 30, 160, 30))
    polygon(screen, (r, g, b), [(x, y - 30), (x + 30, y - 60),
                                (x + 70, y - 60), (x + 100, y - 30)])
    polygon(screen, (173, 216, 230), [(x + 10, y - 35), (x + 30, y - 55),
                                      (x + 55, y - 55), (x + 55, y - 35)])
    polygon(screen, (173, 216, 230), [(x + 60, y - 35), (x + 60, y - 55),
                                      (x + 70, y - 55), (x + 85, y - 35)])
    rect(screen, (255, 255, 255), (x - 30, y - 25, 10, 5))
    rect(screen, (255, 0, 0), (x + 120, y - 25, 10, 10))


def draw_wheel(x, y):
    """This function draws the wheel at coordinates (x,y)"""
    circle(screen, (47, 79, 79), (x, y), 20, 8)
    circle(screen, (176, 196, 222), (x, y), 12, 10)
    circle(screen, (0, 0, 0), (x, y), 20, 2)
    circle(screen, (0, 0, 0), (x, y), 4)


# Create window
FPS = 30
black = (0, 0, 0)
screen = pygame.display.set_mode((1200, 400))

# Play sound
pygame.mixer.music.load('car_sound.wav')
pygame.mixer.music.play()

# Draw a car in motion
y = 150
for x in range(1050, 50, -1):
    screen.fill(black)
    f = pygame.font.Font(None, 36)
    text1 = f.render('START', True, (255, 255, 255))
    text2 = f.render('FINISH', True, (255, 255, 255))
    line(screen, (255, 255, 255), [1000, 0], [1000, 400], 5)
    screen.blit(text1, (1010, 25))
    line(screen, (255, 255, 255), [195, 0], [195, 400], 10)
    screen.blit(text2, (100, 25))
    # Car 1
    draw_car_body(0, 128, 128, x, y)
    draw_wheel(x, y)
    draw_wheel(x + 100, y)
    # Car 2
    draw_car_body(0, 128, 0, x * 1.1, y + 150)
    draw_wheel(x * 1.1, y + 150)
    draw_wheel(x * 1.1 + 100, y + 150)
    pygame.display.update()

pygame.mixer.music.stop()
pygame.mixer.music.unload()
clock = pygame.time.Clock()
finished = False

# Tracking events
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
