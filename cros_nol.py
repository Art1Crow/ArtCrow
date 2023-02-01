import winner_draw
import winner_crosses
import winner_nol
import pygame
from sys import exit
from time import sleep

pygame.init()


def get_win(x):
    return x == 'X'


def get_win_nol(x):
    return x == '0'


def event_game():
    programIcon = pygame.image.load(r'C:\Users\Natalja\Downloads\icon.png')
    pygame.display.set_icon(programIcon)

    x, y = 0, 0

    mas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    ans_mas = []

    x_0, y_0 = 256.5, 20

    pygame.mixer.music.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Music\fon_game_.mp3')
    pygame.mixer.music.play(-1)


    play_game = pygame.display.set_mode((1173, 660))
    pygame.display.set_caption('GAME')

    fon_game = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\FON.png')
    play_game.blit(fon_game, (x, y))

    game_poligon = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\poligon.png')
    play_game.blit(game_poligon, (x_0, y_0))

    cros = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\cros.png')

    nol = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\nol.png')

    click = pygame.mixer.Sound(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Music\click.ogg')

    cros_nol = cros


    game = True

    block_1 = True
    block_2 = True
    block_3 = True
    block_4 = True
    block_5 = True
    block_6 = True
    block_7 = True
    block_8 = True
    block_9 = True


    while game:
        for event in pygame.event.get():
            (x_mouse, y_mouse) = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sleep(0.1)
                exit()

            elif x_mouse >= (x_0 + 20) and x_mouse <= (x_0 + 200) and y_mouse >= (y_0 + 20) and y_mouse <= (y_0 + 200) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_1 == True:
                click.play()
                if cros_nol == cros:
                    play_game.blit(cros, (x_0 + 20 , y_0 + 20))
                    cros_nol = nol
                    mas[0] = 'X'
                else:
                    play_game.blit(nol, (x_0 + 20 , y_0 + 20))
                    cros_nol = cros
                    mas[0] = '0'
                ans_mas.append(None)
                block_1 = False

            elif x_mouse >= (x_0 + 220) and x_mouse <= (x_0 + 400) and y_mouse >= (y_0 + 20) and y_mouse <= (y_0 + 200)\
            and event.type == pygame.MOUSEBUTTONDOWN and block_2 == True:
                click.play()
                if cros_nol == cros:
                    play_game.blit(cros, (x_0 + 220 , y_0 + 20))
                    cros_nol = nol
                    mas[1] = 'X'
                else:
                    play_game.blit(nol, (x_0 + 220 , y_0 + 20))
                    cros_nol = cros
                    mas[1] = '0'
                ans_mas.append(None)
                block_2 = False

            elif x_mouse >= (x_0 + 420) and x_mouse <= (x_0 + 600) and y_mouse >= (y_0 + 20) and y_mouse <= (y_0 + 200) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_3 == True:
                click.play()
                if cros_nol == cros:
                    play_game.blit(cros, (x_0 + 420 , y_0 + 20))
                    cros_nol = nol
                    mas[2] = 'X'
                else:
                    play_game.blit(nol, (x_0 + 420 , y_0 + 20))
                    cros_nol = cros
                    mas[2] = '0'
                ans_mas.append(None)
                block_3 = False

            elif x_mouse >= (x_0 + 20) and x_mouse <= (x_0 + 200) and y_mouse >= (y_0 + 220) and y_mouse <= (y_0 + 400) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_4 == True:
                click.play()
                if cros_nol == cros:
                    play_game.blit(cros, (x_0 + 20 , y_0 + 220))
                    cros_nol = nol
                    mas[3] = 'X'
                else:
                    play_game.blit(nol, (x_0 + 20 , y_0 + 220))
                    cros_nol = cros
                    mas[3] = '0'
                ans_mas.append(None)
                block_4 = False

            elif x_mouse >= (x_0 + 220) and x_mouse <= (x_0 + 400) and y_mouse >= (y_0 + 220) and y_mouse <= (y_0 + 400) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_5 == True:
                click.play()
                if cros_nol == cros:
                    play_game.blit(cros, (x_0 + 220 , y_0 + 220))
                    cros_nol = nol
                    mas[4] = 'X'
                else:
                    play_game.blit(nol, (x_0 + 220 , y_0 + 220))
                    cros_nol = cros
                    mas[4] = '0'
                ans_mas.append(None)
                block_5 = False

            elif x_mouse >= (x_0 + 420) and x_mouse <= (x_0 + 600) and y_mouse >= (y_0 + 220) and y_mouse <= (y_0 + 400) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_6 == True:
                click.play()
                if cros_nol == cros:
                    play_game.blit(cros, (x_0 + 420 , y_0 + 220))
                    cros_nol = nol
                    mas[5] = 'X'
                else:
                    play_game.blit(nol, (x_0 + 420 , y_0 + 220))
                    cros_nol = cros
                    mas[5] = '0'
                ans_mas.append(None)
                block_6 = False

            elif x_mouse >= (x_0 + 20) and x_mouse <= (x_0 + 220) and y_mouse >= (y_0 + 420) and y_mouse <= (y_0 + 600) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_7 == True:
                click.play()
                if cros_nol == cros:
                    play_game.blit(cros, (x_0 + 20 , y_0 + 420))
                    cros_nol = nol
                    mas[6] = 'X'
                else:
                    play_game.blit(nol, (x_0 + 20 , y_0 + 420))
                    cros_nol = cros
                    mas[6] = '0'
                ans_mas.append(None)
                block_7 = False

            elif x_mouse >= (x_0 + 220) and x_mouse <= (x_0 + 400) and y_mouse >= (y_0 + 420) and y_mouse <= (y_0 + 600)\
            and event.type == pygame.MOUSEBUTTONDOWN and block_8 == True:
                click.play()
                if cros_nol == cros:
                    play_game.blit(cros, (x_0 + 220 , y_0 + 420))
                    cros_nol = nol
                    mas[7] = 'X'
                else:
                    play_game.blit(nol, (x_0 + 220 , y_0 + 420))
                    cros_nol = cros
                    mas[7] = '0'
                ans_mas.append(None)
                block_8 = False

            elif x_mouse >= (x_0 + 420) and x_mouse <= (x_0 + 600) and y_mouse >= (y_0 + 420) and y_mouse <= (y_0 + 600) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_9 == True:
                click.play()
                if cros_nol == cros:
                    play_game.blit(cros, (x_0 + 420 , y_0 + 420))
                    cros_nol = nol
                    mas[8] = 'X'
                else:
                    play_game.blit(nol, (x_0 + 420 , y_0 + 420))
                    cros_nol = cros
                    mas[8] = '0'
                block_9 = False
                ans_mas.append(None)
        if (mas[0] == mas[1] == mas[2] == 'X') or (mas[3] == mas[4] == mas[5] == 'X') or (mas[6] == mas[7] == mas[8] == 'X') or\
        (mas[0] == mas[3] == mas[6] == 'X') or (mas[2] == mas[5] == mas[8] == 'X') or (mas[0] == mas[4] == mas[8] == 'X') or\
        (mas[2] == mas[4] == mas[6] == 'X'):
            pygame.display.update()
            game = False
            sleep(0.5)
            pygame.mixer.music.stop()
            winner_crosses.winner_cros()
        if (mas[0] == mas[1] == mas[2] == '0') or (mas[3] == mas[4] == mas[5] == '0') or (mas[6] == mas[7] == mas[8] == '0') or\
        (mas[0] == mas[3] == mas[6] == '0') or (mas[2] == mas[5] == mas[8] == '0') or (mas[0] == mas[4] == mas[8] == '0') or\
        (mas[2] == mas[4] == mas[6] == '0'):
            pygame.display.update()
            game = False
            sleep(0.5)
            pygame.mixer.music.stop()
            winner_nol.winner_nol().winner_nol()
        elif len(ans_mas) == 9:
            pygame.display.update()
            game = False
            sleep(0.5)
            pygame.mixer.music.stop()
            winner_draw.winner_draw()
        pygame.display.update()

