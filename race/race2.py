# This is the "Race 2.3.1" program, where 2 cars driven by two players
import pygame
import sys
import winsound
from datetime import datetime
from random import randint

pygame.init()
pygame.mixer.init()

FPS = 30
SCREEN_SIZE = (1200, 400)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TEAL = (0, 128, 128)
GREEN = (0, 128, 0)


def draw_car(x, y, number, color=WHITE):
    """This function draws car in coordinates (x,y)
    with number (number) and color (RGB),
    the default car color is white,
    start coordinate (x,y) - left wheel axis"""
    # Body car
    pygame.draw.rect(screen, color, (x - 30, y - 30, 160, 30))
    pygame.draw.polygon(screen, color, [(x, y - 30), (x + 30, y - 60),
                                        (x + 70, y - 60), (x + 100, y - 30)])
    pygame.draw.polygon(screen, (173, 216, 230), [(x + 10, y - 35), (x + 30, y - 55),
                                                  (x + 55, y - 55), (x + 55, y - 35)])
    pygame.draw.polygon(screen, (173, 216, 230), [(x + 60, y - 35), (x + 60, y - 55),
                                                  (x + 70, y - 55), (x + 85, y - 35)])
    # Headlights and stop signal
    pygame.draw.rect(screen, WHITE, (x - 30, y - 25, 10, 5))
    pygame.draw.rect(screen, BLACK, (x - 30, y - 25, 10, 5), 1)
    pygame.draw.rect(screen, (255, 0, 0), (x + 120, y - 25, 10, 10))
    pygame.draw.rect(screen, BLACK, (x + 120, y - 25, 10, 10), 1)
    # Wheel left
    pygame.draw.circle(screen, (47, 79, 79), (x, y), 20, 8)
    pygame.draw.circle(screen, (176, 196, 222), (x, y), 12, 10)
    pygame.draw.circle(screen, BLACK, (x, y), 20, 2)
    pygame.draw.circle(screen, BLACK, (x, y), 4)
    # Wheel right
    pygame.draw.circle(screen, (47, 79, 79), (x + 100, y), 20, 8)
    pygame.draw.circle(screen, (176, 196, 222), (x + 100, y), 12, 10)
    pygame.draw.circle(screen, BLACK, (x + 100, y), 20, 2)
    pygame.draw.circle(screen, BLACK, (x + 100, y), 4)
    display_text(number, 36, x + 45, y - 28, BLACK)


def draw_racing_lines():
    """This function draws lines START & FINISH"""
    display_text('START', 36, 1020, 25)
    display_text('FINISH', 36, 90, 25)
    pygame.draw.line(screen, WHITE, [1010, 0], [1010, 400], 5)
    for y in range(0, 400, 20):
        sq1 = pygame.Rect((185, y, 10, 10))
        sq2 = pygame.Rect((195, y + 10, 10, 10))
        pygame.draw.rect(screen, WHITE, sq1)
        pygame.draw.rect(screen, WHITE, sq2)


def draw_finish_flag(x, y):
    """This function draws Finish Flag 120x60,
    (x,y) - flag center coordinates"""
    pygame.draw.rect(screen, WHITE, (x - 60, y - 30, 30, 30))
    pygame.draw.rect(screen, WHITE, (x - 30, y, 30, 30))
    pygame.draw.rect(screen, WHITE, (x, y - 30, 30, 30))
    pygame.draw.rect(screen, WHITE, (x + 30, y, 30, 30))
    pygame.draw.rect(screen, WHITE, (x - 61, y - 31, 122, 62), 1)
    pygame.display.update()


def display_text(content, f_size, x, y, color=WHITE):
    """This function displays text:
    'content' - the text itself, f_size - the font size in pixels,
    (x,y) - the text coordinates, (RGB) - the text color,
    the default text color is white"""
    ft = pygame.font.Font(None, f_size)
    text = ft.render(content, True, color)
    screen.blit(text, (x, y))


def convert_time(ticks):
    """This function converts the received
    milliseconds to time format MM:SS.mmm"""
    millis = int(ticks % 1000)
    seconds = int((ticks/1000) % 60)
    minutes = int(ticks/(1000*60)) % 60
    # hours = int((ticks/(1000*60*60)) % 24a)
    result = '{min:02d}:{sec:02d}.{mil:03d}'.format(min=minutes, sec=seconds, mil=millis)
    return result


def countdown():
    """This function counts down on the screen and beeps"""
    score = ['3', '2', '1', 'GO!']
    b = [500, 500, 500, 1000]
    for n in range(len(score)):
        display_text(score[n], 52, 590, 150)
        pygame.display.update()
        pygame.time.delay(500)
        winsound.Beep(b[n], b[n])
        pygame.draw.rect(screen, BLACK, (580, 135, 110, 60))


def show_help_control():
    """This function shows on-screen help in control"""
    display_text('Control :', 24, 850, 50)
    display_text('Car 1 :', 22, 850, 90, TEAL)
    display_text('A - forward', 22, 850, 110, TEAL)
    display_text('D - back', 22, 850, 130, TEAL)
    display_text('Car 2 :', 22, 850, 240, GREEN)
    display_text('Left - forward', 22, 850, 260, GREEN)
    display_text('Right - back', 22, 850, 280, GREEN)
    draw_racing_lines()
    draw_car(1050, 150, '1', TEAL)
    draw_car(1050, 300, '2', GREEN)
    pygame.display.update()
    pygame.time.wait(1500)


def game_over():
    """This function stops and unloads the music
    and return end=True"""
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.time.wait(3000)
    screen.fill(BLACK)
    display_text('GAME OVER', 36, 520, 170)
    pygame.display.update()
    end = True
    return end


def print_result(winner, time_1st, time_2nd, first=' ', second=' '):
    date = datetime.now()
    file = open('race2_result.txt', 'a', -1, 'utf-8')
    file.write(str(date) + '\n')
    file.write(' Race result: ' + winner + '\n')
    file.write('1 place: ' + convert_time(time_1st) + ' - ' + first + '\n')
    file.write('2 place: ' + convert_time(time_2nd) + ' - ' + second + '\n')
    file.write('----------\n')
    file.close()


def main_loop():
    c = []  # empty list for recording time leader
    x1 = x2 = 1050  # Start position
    pygame.mixer.music.play(-1)
    time_start = pygame.time.get_ticks()
    finish = False
    while not finish:
        clock.tick(FPS)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                sys.exit()

        screen.fill(BLACK)
        draw_racing_lines()
        draw_car(x1, 150, '1', TEAL)
        draw_car(x2, 300, '2', GREEN)
        pygame.display.update()

        keys = pygame.key.get_pressed()

        if x1 > 50 and x2 > 50:
            if keys[pygame.K_a]:
                x1 -= randint(2, 5)
            elif keys[pygame.K_d]:
                x1 += 5

            if keys[pygame.K_LEFT]:
                x2 -= randint(2, 5)
            elif keys[pygame.K_RIGHT]:
                x2 += 5

        elif x1 <= 50 and x2 <= 50:
            x1 = x2 = 50
            time_car1 = pygame.time.get_ticks() - time_start
            time_car2 = pygame.time.get_ticks() - time_start
            draw_finish_flag(600, 200)
            display_text('Draw - no winner', 36, 490, 250)
            display_text('1 - Car1   ' + convert_time(time_car1), 24, 525, 300, TEAL)
            display_text('1 - Car2   ' + convert_time(time_car2), 24, 525, 320, GREEN)
            pygame.display.update()
            print_result('Draw - no winner', time_car1, time_car2)
            game_over()
            finish = game_over()

        elif x1 <= 50 < x2:
            x1 = 50
            time_car1 = pygame.time.get_ticks() - time_start
            draw_finish_flag(600, 200)
            c.append(time_car1)
            sp1 = len(c)
            if sp1 >= 2:
                del c[1]

            if keys[pygame.K_LEFT]:
                x2 -= randint(2, 5)
            elif keys[pygame.K_RIGHT]:
                x2 += 5

            if x2 <= 50:
                x2 = 50
                time_car2 = pygame.time.get_ticks() - time_start
                display_text('Car 1 - WINNER!!!', 36, 490, 250, TEAL)
                display_text('1 - Car1   ' + convert_time(c[0]), 24, 525, 300, TEAL)
                display_text('2 - Car2   ' + convert_time(time_car2), 24, 525, 320, GREEN)
                pygame.display.update()
                print_result('Car 1 - win!', c[0], time_car2, 'Car1', 'Car2')
                game_over()
                finish = game_over()

        elif x2 <= 50 < x1:
            x2 = 50
            time_car2 = pygame.time.get_ticks() - time_start
            draw_finish_flag(600, 200)
            c.append(time_car2)
            sp2 = len(c)
            if sp2 >= 2:
                del c[1]

            if keys[pygame.K_a]:
                x1 -= randint(2, 5)
            elif keys[pygame.K_d]:
                x1 += 5

            if x1 <= 50:
                x1 = 50
                time_car1 = pygame.time.get_ticks() - time_start
                display_text('Car 2 - WINNER!!!', 36, 490, 250, GREEN)
                display_text('1 - Car2   ' + convert_time(c[0]), 24, 525, 300, GREEN)
                display_text('2 - Car1   ' + convert_time(time_car1), 24, 525, 320, TEAL)
                pygame.display.update()
                print_result('Car 2 - win!', c[0], time_car1, 'Car2', 'Car1')
                game_over()
                finish = game_over()


# Create window and load sound
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Race 2.3.1')
pygame.mixer.music.load('race2_sound.wav')
clock = pygame.time.Clock()

show_help_control()
countdown()
main_loop()
