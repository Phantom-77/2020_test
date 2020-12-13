# This is the "Race 2.2.1" program, where 2 cars driven by two players
import pygame
import sys
import time
import winsound
from random import randint

pygame.init()
pygame.mixer.init()


def draw_car(x, y, number, r=255, g=255, b=255):
    """This function draws car in coordinates (x,y)
    with number (number) and color (RGB),
    the default car color is white"""
    # Body car
    pygame.draw.rect(screen, (r, g, b), (x - 30, y - 30, 160, 30))
    pygame.draw.polygon(screen, (r, g, b), [(x, y - 30), (x + 30, y - 60),
                                            (x + 70, y - 60), (x + 100, y - 30)])
    pygame.draw.polygon(screen, (173, 216, 230), [(x + 10, y - 35), (x + 30, y - 55),
                                                  (x + 55, y - 55), (x + 55, y - 35)])
    pygame.draw.polygon(screen, (173, 216, 230), [(x + 60, y - 35), (x + 60, y - 55),
                                                  (x + 70, y - 55), (x + 85, y - 35)])
    # Headlights and stop signal
    pygame.draw.rect(screen, (255, 255, 255), (x - 30, y - 25, 10, 5))
    pygame.draw.rect(screen, (0, 0, 0), (x - 30, y - 25, 10, 5), 1)
    pygame.draw.rect(screen, (255, 0, 0), (x + 120, y - 25, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (x + 120, y - 25, 10, 10), 1)
    # Wheel left
    pygame.draw.circle(screen, (47, 79, 79), (x, y), 20, 8)
    pygame.draw.circle(screen, (176, 196, 222), (x, y), 12, 10)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 20, 2)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 4)
    # Wheel right
    pygame.draw.circle(screen, (47, 79, 79), (x + 100, y), 20, 8)
    pygame.draw.circle(screen, (176, 196, 222), (x + 100, y), 12, 10)
    pygame.draw.circle(screen, (0, 0, 0), (x + 100, y), 20, 2)
    pygame.draw.circle(screen, (0, 0, 0), (x + 100, y), 4)
    print_text(number, 36, x + 45, y - 28, 0, 0, 0)


def draw_racing_lines():
    """This function draws lines START & FINISH"""
    print_text('START', 36, 1010, 25)
    print_text('FINISH', 36, 100, 25)
    pygame.draw.line(screen, (255, 255, 255), [1000, 0], [1000, 400], 5)
    for y in range(0, 400, 20):
        sq1 = pygame.Rect((195, y, 10, 10))
        sq2 = pygame.Rect((205, y + 10, 10, 10))
        pygame.draw.rect(screen, (255, 255, 255), sq1)
        pygame.draw.rect(screen, (255, 255, 255), sq2)


def print_text(content, f_size, x, y, r=255, g=255, b=255):
    """This function displays text:
    'content' - the text itself, f_size - the font size in pixels,
    (x,y) - the text coordinates, (RGB) - the text color,
    the default text color is white"""
    ft = pygame.font.Font(None, f_size)
    text = ft.render(content, True, (r, g, b))
    screen.blit(text, (x, y))


FPS = 30
SIZE = (1200, 400)
BLACK = (0, 0, 0)

# Create window and load sound
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('Race 2.2.1')
pygame.mixer.music.load('car_sound.wav')

print_text('Press the button to control the Car :', 22, 500, 325)
print_text('Car 1 :  <A>   - forward;    <D>   - back', 22, 500, 350, 0, 128, 128)
print_text('Car 2 : <Left> - forward;  <Right> - back', 22, 500, 375, 0, 128, 0)
draw_racing_lines()
x1 = x2 = 1050   # Start position Car 1, 2
draw_car(x1, 150, '1', 0, 128, 128)
draw_car(x2, 300, '2', 0, 128, 0)
pygame.display.update()
time.sleep(3)

# Countdown
A = ['3', '2', '1', 'GO!!!']
B = [500, 500, 500, 1000]
for n in range(len(A)):
    print_text(A[n], 52, 610, 150)
    pygame.display.update()
    time.sleep(0.5)
    winsound.Beep(B[n], B[n])
    pygame.draw.rect(screen, (0, 0, 0), (600, 135, 110, 60))

pygame.mixer.music.play(-1)

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            sys.exit()

    screen.fill(BLACK)
    print_text('Press <A>, <D> - car 1   <Left>, <Right> - car 2', 20, 470, 370)
    draw_racing_lines()
    draw_car(x1, 150, '1', 0, 128, 128)
    draw_car(x2, 300, '2', 0, 128, 0)
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if x1 > 150 and x2 > 150:
        if keys[pygame.K_a]:
            x1 -= randint(2, 5)
        elif keys[pygame.K_d]:
            x1 += 5

        if keys[pygame.K_LEFT]:
            x2 -= randint(2, 5)
        elif keys[pygame.K_RIGHT]:
            x2 += 5

    elif x1 <= 150 < x2:
        print_text('Car 1 - WINNER!!!', 36, 510, 150, 0, 128, 128)
        pygame.display.update()
        pygame.mixer.music.stop()
    elif x2 <= 150 < x1:
        print_text('Car 2 - WINNER!!!', 36, 510, 150, 0, 128, 0)
        pygame.display.update()
        pygame.mixer.music.stop()
    else:
        print_text('Draw - no winner', 36, 510, 150)
        pygame.display.update()
        pygame.mixer.music.stop()

    clock.tick(FPS)
