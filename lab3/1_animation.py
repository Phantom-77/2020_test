# This is the "Race 2.2" program, where 2 cars driven by two players
import pygame
import sys
import time
import winsound
from pygame.draw import *

pygame.init()
pygame.mixer.init()


def draw_car(r, g, b, x, y, number):
    """This function draws a car of color (rgb) at coordinates (x,y)
    with number car (number)"""
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
    print_text(number, 36, x + 45, y - 28)


def draw_racing_lines():
    """This function draws lines START & FINISH"""
    print_text('START', 36, 1010, 25)
    print_text('FINISH', 36, 100, 25)
    line(screen, (255, 255, 255), [1000, 0], [1000, 400], 5)
    for y in range(0, 400, 20):
        sq1 = pygame.Rect((195, y, 10, 10))
        sq2 = pygame.Rect((205, y + 10, 10, 10))
        rect(screen, (255, 255, 255), sq1)
        rect(screen, (255, 255, 255), sq2)


def print_text(content, f_size, x, y):
    """This function print text on screen 'content' - text,
     f_size - font size in pixels, (x,y) - coordinates"""
    f1 = pygame.font.Font(None, f_size)
    text = f1.render(content, True, (255, 255, 255))
    screen.blit(text, (x, y))


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

print_text('Press the button to control the Car :', 22, 500, 325)
print_text('Car 1 :  <A>   - forward;    <D>   - back', 22, 500, 350)
print_text('Car 2 : <Left> - forward;  <Right> - back', 22, 500, 375)
draw_racing_lines()
draw_car(0, 128, 128, x1, 150, '1')
draw_car(0, 128, 0, x2, 300, '2')
pygame.display.update()
time.sleep(3)

# Countdown before the start
A = ['3', '2', '1', 'GO!!!']
B = [500, 500, 500, 1000]
for n in range(len(A)):
    print_text(A[n], 52, 610, 150)
    pygame.display.update()
    rect(screen, (0, 0, 0), (600, 135, 110, 60))
    winsound.Beep(B[n], B[n])
    time.sleep(0.5)

pygame.mixer.music.play(-1)

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            sys.exit()

    screen.fill(black)
    print_text('Press <A>, <D> - car 1   <Left>, <Right> - car 2', 20, 470, 370)
    draw_racing_lines()
    draw_car(0, 128, 128, x1, 150, '1')
    draw_car(0, 128, 0, x2, 300, '2')
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if x1 > 150 and x2 > 150:
        if keys[pygame.K_a]:
            x1 -= 5
        elif keys[pygame.K_d]:
            x1 += 5

        if keys[pygame.K_LEFT]:
            x2 -= 5
        elif keys[pygame.K_RIGHT]:
            x2 += 5

    elif x1 == 150 and x2 > 150:
        print_text('Car 1 - WINNER!!!', 36, 510, 150)
        pygame.display.update()
        pygame.mixer.music.stop()
    elif x2 == 150 and x1 > 150:
        print_text('Car 2 - WINNER!!!', 36, 510, 150)
        pygame.display.update()
        pygame.mixer.music.stop()
    else:
        print_text('Draw - no winner', 36, 510, 150)
        pygame.display.update()
        pygame.mixer.music.stop()

    clock.tick(FPS)
