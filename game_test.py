import pygame, time, threading, random, math
from pygame.locals import *
NUM = 0



def init_window():
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Game')


def ACTION():
    NUM = True
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    font = pygame.font.SysFont('fixedsys', 40)
    text = font.render('Press any key to start', True, (222, 218, 144))
    font = pygame.font.SysFont('fixedsys', 80)
    text1 = font.render('"Can you manage the', True, (250, 238, 231))
    font = pygame.font.SysFont('fixedsys', 120)
    text2 = font.render('DARK?"', True, (255, 255, 255))
    sec = 0
    fl = True
    while NUM:
        screen.fill((0, 0, 0))
        time.sleep(0.5)
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
        if sec % 4 == 0 or sec == 0:
            fl = False
        elif sec % 2 == 0:
            fl = True
        pygame.draw.line(screen, (255, 255, 255), [300, 0], [300, 250], 5)
        pygame.draw.rect(screen, (255, 255, 255), (275, 250, 50, 15))
        if fl:
            pygame.draw.circle(screen, (222, 218, 144), (300, 500), 50)
            pygame.draw.ellipse(screen, (217, 211, 189), (160, 700, 280, 70))
        else:
            pygame.draw.circle(screen, (255, 255, 255), (300, 500), 50, 5)
            pygame.draw.ellipse(screen, (0, 0, 0), (160, 700, 280, 70))
        pygame.draw.rect(screen, (0, 0, 0), (250, 450, 100, 50))
        pygame.draw.polygon(screen, (255, 255, 255), [(300, 250), (175, 500), (425, 500)], 5)
        screen.blit(text, [700, 800])
        screen.blit(text1, [400, 200])
        screen.blit(text2, [650, 280])
        pygame.display.flip()


def HISTORY():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    running = True
    font = pygame.font.SysFont('monaco', 34)
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
    while running:
        if len(st) != len(mas):
            st += mas[len(st)]
            time.sleep(0.05)
        text = font.render(st, True, (0, 0, 0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        if len(mas_true) == 0 and len(st) == len(mas):
            time.sleep(0.5)
            screen.fill((0, 0, 0))
            fl = False
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
    def __init__(self, x, y):
        self.mas_hero = [((235, 192, 106), (0, 0), 30),
                ((199, 165, 97), (-25, 0, 20, 20)),
                ((199, 165, 97), (5, -15, 20, 20)),
                ((247, 238, 215), (0, 0), 20),
                ((199, 165, 97), (-10, -30, 10, 10)),
                ((247, 238, 215), (5, 15, 10, 10)),
                ((247, 238, 215), (15, - 15, 12, 12)),
                ((247, 238, 215), (20, -20, 5, 5)),
                ((247, 238, 215), (-20, -25, 15, 15)),
                ((199, 165, 97), (-10, 15, 10, 10)),
                ((199, 165, 97), (-5, 5, 5, 5)),
                ((199, 165, 97), (5, -10, 10, 10)),
                ((199, 165, 97), (-5, 0, 5, 5))]
        self.hero_x = x
        self.hero_y = y
        self.mas = [((255, 255, 255), (30, 95, 5, 5), 20), ((240, 220, 130), (35, 90, 15, 15), 40),
               ((199, 165, 97), (45, 100, 10, 10), 30), ((240, 220, 130), (25, 115, 15, 15), 10),
               ((255, 255, 255), (50, 140, 10, 10), 30), ((199, 165, 97), (45, 135, 10, 10), 40),
               ((255, 255, 255), (65, 130, 10, 10), 50), ((255, 255, 255), (70, 100, 5, 5), 20)]
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen.fill((0, 0, 0))

    def INIT_PLAY(self, cl):
        running = True
        self.screen.fill(pygame.Color("black"))
        cl = cl / 1000
        mas_1 = []
        for i in range(len(self.mas_hero)):
            el = self.mas_hero[i]
            if i == 0 or i == 3:
                pygame.draw.circle(self.screen, el[0], (round(self.hero_x), round(self.hero_y)), el[2])
            else:
                x, y, raz_1, raz_2 = el[1]
                pygame.draw.rect(self.screen, el[0], (round(self.hero_x + x), round(self.hero_y + y), raz_1, raz_2))
        for el in self.mas:
            color, items, rad = el
            x, y, raz_1, raz_2 = items
            print(items)
            x += 50 * cl
            y += 50 * cl
            pygame.draw.rect(self.screen, color, (round(self.hero_x - 50 + rad * math.sin(math.radians(x))),
                                                   round(self.hero_y - 50 + rad * math.cos(math.radians(y))), raz_1, raz_2))
            mas_1.append((color, (x, y, raz_1, raz_2), rad))
        self.mas = mas_1[::]

    def move(self, coords):
        self.hero_x, self.hero_y = coords

def Game_Start():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    running = True
    HERO = Main_Hero(150, 150)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        coords = pygame.mouse.get_pos()
        HERO.move(coords)
        HERO.INIT_PLAY(clock.tick())
        pygame.display.flip()


def main():
    init_window()
    Game_Start()

main()