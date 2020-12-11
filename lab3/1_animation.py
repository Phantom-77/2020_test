# This is the "Race 2.1" program, where there are 2 cars driven by two players
import pygame
import sys
from pygame.draw import *

pygame.init()
pygame.mixer.init()


def draw_car(r, g, b, x, y):
    """This function draws a car of color (rgb) at coordinates (x,y)"""
    # Body car
    rect(screen, (r, g, b), (x - 30, y - 30, 160, 30))
    polygon(screen, (r, g, b), [(x, y - 30), (x + 30, y - 60),
                                (x + 70, y - 60), (x + 100, y - 30)])
    polygon(screen, (173, 216, 230), [(x + 10, y - 35), (x + 30, y - 55),
                                      (x + 55, y - 55), (x + 55, y - 35)])
    polygon(screen, (173, 216, 230), [(x + 60, y - 35), (x + 60, y - 55),
                                      (x + 70, y - 55), (x + 85, y - 35)])
    # Headlights and stop signal
    rect(screen, (255, 255, 255), (x - 30, y - 25, 10, 5))
    rect(screen, (0, 0, 0), (x - 30, y - 25, 10, 5), 1)
    rect(screen, (255, 0, 0), (x + 120, y - 25, 10, 10))
    rect(screen, (0, 0, 0), (x + 120, y - 25, 10, 10), 1)
    # Wheel left
    circle(screen, (47, 79, 79), (x, y), 20, 8)
    circle(screen, (176, 196, 222), (x, y), 12, 10)
    circle(screen, (0, 0, 0), (x, y), 20, 2)
    circle(screen, (0, 0, 0), (x, y), 4)
    # Wheel right
    circle(screen, (47, 79, 79), (x + 100, y), 20, 8)
    circle(screen, (176, 196, 222), (x + 100, y), 12, 10)
    circle(screen, (0, 0, 0), (x + 100, y), 20, 2)
    circle(screen, (0, 0, 0), (x + 100, y), 4)


def draw_racing_lines():
    """This function draws lines START & FINISH"""
    print_text('START', 36, 1010, 25)
    print_text('FINISH', 36, 100, 25)
    line(screen, (255, 255, 255), [1000, 0], [1000, 400], 5)
    for y3 in range(0, 400, 20):
        sq1 = pygame.Rect((195, y3, 10, 10))
        sq2 = pygame.Rect((205, y3+10, 10, 10))
        rect(screen, (255, 255, 255), sq1)
        rect(screen, (255, 255, 255), sq2)


def print_text(content, f_size, x3, y3):
    """This function print text on screen 'content' - text,
     f_size - font size in pixels, (x3,y3) - coordinates"""
    f1 = pygame.font.Font(None, f_size)
    text = f1.render(content, True, (255, 255, 255))
    screen.blit(text, (x3, y3))


# Create window and load sound
FPS = 30
vin_width = 1200
vin_height = 400
black = (0, 0, 0)
x1 = 1050
x2 = 1050

screen = pygame.display.set_mode((vin_width, vin_height))
clock = pygame.time.Clock()
pygame.mixer.music.load('car_sound.wav')
pygame.mixer.music.play(-1)

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            sys.exit()

    screen.fill(black)
    print_text('Press <A>, <D> - car 1; <Left>, <Right> - car 2', 20, 470, 370)
    draw_racing_lines()
    draw_car(0, 128, 128, x1, 150)
    draw_car(0, 128, 0, x2, 300)
    pygame.display.update()

    if x1 <= 150:
        print_text('Car 1 - WINNER!!!', 36, 510, 150)
        pygame.display.update()
    elif x2 <= 150:
        print_text('Car 2 - WINNER!!!', 36, 510, 150)
        pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        x1 -= 5
    elif keys[pygame.K_d]:
        x1 += 5

    if keys[pygame.K_LEFT]:
        x2 -= 5
    elif keys[pygame.K_RIGHT]:
        x2 += 5

    clock.tick(FPS)
