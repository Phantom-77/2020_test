# This is the "Race 3.1.0" program, where 2 cars driven by two players
import pygame
import sys
import random
from datetime import datetime

pygame.init()
pygame.mixer.init()

FPS = 30
WIDTH = 1280
HEIGHT = 420
xct = WIDTH / 2
yct = HEIGHT / 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (30, 144, 255)
GREEN = (0, 128, 0)


def convert_time(ticks):
    """
    This function converts the received
    milliseconds to time format MM:SS.mmm
    """
    millis = int(ticks % 1000)
    seconds = int((ticks/1000) % 60)
    minutes = int(ticks/(1000*60)) % 60
    # hours = int((ticks/(1000*60*60)) % 24a)
    res = '{min:02d}:{sec:02d}.{mil:03d}'.format(min=minutes, sec=seconds, mil=millis)
    return res


def display_text(content, f_size, x, y, color=WHITE):
    """
    This function displays text:
    'content' - the text itself, f_size - the font size in pixels,
    x, y - the text coordinates, color - the text color (rgb),
    the default text color is WHITE
    """
    ft = pygame.font.Font(None, f_size)
    text = ft.render(content, True, color)
    screen.blit(text, (int(x), int(y)))


def display_text_center(content, f_size, dx=0, dy=0, color=WHITE):
    """
    This function displays text on the center screen:
    'content' - the text itself, f_size - the font size in pixels,
    dx,dy - shift the coordinates of the text from the center,
    color - the text color (rgb), the default text color is WHITE
    """
    font = pygame.font.Font(None, f_size)
    text = font.render(content, True, color)
    text_rect = text.get_rect(center=(xct + dx, yct + dy))
    screen.blit(text, text_rect)


def draw_racing_lines():
    """
    This function draws lines START and FINISH
    """
    display_text('START', 36, WIDTH - 180, 25)
    display_text('FINISH', 36, 90, 25)
    pygame.draw.line(screen, WHITE, [WIDTH-190, 0], [WIDTH-190, HEIGHT], 5)
    for y in range(0, HEIGHT, 20):
        sq1 = pygame.Rect((185, y, 10, 10))
        sq2 = pygame.Rect((195, y + 10, 10, 10))
        pygame.draw.rect(screen, WHITE, sq1)
        pygame.draw.rect(screen, WHITE, sq2)


def start_screen():
    """
    This function shows start screen game
    """
    backdrop = pygame.image.load('img/menu.jpg').convert()
    backdrop_rect = backdrop.get_rect(center=(xct, yct))
    screen.blit(backdrop, backdrop_rect)
    display_text_center('RACE 3', 54, 0, -170, BLACK)
    display_text_center('SPACE - start race', 22, 0, -130, BLACK)
    display_text_center('Q - quit', 22, 0, -110, BLACK)
    display_text_center('P - statistics;  H - help in the controls cars', 22, 0, +185)
    pygame.display.update()


def statistics():
    """
    This function displays race results on the start screen
    """
    total = c1 = c2 = draw = 0
    try:
        with open('race3.1_result.txt', 'r') as file_handler:
            for line in file_handler:
                if 'Race result' in line:
                    total += 1
                if 'Win_Car1' in line:
                    c1 += 1
                if 'Win_Car2' in line:
                    c2 += 1
                if 'Draw' in line:
                    draw += 1
        shield = pygame.image.load('img/menu_s.png')
        shield_rect = shield.get_rect(center=(xct, yct + 90))
        screen.blit(shield, shield_rect)
        display_text('Total Races: ', 22, xct - 70, yct + 80, BLACK)
        display_text(str(total), 22, xct + 55, yct + 80, BLACK)
        display_text('Win Car1: ', 22, xct - 70, yct + 100, BLACK)
        display_text(str(c1), 22, xct + 55, yct + 100, BLACK)
        display_text('Win Car2: ', 22, xct - 70, yct + 120, BLACK)
        display_text(str(c2), 22, xct + 55, yct + 120, BLACK)
        display_text('Draw: ', 22, xct - 70, yct + 140, BLACK)
        display_text(str(draw), 22, xct + 55, yct + 140, BLACK)
        pygame.display.update()
        pygame.time.wait(2000)
    except IOError:
        display_text_center('Sorry, statistics are not available...', 22, 0, 0, RED)
        shield = pygame.image.load('img/sorry.png')
        shield_rect = shield.get_rect(center=(xct, yct + 90))
        screen.blit(shield, shield_rect)
        pygame.display.update()
        pygame.time.wait(2000)


def help_control():
    """
    This function shows cars control keys on the start screen
    """
    shield = pygame.image.load('img/shield1.png')
    shield_rect = shield.get_rect(center=(xct - 350, yct))
    screen.blit(shield, shield_rect)
    shield = pygame.image.load('img/shield2.png')
    shield_rect = shield.get_rect(center=(xct + 350, yct))
    screen.blit(shield, shield_rect)
    pygame.display.update()
    pygame.time.wait(2000)


def countdown():
    """
    This function counts down on the screen and beeps
    """
    pygame.mixer.music.stop()
    background = pygame.image.load('img/road.jpg').convert()
    background_rect = background.get_rect(center=(xct, yct))
    screen.blit(background, background_rect)
    draw_racing_lines()
    car1.rect.right = car2.rect.right = WIDTH
    all_sprites.draw(screen)
    pygame.display.update()
    pygame.mixer.music.load('sounds/start.wav')
    pygame.mixer.music.play()
    pygame.time.wait(6500)
    score = ['img/3.png', 'img/2.png', 'img/1.png', 'img/go.png']
    b = [1700, 1500, 1900, 1000]
    for n in range(len(score)):
        field = pygame.image.load(score[n])
        field_rect = field.get_rect(center=(xct, yct))
        screen.blit(field, field_rect)
        pygame.display.update()
        pygame.time.wait(b[n])


def race():
    """
    This function starts the race
    """
    c1 = []
    c2 = []
    pygame.mixer.music.load('sounds/sound.wav')
    pygame.mixer.music.play(-1)
    time_start = pygame.time.get_ticks()

    end = False
    while not end:
        clock.tick(FPS)
        for r in pygame.event.get():
            if r.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                sys.exit()

        all_sprites.update()

        # Rendering
        background = pygame.image.load('img/road.jpg').convert()
        background_rect = background.get_rect(center=(xct, yct))
        screen.blit(background, background_rect)
        display_text_center('Press R - for quit race', 22, 0, 180)
        draw_racing_lines()

        car1.speed_x = car2.speed_x = 0
        car1.speed_y = car2.speed_y = 0

        hits1 = pygame.sprite.spritecollide(car1, barriers, False)
        if hits1:
            sound1.play()
            car1.speed_x = 3
            car1.rect.x += car1.speed_x
        hits2 = pygame.sprite.spritecollide(car2, barriers, False)
        if hits2:
            sound1.play()
            car2.speed_x = 3
            car2.rect.x += car2.speed_x

        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_r]:
            end = True

        if key_state[pygame.K_w]:
            car1.speed_x = -5
        if key_state[pygame.K_s]:
            car1.speed_x = 5
        if key_state[pygame.K_d]:
            car1.speed_y = -3
        if key_state[pygame.K_a]:
            car1.speed_y = 3
        car1.rect.x += car1.speed_x
        car1.rect.y += car1.speed_y

        if key_state[pygame.K_LEFT]:
            car2.speed_x = -5
        if key_state[pygame.K_RIGHT]:
            car2.speed_x = 5
        if key_state[pygame.K_UP]:
            car2.speed_y = -3
        if key_state[pygame.K_DOWN]:
            car2.speed_y = 3
        car2.rect.x += car2.speed_x
        car2.rect.y += car2.speed_y

        if car1.rect.left <= 50:
            time_car1 = pygame.time.get_ticks() - time_start
            c1.append(time_car1)
            sp1 = len(c1)
            if sp1 >= 2:
                del c1[1]
            flag = pygame.image.load('img/finish_flag.png')
            flag_rect = flag.get_rect(center=(xct, yct))
            screen.blit(flag, flag_rect)

        if car2.rect.left <= 50:
            time_car2 = pygame.time.get_ticks() - time_start
            c2.append(time_car2)
            sp2 = len(c2)
            if sp2 >= 2:
                del c2[1]
            flag = pygame.image.load('img/finish_flag.png')
            flag_rect = flag.get_rect(center=(xct, yct))
            screen.blit(flag, flag_rect)

        if car1.rect.left <= 10 and car2.rect.left <= 10:
            result(c1[0], c2[0])
            end = True

        all_sprites.draw(screen)
        pygame.display.flip()


def result(time_car1, time_car2):
    """
    This function determines the winner of the race
    by comparing the time Car1 and Car2
    """
    t1 = time_car1
    t2 = time_car2
    tc1 = convert_time(t1)
    tc2 = convert_time(t2)

    background = pygame.image.load('img/road1.jpg').convert()
    background_rect = background.get_rect(center=(xct, yct))
    screen.blit(background, background_rect)
    pygame.mixer.music.load('sounds/win.wav')
    pygame.mixer.music.play(-1)

    if t1 < t2:
        shield = pygame.image.load('img/win1.png')
        shield_rect = shield.get_rect(center=(xct, yct-30))
        screen.blit(shield, shield_rect)
        display_text('Win Car 1', 24, xct-45, yct+80, BLUE)
        display_text('1 place - Car1  ' + tc1, 24, xct-100, yct+100, BLUE)
        display_text('2 place - Car2  ' + tc2, 24, xct-100, yct+120, GREEN)
        pygame.display.update()
        result_rec('Win_Car1', tc1, tc2, 'Car1', 'Car2')
    elif t1 > t2:
        shield = pygame.image.load('img/win2.png')
        shield_rect = shield.get_rect(center=(xct, yct-30))
        screen.blit(shield, shield_rect)
        display_text('Win Car 2', 24, xct-45, yct+80, GREEN)
        display_text('1 place - Car2  ' + tc2, 24, xct-100, yct+100, GREEN)
        display_text('2 place - Car1  ' + tc1, 24, xct-100, yct+120, BLUE)
        pygame.display.update()
        result_rec('Win_Car2', tc2, tc1, 'Car2', 'Car1')
    else:
        display_text('Draw', 24, xct-20, yct+60)
        display_text('Car1  ' + tc1, 24, xct-60, yct+100, BLUE)
        display_text('Car2  ' + tc2, 24, xct-60, yct+120, GREEN)
        pygame.display.update()
        result_rec('Draw', tc1, tc2)
    pygame.time.wait(4500)


def result_rec(win, t1, t2, first=' ', second=' '):
    """
    This function writes the race result
    to a file race3.1_result.txt
    """
    date = datetime.now()
    file = open('race3.1_result.txt', 'a', -1, 'utf-8')
    file.write(str(date) + '\n')
    file.write('Race result: ' + win + '\n')
    file.write('1 place: ' + t1 + ' - ' + first + '\n')
    file.write('2 place: ' + t2 + ' - ' + second + '\n')
    file.write('#\n')
    file.close()


class Player(pygame.sprite.Sprite):
    def __init__(self, name, image, pos=0):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT / 2 + pos
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


class Barrier(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(190, 1000)
        self.rect.y = random.choice([-50, 420])
        self.speed_y = random.randrange(-3, 4)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom > HEIGHT + 60 or self.rect.top < -60:
            self.rect.x = random.randrange(190, 1000)
            self.rect.y = random.choice([-50, 420])
            self.speed_y = random.randrange(-3, 4)


# Create window, load music and sounds
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Race 3.1')
clock = pygame.time.Clock()
pygame.mixer.music.load('sounds/menu.wav')
pygame.mixer.music.play(-1)

sound1 = pygame.mixer.Sound('sounds/pf-f-f.wav')

car1_img = pygame.image.load('img/car1.png')
car2_img = pygame.image.load('img/car2.png')
barrier_img = pygame.image.load('img/barrier.png')

all_sprites = pygame.sprite.Group()
barriers = pygame.sprite.Group()
car1 = Player('Car1', car1_img, -50)
car2 = Player('Car2', car2_img, +125)
all_sprites.add(car1, car2)
for i in range(7):
    let = Barrier(barrier_img)
    all_sprites.add(let)
    barriers.add(let)

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
        countdown()
        race()
        car1.rect.bottom = HEIGHT / 2 - 50
        car2.rect.bottom = HEIGHT / 2 + 125
        pygame.mixer.music.load('sounds/menu.wav')
        pygame.mixer.music.play(-1)
        start_screen()
    if keys[pygame.K_p]:
        statistics()
    if keys[pygame.K_h]:
        help_control()
    if keys[pygame.K_q]:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        exiting = pygame.image.load('img/exit.png')
        exiting_rect = exiting.get_rect(center=(xct, yct))
        screen.blit(exiting, exiting_rect)
        pygame.display.update()
        pygame.time.wait(300)
        finish = True
pygame.quit()
