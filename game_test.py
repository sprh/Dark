import pygame, time, threading, random
from pygame.locals import *
NUM = 0


def init_window():
    pygame.init()
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


def main():
    init_window()
    ACTION()

main()