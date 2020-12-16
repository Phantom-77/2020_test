# This is the "Race 2.2.14" program, where 2 cars driven by two players
# Не решенная проблема - время финишировавшего первым автомобиля перезаписывается циклом
# пока не финиширует второй авто. Как дикий вариант - создать кортеж значений и потом выдергивать
# нулевой элемент кортежа A=(1, 2, 3, 4, 5), A[0] == 1
import pygame
import sys
import winsound
from random import randint

pygame.init()
pygame.mixer.init()


def draw_car(x, y, number, r=255, g=255, b=255):
    """This function draws car in coordinates (x,y)
    with number (number) and color (RGB),
    the default car color is white,
    start coordinate (x,y) - left wheel axis"""
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
    display_text(number, 36, x + 45, y - 28, 0, 0, 0)


def draw_racing_lines():
    """This function draws lines START & FINISH"""
    display_text('START', 36, 1010, 25)
    display_text('FINISH', 36, 100, 25)
    pygame.draw.line(screen, (255, 255, 255), [1000, 0], [1000, 400], 5)
    for y in range(0, 400, 20):
        sq1 = pygame.Rect((195, y, 10, 10))
        sq2 = pygame.Rect((205, y + 10, 10, 10))
        pygame.draw.rect(screen, (255, 255, 255), sq1)
        pygame.draw.rect(screen, (255, 255, 255), sq2)


def display_text(content, f_size, x, y, r=255, g=255, b=255):
    """This function displays text:
    'content' - the text itself, f_size - the font size in pixels,
    (x,y) - the text coordinates, (RGB) - the text color,
    the default text color is white"""
    ft = pygame.font.Font(None, f_size)
    text = ft.render(content, True, (r, g, b))
    screen.blit(text, (x, y))


def game_over():
    pygame.mixer.music.stop()
    pygame.time.delay(5000)
    screen.fill(BLACK)
    display_text('GAME OVER', 36, 510, 150)
    pygame.display.update()
    pygame.time.delay(1000)


def convert_time(ms):
    """This function converts the received
    milliseconds to time format MM:SS.mmm"""
    ms = int(ms)
    millis = ms % 1000
    millis = int(millis)
    seconds = (ms/1000) % 60
    seconds = int(seconds)
    minutes = (ms/(1000*60)) % 60
    minutes = int(minutes)
    # hours = (ms/(1000*60*60)) % 24
    # result = ("%d:%d:%d.%d" % (hours, minutes, seconds, millis))
    result = ("%d:%d.%d" % (minutes, seconds, millis))
    return result


FPS = 30
SIZE = (1200, 400)
BLACK = (0, 0, 0)

# Create window and load sound
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('Race 2.2.14')
pygame.mixer.music.load('car_sound.wav')

display_text('Press the button to control the Car :', 22, 490, 325)
display_text('Car 1 :  <A>   - forward;    <D>   - back', 22, 485, 350, 0, 128, 128)
display_text('Car 2 : <Left> - forward;  <Right> - back', 22, 480, 375, 0, 128, 0)
draw_racing_lines()
x1 = x2 = 1050   # Start position Car 1, 2
draw_car(x1, 150, '1', 0, 128, 128)
draw_car(x2, 300, '2', 0, 128, 0)
pygame.display.update()
pygame.time.delay(1500)

# Countdown
A = ['3', '2', '1', 'GO!!!']
B = [500, 500, 500, 1000]
for n in range(len(A)):
    display_text(A[n], 52, 610, 150)
    pygame.display.update()
    pygame.time.delay(500)
    winsound.Beep(B[n], B[n])
    pygame.draw.rect(screen, (0, 0, 0), (600, 135, 110, 60))

pygame.mixer.music.play(-1)
time_start = pygame.time.get_ticks()

finish = False
while not finish:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            sys.exit()

    screen.fill(BLACK)
    display_text('Press <A>, <D> - car 1   <Left>, <Right> - car 2', 20, 470, 370)
    draw_racing_lines()
    draw_car(x1, 150, '1', 0, 128, 128)
    draw_car(x2, 300, '2', 0, 128, 0)
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if x1 > 60 and x2 > 60:
        if keys[pygame.K_a]:
            x1 -= randint(2, 5)
        elif keys[pygame.K_d]:
            x1 += 5

        if keys[pygame.K_LEFT]:
            x2 -= randint(2, 5)
        elif keys[pygame.K_RIGHT]:
            x2 += 5

    elif x1 <= 60 and x2 <= 60:
        x1 = 60
        x2 = 60
        time_car1 = pygame.time.get_ticks() - time_start
        time_car2 = pygame.time.get_ticks() - time_start
        display_text('Draw - no winner', 36, 510, 150)
        display_text('#1 Car1   ' + convert_time(time_car1), 24, 545, 200, 0, 128, 128)
        display_text('#1 Car2   ' + convert_time(time_car2), 24, 545, 220, 0, 128, 0)
        pygame.display.update()
        game_over()
        finish = True

    elif x1 <= 60 and x2 > 60:
        x1 = 60
        time_car1 = pygame.time.get_ticks() - time_start
        print('Start-' + str(time_start), '1-' + str(time_car1))
        if keys[pygame.K_LEFT]:
            x2 -= randint(2, 5)
        elif keys[pygame.K_RIGHT]:
            x2 += 5
        if x2 <= 60:
            x2 = 60
            time_car2 = pygame.time.get_ticks() - time_start
            print('Start-' + str(time_start), '2-' + str(time_car2))
            display_text('Car 1 - WINNER!!!', 36, 520, 150, 0, 128, 128)
            display_text('#1 Car1   ' + convert_time(time_car1), 24, 545, 200, 0, 128, 128)
            display_text('#2 Car2   ' + convert_time(time_car2), 24, 545, 220, 0, 128, 0)
            pygame.display.update()
            game_over()
            finish = True

    elif x2 <= 60 and x1 > 60:
        x2 = 60
        time_car2 = pygame.time.get_ticks() - time_start
        print('Start-' + str(time_start), '2-' + str(time_car2))
        if keys[pygame.K_a]:
            x1 -= randint(2, 5)
        elif keys[pygame.K_d]:
            x1 += 5
        if x1 <= 60:
            x1 = 60
            time_car1 = pygame.time.get_ticks() - time_start
            print('Start-' + str(time_start), '1-' + str(time_car1))
            display_text('Car 2 - WINNER!!!', 36, 520, 150, 0, 128, 0)
            display_text('#1 Car2   ' + convert_time(time_car2), 24, 545, 200, 0, 128, 0)
            display_text('#2 Car1   ' + convert_time(time_car1), 24, 545, 220, 0, 128, 128)
            pygame.display.update()
            game_over()
            finish = True

    clock.tick(FPS)
