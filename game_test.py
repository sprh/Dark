import pygame
import time
import threading
import random
import math
import os
from pygame.locals import *
from pygame.math import Vector2
NUM = 0


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


def init_window():
    # инициализация окна
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Game')


def ACTION():
    # начало игры
    NUM = True
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    # Установление шрифта
    font = pygame.font.SysFont('fixedsys', 40)
    text = font.render('Press any key to start', True, (222, 218, 144))
    # Увеличение шрифта
    font = pygame.font.SysFont('fixedsys', 80)
    text1 = font.render('"Can you manage the', True, (250, 238, 231))
    font = pygame.font.SysFont('fixedsys', 120)
    text2 = font.render('DARK?"', True, (255, 255, 255))
    sec = 0
    fl = True
    while NUM:
        screen.fill((0, 0, 0))
        # Задержка. Сделана для того, чтоб изображать мигание света (включение/выключение лампы)
        time.sleep(0.5)
        # После задержки увеличиваем на 1 переменную sec
        sec += 1
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    NUM = False
                else:
                    NUM = False
                    screen.fill((0, 0, 0))
                    HISTORY()
            elif event.type == QUIT:
                NUM = False
        # смотрим, сключена или выключена лампа (все зависит от переменной sec
        if sec % 4 == 0 or sec == 0:
            fl = False
        elif sec % 2 == 0:
            fl = True
        # Рисуется линия + прямоугольник -- основание лампы
        pygame.draw.line(screen, (255, 255, 255), [300, 0], [300, 250], 5)
        pygame.draw.rect(screen, (255, 255, 255), (275, 250, 50, 15))
        if fl:
            # Если лампа выключена (эллипс снизу - изображение свечения
            pygame.draw.circle(screen, (222, 218, 144), (300, 500), 50)
            pygame.draw.ellipse(screen, (217, 211, 189), (160, 700, 280, 70))
        else:
            # Если лампа выключена
            pygame.draw.circle(screen, (255, 255, 255), (300, 500), 50, 5)
            pygame.draw.ellipse(screen, (0, 0, 0), (160, 700, 280, 70))
        pygame.draw.rect(screen, (0, 0, 0), (250, 450, 100, 50))
        pygame.draw.polygon(screen, (255, 255, 255), [(300, 250), (175, 500), (425, 500)], 5)
        # Вывод текста
        screen.blit(text, [700, 800])
        screen.blit(text1, [400, 200])
        screen.blit(text2, [650, 280])
        pygame.display.flip()


# 2 часть вступления. История героя
def HISTORY():
    # загрузка звука печатания на клавиатуре
    pygame.mixer.music.load('keyboard.mp3')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    running = True
    # установление шрифта
    font = pygame.font.SysFont('monaco', 34)
    # История. Первые строки сложно прочитать, они пропадают практически сразу же
    # (сделано специально!)
    mas = 'Albert Einstein said that darkness does not exist.'
    mas_true = ['Darkness is merely the absence of light.', ' ',
                'I disagree.', ' ',
                'I know that darkness exists. I have lived with it.',
                'And in it.',
                ' ', 'I know what darkness is.', ' ',
                'I know how darkness feels. I know its blindness.', ' ',
                'I know its aloneness. I know its eerie silence.', ' ',
                'It exists. I can say that as an absolute fact.', ' ',
                'Nothing exists without its opposite.',
                'The yin does not come without the yang. '
                ]
    texts = ['Albert Einstein said that darkness does not exist.'] + mas_true
    coord = [520, 240]
    st = ''
    fl = True
    # запуск звуковой дорожки. параметр -1 означает, что воспроизводится она бесконечное количество
    # раз
    pygame.mixer.music.play(-1, 0.0)
    # Установление громкости
    pygame.mixer.music.set_volume(0.1)
    while running:
        if len(st) != len(mas):
            st += mas[len(st)]
            time.sleep(0.05)
        # Текст
        text = font.render(st, True, (0, 0, 0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                else:
                    # Если после того, как вся истрия появилась, игрок нажимает на любую кнопку,
                    #  он переходит к началу игры
                    if not fl and len(mas_true) == 0 and len(st) == len(mas):
                        # Переход к рассказу персонажа о свете
                        screen.fill((0, 0, 0))
                        HISTORY_CONTINUED()
            elif event.type == QUIT:
                running = False
        if len(mas_true) == 0 and len(st) == len(mas):
            # Остановка музыки
            pygame.mixer.music.stop()
            time.sleep(0.5)
            screen.fill((0, 0, 0))
            fl = False
            # Все рисуется заново. Лампа выключается, тот же текст появляется на черном фоне -->
            # у игрока появляется возможность прочитать
            pygame.draw.line(screen, (255, 255, 255), [300, 0], [300, 250], 5)
            pygame.draw.rect(screen, (255, 255, 255), (275, 250, 50, 15))
            pygame.draw.circle(screen, (255, 255, 255), (300, 500), 50, 5)
            pygame.draw.ellipse(screen, (0, 0, 0), (160, 700, 280, 70))
            pygame.draw.rect(screen, (0, 0, 0), (250, 450, 100, 49))
            pygame.draw.rect(screen, (255, 255, 255), (500, 200, 600, 600), 5)
            pygame.draw.polygon(screen, (255, 255, 255), [(300, 250), (175, 500), (425, 500)], 5)
            for i in range(len(texts)):
                text = font.render(texts[i], True, (255, 255, 255))
                screen.blit(text, [520, 240 + 30 * i])
            pygame.display.flip()
            time.sleep(1)
            font1 = pygame.font.SysFont('fixedsys', 35)
            text = font1.render('Press any key to resume', True, (222, 218, 144))
            screen.blit(text, [900, 50])
        elif fl:
            # Рисуется лампа
            pygame.draw.line(screen, (255, 255, 255), [300, 0], [300, 250], 5)
            pygame.draw.rect(screen, (255, 255, 255), (275, 250, 50, 15))
            pygame.draw.circle(screen, (222, 218, 144), (300, 500), 50)
            pygame.draw.ellipse(screen, (217, 211, 189), (160, 700, 280, 70))
            pygame.draw.rect(screen, (0, 0, 0), (250, 450, 100, 50))
            pygame.draw.polygon(screen, (255, 255, 255), [(300, 250), (175, 500), (425, 500)], 5)
            pygame.draw.rect(screen, (255, 255, 255), (500, 200, 600, 600))
            screen.blit(text, coord)
            if len(st) == len(mas) and len(mas_true) != 0:
                st = ''
                mas = mas_true.pop(0)
                coord[1] += 30
        pygame.display.flip()


def HISTORY_CONTINUED():
    # загрузка звука печатания на клавиатуре
    pygame.mixer.music.load('keyboard.mp3')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    running = True
    # установление шрифта
    font = pygame.font.SysFont('monaco', 45)
    mas = 'Darkness swept my world centuries ago.'
    mas_true = ['My ancestord told me that.',
                ' ',
                'But what is the light?',
                'Where is he?',
                ' ',
                'I whant to find him.. ']
    texts = ['Darkness swept my world centuries ago.'] + mas_true
    coord = [400, 240]
    st = ''
    fl = True
    # запуск звуковой дорожки. параметр -1 означает, что воспроизводится она бесконечное количество
    # раз
    pygame.mixer.music.play(-1, 0.0)
    # Установление громкости
    pygame.mixer.music.set_volume(0.1)
    while running:
        if len(st) != len(mas):
            st += mas[len(st)]
            time.sleep(0.05)
        # Текст
        text = font.render(st, True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                else:
                    # Если после того, как вся истрия появилась, игрок нажимает на любую кнопку,
                    #  он переходит к началу игры
                    if not fl and len(mas_true) == 0 and len(st) == len(mas):
                        screen.fill((0, 0, 0))
                        GAME_START()
            elif event.type == QUIT:
                running = False
        if len(mas_true) == 0 and len(st) == len(mas):
            # Остановка музыки
            pygame.mixer.music.stop()
            time.sleep(0.5)
            fl = False
            time.sleep(1)
            font1 = pygame.font.SysFont('fixedsys', 35)
            text = font1.render('Press any key to resume', True, (222, 218, 144))
            screen.blit(text, [900, 50])
        elif fl:
            # Вывод текста
            screen.blit(text, coord)
            if len(st) == len(mas) and len(mas_true) != 0:
                st = ''
                mas = mas_true.pop(0)
                coord[1] += 50
        pygame.display.flip()


class Main_Hero(pygame.sprite.Sprite):
    # Класс главного персонажа
    def __init__(self, pole=None):
        self.BG_COLOR = pygame.Color(0, 0, 0)
        # Сам персонаж - искра. Первый круг - ядро, второй - свечение.
        self.BALL_1 = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.BALL_2 = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.circle(self.BALL_1, [199, 180, 97], [40, 40], 40)
        pygame.draw.circle(self.BALL_2, [255, 255, 255], [40, 40], 25)
        # Квадраты, которые находятся внутри персонажа (персонаж так оформлен,
        # Т к искра не имеет определенных очертаний)
        self.mas_hero = [((199, 165, 70), (-25, 0, 20, 20)),
                         ((199, 165, 65), (5, -15, 20, 20)),
                         ((199, 165, 97), (-10, -30, 10, 10)),
                         ((247, 238, 200), (5, 15, 10, 10)),
                         ((247, 238, 215), (15, - 15, 12, 12)),
                         ((247, 238, 215), (20, -20, 5, 5)),
                         ((247, 238, 215), (-20, -25, 15, 15)),
                         ((199, 165, 97), (-10, 15, 10, 10)),
                         ((199, 165, 97), (-5, 5, 5, 5)),
                         ((199, 165, 97), (5, -10, 10, 10)),
                         ((199, 165, 97), (-5, 0, 5, 5))]
        # За искрой тянется шлейф --> как свечение.
        self.mas = [((255, 255, 255), (30, 95, 5, 5), 20), ((240, 220, 130), (35, 90, 15, 15), 40),
                    ((199, 165, 97), (45, 100, 10, 10), 30),
                    ((240, 220, 130), (25, 115, 15, 15), 10),
                    ((255, 255, 255), (50, 140, 10, 10), 30),
                    ((199, 165, 97), (45, 135, 10, 10), 40),
                    ((255, 255, 255), (65, 130, 10, 10), 50),
                    ((255, 255, 255), (70, 100, 5, 5), 20)]
        # Переменные для шара
        surface = pygame.display.get_surface()
        x, y = surface.get_width(), surface.get_height()
        self.ball_pos = Vector2(x // 2 + 100, y // 2)
        self.ballrect = self.BALL_1.get_rect(center=self.ball_pos)
        self.ball_vel = Vector2(0, 0)
        self.ball_mask = pygame.mask.from_surface(self.BALL_1)
        self.hero_fl = False

    def INIT_PLAY(self, cl):
        global screen
        # Плавное движение персонажа
        self.ball_vel *= .94
        self.ball_pos += self.ball_vel
        self.ballrect.center = self.ball_pos
        screen.blit(self.BALL_1, self.ballrect)
        screen.blit(self.BALL_2, self.ballrect)
        mas_1 = []
        # Все части шлейфа находятся в постоянном движении. Движутся они по круговой орбите
        for el in self.mas:
            color, items, rad = el
            x, y, raz_1, raz_2 = items
            x += 50 * cl
            y += 50 * cl
            pygame.draw.rect(screen, color, (round(self.ball_pos.x - 90 + rad
                                                   * math.sin(math.radians(x))),
                                             round(self.ball_pos.y - 60 + rad *
                                                   math.cos(math.radians(y))), raz_1, raz_2))
            mas_1.append((color, (x, y, raz_1, raz_2), rad))
        # Для осществления кругового движения массив постоянно обновляется
        self.mas = mas_1[::]

        for i in self.mas_hero:
            x, y, raz_1, raz_2 = i[1]
            pygame.draw.rect(screen, i[0], (round(self.ball_pos.x + x),
                                            round(self.ball_pos.y + y), raz_1, raz_2))
        pygame.draw.circle(self.BALL_1, [199, 180, 97], [40, 40], 40)
        pygame.draw.circle(self.BALL_2, [255, 255, 255], [40, 40], 25)

    def move(self, wh):
        # Осуществление движения персонажа
        if wh == 'a':
            self.ball_vel.x = -9
        elif wh == 'd':
            self.ball_vel.x = 10
        elif wh == 'w':
            self.ball_vel.y = -5
        elif wh == 's':
            self.ball_vel.y = 7
        # Персонаж не может зайти за поле
        if self.ballrect.top < 0 and self.ball_vel.y < 0:
            self.ball_vel.y *= -1
        elif self.ballrect.bottom > screen.get_height() and self.ball_vel.y > 0:
            self.ball_vel.y *= -1
        # если поле не раздеоено на 2 части (белую и черную)
        if not self.hero_fl:
            if self.ballrect.left < 0 and self.ball_vel.x < 0:
                self.ball_vel.x *= -1
            elif self.ballrect.right > screen.get_width() and self.ball_vel.x > 0:
                self.ball_vel.x *= -1
        # Получение размеров поля
        surface = pygame.display.get_surface()
        x, y = surface.get_width(), surface.get_height()
        # если разделено
        if self.hero_fl:
            if self.ballrect.left < x // 2 + 70 and self.ball_vel.x < 0:
                self.ball_vel.x *= -1
            elif self.ballrect.right > screen.get_width() and self.ball_vel.x > 0:
                self.ball_vel.x *= -1

    def flag_change(self, fl):
        self.hero_fl = fl


# Начало игры. Появление персонажа
# класс, отвечающий за ответы света
class print_text_master():
    def __init__(self):
        self.mas = ''
        self.tt = ''
        self.font = pygame.font.SysFont('fixedsys', 40)
        self.mas_true = []
        self.mas_pro = []

    def change_text(self, text):
        self.mas_pro = []
        self.mas_true = text
        self.tt = ''
        self.mas = self.mas_true.pop(0)

    def print_texts(self):
        # текст печатается
        if len(self.tt) != len(self.mas):
            self.tt += self.mas[len(self.tt)]
            time.sleep(0.01)
        if len(self.tt) == len(self.mas) and len(self.mas_true) != 0:
            self.mas = self.mas_true.pop(0)
            self.mas_pro.append(self.tt)
            self.tt = ''
        if len(self.mas_pro) != 0:
            for i in range(len(self.mas_pro)):
                text = self.font.render(self.mas_pro[i], True, (0, 0, 0))
                screen.blit(text, [100, 100 + 29 * i])
        if len(self.tt) != 0:
            text = self.font.render(self.tt, True, (0, 0, 0))
            screen.blit(text, [100, 100 + 29 * len(self.mas_pro)])

    def return_len(self):
        # возвращает True/False в зависимости о того, напечатан ли текст полностью
        return len(self.tt) == len(self.mas)


# класс отвечает за тесты игрока
class print_text_player():
    def __init__(self):
        self.vib = 0
        self.mas = []
        surface = pygame.display.get_surface()
        self.x, self.y = surface.get_width(), surface.get_height()
        self.font = pygame.font.SysFont('fixedsys', 40)
        self.mas = ''

    def change_vib(self, arrow):
        # меняется выбор игрока
        if arrow == 'left' and self.vib == 1:
            self.vib = 0
        elif arrow == 'right' and self.vib == 0:
            self.vib = 1

    def change_texts(self, tt):
        # замена фраз
        self.mas = tt

    def texts(self):
        # текст выводится на экран
        for i in range(2):
            for el in range(len(self.mas)):
                text = self.font.render(self.mas[i][el], True, (199, 165, 70))
                screen.blit(text, [self.x // 2 * i + 50, self.y - 150 + 25 * el])

    def print_output(self):
        # выделяет выбранную фразу
        rect = pygame.Surface((self.x // 2, 200), pygame.SRCALPHA, 32)
        rect.fill((23, 100, 255, 50))
        if self.vib == 0:
            screen.blit(rect, (0, self.y - 200))
        elif self.vib == 1:
            screen.blit(rect, (self.x // 2, self.y - 200))

    def return_vib(self):
        # возвращает выбор игрока
        return self.vib


# таймер для того, чтоб не было задержек
def timer():
   now = time.localtime(time.time())
   return now[5]


# Начало игры. Появление персонажа
def GAME_START():
    global TEXTS
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    running = True
    surface = pygame.display.get_surface()
    x, y = surface.get_width(), surface.get_height()
    WHITE = (255, 255, 255)
    surf_left = pygame.Surface((x // 2, y))
    surf_left.fill(WHITE)
    # Вызываем класс героя
    HERO = Main_Hero()
    surf_right = pygame.Surface((x // 2, y))
    screen.blit(surf_left, (0, 0))
    screen.blit(surf_right, (x // 2, 0))
    HERO.flag_change(True)
    time_now = time.localtime(time.time())[5]
    font = pygame.font.SysFont('fixedsys', 45)
    # подсказки. исчезнут через 8 секунд
    text = font.render("Press -> or <- to change answer", True, (199, 165, 70))
    text2 = font.render("Press enter to confirm your answer", True, (199, 165, 70))
    clock = pygame.time.Clock()
    TEXTS = print_text_player()
    TEXTS.change_texts([('Who are you?', ' '), ('What are you?', ' ')])
    TEXTS_master = print_text_master()
    scene = 0
    # Загрузка музыки
    pygame.mixer.music.load('fon.mp3')
    # Установление громкости
    pygame.mixer.music.set_volume(0.1)
    # Запуск музыки
    pygame.mixer.music.play(-1, 0.0)
    # тексты света и героя в зависимости от номера сцены
    tab = {1: (["Are you serious? 'What' am I?", ' '],
               [('Sorry.. Who are you', ''),
                ("I didn't know how to address you.", "So who are you?")]),
           2: (["I'm LIGHT! Why were you looking for me?", ' '],
               [('I know all about dark. But I had never seen you',
                 'before. Can you tell me about yourself?'),
                ("I'm tired of living in the dark.", ' ')]),
           3: (["Oh, you are very brave. But what do you", "want to know?", ' '],
               [("I want to know all.", ' '),
                ("I don't know", ' ')]),
           4: (["Why? I think that dark more interesting", "than me.", ' '],
               [("I don't think so.", ' '),
                ("But I don't know you..", ' ')]),
           6: (["Ok, I understand you and I tell you.", "Light is in everyone who is ready to see ",
                "all. You know? You are just like me.", "You are light.", ' '],
               [' ', ' ']),
           5: (["You haven't seen me until this point ", "because I don't open myself to such ",
                "creators. Are you really think that you", "deserve? Huh! Maybe it's too early!",
                ' '],
               [' ', ' '])}
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    # перемещение героя
                if event.key == K_w:
                    HERO.move('w')
                elif event.key == K_s:
                    HERO.move('s')
                elif event.key == K_a:
                    HERO.move('a')
                elif event.key == K_d:
                    HERO.move('d')
                if TEXTS_master.return_len():
                    if event.key == K_RIGHT:
                        TEXTS.change_vib('right')
                    elif event.key == K_LEFT:
                        TEXTS.change_vib('left')
                    elif event.key == K_RETURN:
                        if scene == 0 and TEXTS.return_vib() == 0:
                            scene += 1
                        if scene == 2 and TEXTS.return_vib() == 1:
                            scene += 1
                        if scene == 3 and TEXTS.return_vib() == 0:
                            scene += 3
                        if scene != 5 and scene != 6:
                            scene += 1
                        TEXTS_master.change_text(tab[scene][0])
                        TEXTS.change_texts(tab[scene][1])
        screen.blit(surf_left, (0, 0))
        screen.blit(surf_right, (x // 2, 0))
        HERO.INIT_PLAY(clock.tick() / 1000)
        # в последних сценах нет фраз игрока
        if -1 < scene < 5:
            TEXTS.print_output()
            TEXTS.texts()
        TEXTS_master.print_texts()
        if scene in [5, 6]:
            time_now = time.localtime(time.time())[5]
            if scene == 5:
                scene = -2
            else:
                scene = -1
        if scene < 0 and abs(time_now - timer()) > 10:
            if scene == -2:
                screen.fill((0, 0, 0))
            elif scene == -1:
                screen.fill((255, 255, 255))
        if abs(time_now - timer()) < 8:
            screen.blit(text, [x - 550, 60])
            screen.blit(text2, [x - 550, 100])
        pygame.display.flip()
    pygame.display.update()


# Инициализация игры, запуск первой функции
def main():
    init_window()
    ACTION()


main()