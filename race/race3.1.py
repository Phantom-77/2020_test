# This is the "Race 3.1.0" program, where 2 cars driven by two players
import pygame
# import os
import sys
import winsound
from datetime import datetime
# from random import randint

FPS = 30
WIDTH = 1280
HEIGHT = 420
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (30, 144, 255)
GREEN = (0, 128, 0)


def convert_time(ticks):
    """This function converts the received
    milliseconds to time format MM:SS.mmm"""
    millis = int(ticks % 1000)
    seconds = int((ticks/1000) % 60)
    minutes = int(ticks/(1000*60)) % 60
    # hours = int((ticks/(1000*60*60)) % 24a)
    res = '{min:02d}:{sec:02d}.{mil:03d}'.format(min=minutes, sec=seconds, mil=millis)
    return res


def countdown():
    """This function counts down on the screen and beeps"""
    pygame.mixer.music.stop()
    bg_img = pygame.image.load('img/road.jpg').convert()
    bg_img_rect = bg_img.get_rect(center=(xct, yct))
    screen.blit(bg_img, bg_img_rect)
    draw_racing_lines()
    # draw_car(WIDTH-150, yct-50, '1', BLUE)
    # draw_car(WIDTH-150, yct+100, '2', GREEN)
    pygame.display.update()
    pygame.mixer.music.load('sounds/start.wav')
    pygame.mixer.music.play()
    pygame.time.wait(2000)
    score = ['3', '2', '1', 'GO!']
    b = [500, 500, 500, 1000]
    for n in range(len(score)):
        display_text_center(score[n], 52)
        pygame.display.update()
        pygame.time.wait(500)
        winsound.Beep(b[n], b[n])
        bg_img = pygame.image.load('img/road_cr.jpg').convert()
        bg_img_rect = bg_img.get_rect(center=(xct, yct))
        screen.blit(bg_img, bg_img_rect)


def display_text(content, f_size, x, y, color=WHITE):
    """This function displays text:
    'content' - the text itself, f_size - the font size in pixels,
    (x,y) - the text coordinates, (RGB) - the text color,
    the default text color is white"""
    ft = pygame.font.Font(None, f_size)
    text = ft.render(content, True, color)
    screen.blit(text, (int(x), int(y)))


def display_text_center(content, f_size, dx=0, dy=0, color=WHITE):
    """This function displays text on the center screen:
    'content' - the text itself, f_size - the font size in pixels,
    dx,dy - shift the coordinates of the text from the center,
    (RGB) - the text color, the default text color is WHITE"""
    font = pygame.font.Font(None, f_size)
    text = font.render(content, True, color)
    text_rect = text.get_rect(center=(xct + dx, yct + dy))
    screen.blit(text, text_rect)


def draw_racing_lines():
    """This function draws lines START & FINISH"""
    display_text('START', 36, WIDTH - 180, 25)
    display_text('FINISH', 36, 90, 25)
    pygame.draw.line(screen, WHITE, [WIDTH-190, 0], [WIDTH-190, HEIGHT], 5)
    for y in range(0, HEIGHT, 20):
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


def race():
    """This function starts the race"""
    # c1 = []  # empty list for recording time car1
    # c2 = []  # empty list for recording time car2
    # x1 = x2 = WIDTH - 150  # Start position
    pygame.mixer.music.load('sounds/sound.wav')
    pygame.mixer.music.play(-1)
    # time_start = pygame.time.get_ticks()
    end = False
    while not end:
        clock.tick(FPS)
        for r in pygame.event.get():
            if r.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                sys.exit()

        # screen.fill(BLACK)
        # Обновление
        all_sprites.update()

        # Рендеринг
        bg_img = pygame.image.load('img/road.jpg').convert()
        bg_img_rect = bg_img.get_rect(center=(xct, yct))
        screen.blit(bg_img, bg_img_rect)
        draw_racing_lines()
        all_sprites.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()


def result(time_car1, time_car2):
    """This function determines the winner of the race
    by comparing the time Car1 and Car2"""
    t1 = time_car1
    t2 = time_car2
    tc1 = convert_time(t1)
    tc2 = convert_time(t2)
    if t1 < t2:
        display_text('Win Car 1', 24, xct-45, yct+60, BLUE)
        display_text('1 place - Car1  ' + tc1, 24, xct-100, yct+100, BLUE)
        display_text('2 place - Car2  ' + tc2, 24, xct-100, yct+120, GREEN)
        pygame.display.update()
        result_recording('Win_Car1', tc1, tc2, 'Car1', 'Car2')
    elif t1 > t2:
        display_text('Win Car 2', 24, xct-45, yct+60, GREEN)
        display_text('1 place - Car2  ' + tc2, 24, xct-100, yct+100, GREEN)
        display_text('2 place - Car1  ' + tc1, 24, xct-100, yct+120, BLUE)
        pygame.display.update()
        result_recording('Win_Car2', tc2, tc1, 'Car2', 'Car1')
    else:
        display_text('Draw', 24, xct-20, yct+60)
        display_text('Car1  ' + tc1, 24, xct-60, yct+100, BLUE)
        display_text('Car2  ' + tc2, 24, xct-60, yct+120, GREEN)
        pygame.display.update()
        result_recording('Draw', tc1, tc2)


def result_recording(win, t1, t2, first=' ', second=' '):
    """This function writes the race result
    to a file race3_result.txt"""
    date = datetime.now()
    file = open('race3_result.txt', 'a', -1, 'utf-8')
    file.write(str(date) + '\n')
    file.write('Race result: ' + win + '\n')
    file.write('1 place: ' + t1 + ' - ' + first + '\n')
    file.write('2 place: ' + t2 + ' - ' + second + '\n')
    file.write('#\n')
    file.close()


def start_screen():
    """This function shows on-screen help in control"""
    screen.fill(BLACK)
    bg_img = pygame.image.load('img/menu.jpg').convert()
    bg_img_rect = bg_img.get_rect(center=(xct, yct))
    screen.blit(bg_img, bg_img_rect)
    display_text_center('RACE 3', 54, 0, -180)
    display_text_center('Press SPACE - for start race', 22, 0, -140)
    display_text_center('Press Q - for quit game', 22, 0, -120)
    display_text_center('Press P - to view statistics', 22, 0, -100)
    display_text('Car 1 :', 22, xct-350, yct-110, BLUE)
    display_text('A - forward', 22, xct-350, yct-90, BLUE)
    display_text('D - back', 22, xct-350, yct-70, BLUE)
    display_text('Car 2 :', 22, xct+300, yct-110, GREEN)
    display_text('Left - forward', 22, xct+300, yct-90, GREEN)
    display_text('Right - back', 22, xct+300, yct-70, GREEN)
    pygame.display.update()


def statistics():
    """This function displays race results
    statistics on the start screen"""
    total = c1 = c2 = draw = 0
    try:
        with open('race3_result.txt', 'r') as file_handler:
            for line in file_handler:
                if 'Race result' in line:
                    total += 1
                if 'Win_Car1' in line:
                    c1 += 1
                if 'Win_Car2' in line:
                    c2 += 1
                if 'Draw' in line:
                    draw += 1
    except IOError:
        display_text_center('Sorry, statistics are not available...', 22, 0, 0, RED)
    bg_img = pygame.image.load('img/menu_s.jpg').convert()
    bg_img_rect = bg_img.get_rect(center=(xct, yct+90))
    screen.blit(bg_img, bg_img_rect)
    display_text('Total Races: ', 22, xct-70, yct+80, BLACK)
    display_text(str(total), 22, xct+55, yct+80, BLACK)
    display_text('Win Car1: ', 22, xct-70, yct+100, BLUE)
    display_text(str(c1), 22, xct+55, yct+100, BLUE)
    display_text('Win Car2: ', 22, xct-70, yct+120, GREEN)
    display_text(str(c2), 22, xct+55, yct+120, GREEN)
    display_text('Draw: ', 22, xct-70, yct+140, BLACK)
    display_text(str(draw), 22, xct+55, yct+140, BLACK)
    pygame.display.update()
    pygame.time.wait(2000)


# Create window and load sound
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Race 3.1')
clock = pygame.time.Clock()
pygame.mixer.music.load('sounds/menu.wav')
pygame.mixer.music.play(-1)
xct = WIDTH / 2
yct = HEIGHT / 2

player_img = pygame.image.load('img/car1.jpg').convert()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT / 2 - 50
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


all_sprites = pygame.sprite.Group()
car1 = Player()
car2 = Player()
all_sprites.add(car1)
all_sprites.add(car2)

# Main loop
finish = False
while not finish:
    clock.tick(FPS)
    start_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        screen.fill(BLACK)
        countdown()
        race()
        pygame.mixer.music.load('sounds/menu.wav')
        pygame.mixer.music.play(-1)
        start_screen()
    if keys[pygame.K_p]:
        statistics()
    if keys[pygame.K_q]:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        finish = True
pygame.quit()
