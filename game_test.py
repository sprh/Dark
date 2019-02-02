import pygame, time, threading, random, math, os
from pygame.locals import *
from pygame.math import Vector2
NUM = 0


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


def init_window():
    #инициализация окна
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Game')


def ACTION():
    #начало игры
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
                        Game_Start()
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


class Main_Hero(pygame.sprite.Sprite):
    # Класс главного персонажа
    def __init__(self):
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
        self.ball_pos = Vector2(275, 200)
        self.ballrect = self.BALL_1.get_rect(center=self.ball_pos)
        self.ball_vel = Vector2(0, 0)
        self.ball_mask = pygame.mask.from_surface(self.BALL_1)

    def INIT_PLAY(self, cl):
        global screen
        # Плавное движение персонажа
        self.ball_vel *= .94
        self.ball_pos += self.ball_vel
        self.ballrect.center = self.ball_pos
        screen.fill(self.BG_COLOR)
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
        # Персонаж не может зайти за поле, т к он находится в темном кубе
        if self.ballrect.top < 0 and self.ball_vel.y < 0:
            self.ball_vel.y *= -1
        elif self.ballrect.bottom > screen.get_height() and self.ball_vel.y > 0:
            self.ball_vel.y *= -1
        if self.ballrect.left < 0 and self.ball_vel.x < 0:
            self.ball_vel.x *= -1
        elif self.ballrect.right > screen.get_width() and self.ball_vel.x > 0:
            self.ball_vel.x *= -1


# Начало игры. Появление персонажа
def Game_Start():
    # Загрузка музыки
    pygame.mixer.music.load('fon.mp3')
    # Установление громкости
    pygame.mixer.music.set_volume(0.1)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    running = True
    # Вызываем класс героя
    HERO = Main_Hero()
    clock = pygame.time.Clock()
    # Запуск музыки
    pygame.mixer.music.play(-1, 0.0)
    mas = ['Darkness swept my world centuries ago.',
           'My ancestord told me that.',
           ' ',
           'But what is the light?',
           'Where is he?',
           ' ',
           'I whant to find him..']
    # Получение размеров поля
    surface = pygame.display.get_surface()
    x, y = surface.get_width(), surface.get_height()
    font = pygame.font.SysFont('monaco', 34)
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
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
            elif event.type == QUIT:
                running = False
        coords = pygame.mouse.get_pos()
        HERO.move(coords)
        HERO.INIT_PLAY(clock.tick() / 1000)
        rect = pygame.Surface((x - 0-0, 200), pygame.SRCALPHA, 32)
        rect.fill((200, 200, 207, 50))
        screen.blit(rect, (0, y - 200))
        pygame.display.flip()


# Инициализация игры, запуск первой функции
def main():
    init_window()
    Game_Start()

main()