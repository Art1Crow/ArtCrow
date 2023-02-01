import lobby
import cros_nol
import pygame
import sys
from time import sleep
pygame.init()


def winner_cros():
    programIcon = pygame.image.load(r'C:\Users\Natalja\Downloads\icon.png')
    pygame.display.set_icon(programIcon)

    winner = pygame.display.set_mode((1173, 660))

    pygame.mixer.music.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Music\win.ogg')
    pygame.mixer.music.play(-1)


    pygame.display.set_caption('Winner')

    x, y = 0, 0

    clock = pygame.time.Clock()
    FPS = 60

    fon_lobby = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\FON.png')
    winner.blit(fon_lobby, (x, y))

    replay = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\continue.png')
    winner.blit(replay, (x + 500, y + 450))

    win = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\win_cros.png')
    winner.blit(win, (x + 250, y + 200))

    home = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\home_game.png')
    winner.blit(home, (x + 1040, y + 530))

    click = pygame.mixer.Sound(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Music\click.ogg')

    game = True
    while game:
        for event in pygame.event.get():
            (x1, y1) = pygame.mouse.get_pos()
            if x1 >= (x + 1040) and x1 <= (x + 1140) and y1 >= (y + 530) and y1 <= (y + 630) and event.type == pygame.MOUSEBUTTONDOWN:   # вернуться в меню
                pygame.mixer.music.stop()
                click.play()
                sleep(0.05)
                lobby.get_lobby()
            elif x1 >= (x + 500) and x1 <= (x + 600) and y1 >= (y + 450) and y1 <= (y + 550) and event.type == pygame.MOUSEBUTTONDOWN:  # сыграть еще раз
                pygame.mixer.music.stop()
                click.play()
                sleep(0.05)
                cros_nol.event_game()
            elif event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
    clock.tick(FPS)


