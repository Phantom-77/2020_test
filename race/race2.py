# This is the "Race 2.3" program, where 2 cars driven by two players
import pygame
import sys
import winsound
from random import randint

pygame.init()
pygame.mixer.init()

FPS = 30
SCREEN_SIZE = (1200, 400)
BLACK = (0, 0, 0)


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
    display_text('START', 36, 1020, 25)
    display_text('FINISH', 36, 90, 25)
    pygame.draw.line(screen, (255, 255, 255), [1010, 0], [1010, 400], 5)
    for y in range(0, 400, 20):
        sq1 = pygame.Rect((185, y, 10, 10))
        sq2 = pygame.Rect((195, y + 10, 10, 10))
        pygame.draw.rect(screen, (255, 255, 255), sq1)
        pygame.draw.rect(screen, (255, 255, 255), sq2)


def draw_finish_flag(x, y):
    """This function draws Finish Flag 120x60,
    (x,y) - flag center coordinates"""
    pygame.draw.rect(screen, (255, 255, 255), (x - 60, y - 30, 30, 30))
    pygame.draw.rect(screen, (255, 255, 255), (x - 30, y, 30, 30))
    pygame.draw.rect(screen, (255, 255, 255), (x, y - 30, 30, 30))
    pygame.draw.rect(screen, (255, 255, 255), (x + 30, y, 30, 30))
    pygame.draw.rect(screen, (255, 255, 255), (x - 61, y - 31, 122, 62), 1)
    pygame.display.update()


def display_text(content, f_size, x, y, r=255, g=255, b=255):
    """This function displays text:
    'content' - the text itself, f_size - the font size in pixels,
    (x,y) - the text coordinates, (RGB) - the text color,
    the default text color is white"""
    ft = pygame.font.Font(None, f_size)
    text = ft.render(content, True, (r, g, b))
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


def main_loop(start_position):
    c = []  # empty list for recording time leader
    x1 = x2 = start_position

    # Countdown before the start
    score = ['3', '2', '1', 'GO!']
    b = [500, 500, 500, 1000]
    for n in range(len(score)):
        display_text(score[n], 52, 590, 150)
        pygame.display.update()
        pygame.time.delay(500)
        winsound.Beep(b[n], b[n])
        pygame.draw.rect(screen, (0, 0, 0), (580, 135, 110, 60))
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
        display_text('Press <A>, <D> - car 1   <Left>, <Right> - car 2', 20, 460, 370)
        draw_racing_lines()
        draw_car(x1, 150, '1', 0, 128, 128)
        draw_car(x2, 300, '2', 0, 128, 0)
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
            display_text('#1 Car1   ' + convert_time(time_car1), 24, 525, 300, 0, 128, 128)
            display_text('#1 Car2   ' + convert_time(time_car2), 24, 525, 320, 0, 128, 0)
            pygame.display.update()
            game_over()
            finish = True

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
                display_text('Car 1 - WINNER!!!', 36, 490, 250, 0, 128, 128)
                display_text('#1 Car1   ' + convert_time(c[0]), 24, 525, 300, 0, 128, 128)
                display_text('#2 Car2   ' + convert_time(time_car2), 24, 525, 320, 0, 128, 0)
                pygame.display.update()
                game_over()
                finish = True

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
                display_text('Car 2 - WINNER!!!', 36, 490, 250, 0, 128, 0)
                display_text('#1 Car2   ' + convert_time(c[0]), 24, 525, 300, 0, 128, 0)
                display_text('#2 Car1   ' + convert_time(time_car1), 24, 525, 320, 0, 128, 128)
                pygame.display.update()
                game_over()
                finish = True


def game_over():
    """This function stops and unloads the music
    and displays 'Game over' with a delay"""
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.time.delay(5000)
    screen.fill(BLACK)
    display_text('GAME OVER', 36, 510, 150)
    pygame.display.update()
    pygame.time.delay(1000)


# Create window and load sound
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Race 2.3')
pygame.mixer.music.load('race2_sound.wav')
clock = pygame.time.Clock()

# Help to control car
display_text('Control :', 24, 585, 320)
display_text('Car 1 :  <A>   - forward;    <D>   - back', 22, 475, 350, 0, 128, 128)
display_text('Car 2 : <Left> - forward;  <Right> - back', 22, 470, 375, 0, 128, 0)

draw_racing_lines()
draw_car(1050, 150, '1', 0, 128, 128)
draw_car(1050, 300, '2', 0, 128, 0)
pygame.display.update()
pygame.time.delay(1500)
main_loop(1050)
