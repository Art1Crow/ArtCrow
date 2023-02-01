import draw_b_o
import winner_b_nol
import loser_b_o
import pygame
from random import choice
from sys import exit
from time import sleep

pygame.init()


def bot_game_o():
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

    hod = True

    while game:
        for event in pygame.event.get():
            (x_mouse, y_mouse) = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sleep(0.1)
                exit()
            elif x_mouse >= (x_0 + 20) and x_mouse <= (x_0 + 200) and y_mouse >= (y_0 + 20) and y_mouse <= (y_0 + 200) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_1 == True:
                click.play()
                play_game.blit(nol, (x_0 + 20 , y_0 + 20))
                pygame.display.update()
                sleep(0.3)
                mas[0] = 'X'
                ans_mas.append(None)
                block_1 = False
                hod = True

            elif x_mouse >= (x_0 + 220) and x_mouse <= (x_0 + 400) and y_mouse >= (y_0 + 20) and y_mouse <= (y_0 + 200)\
            and event.type == pygame.MOUSEBUTTONDOWN and block_2 == True:
                click.play()
                play_game.blit(nol, (x_0 + 220 , y_0 + 20))
                pygame.display.update()
                sleep(0.3)
                mas[1] = 'X'
                ans_mas.append(None)
                block_2 = False
                hod = True

            elif x_mouse >= (x_0 + 420) and x_mouse <= (x_0 + 600) and y_mouse >= (y_0 + 20) and y_mouse <= (y_0 + 200) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_3 == True:
                click.play()
                play_game.blit(nol, (x_0 + 420 , y_0 + 20))
                pygame.display.update()
                sleep(0.3)
                mas[2] = 'X'
                ans_mas.append(None)
                block_3 = False
                hod = True

            elif x_mouse >= (x_0 + 20) and x_mouse <= (x_0 + 200) and y_mouse >= (y_0 + 220) and y_mouse <= (y_0 + 400) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_4 == True:
                click.play()
                play_game.blit(nol, (x_0 + 20 , y_0 + 220))
                pygame.display.update()
                sleep(0.3)
                mas[3] = 'X'
                ans_mas.append(None)
                block_4 = False
                hod = True

            elif x_mouse >= (x_0 + 220) and x_mouse <= (x_0 + 400) and y_mouse >= (y_0 + 220) and y_mouse <= (y_0 + 400) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_5 == True:
                click.play()
                play_game.blit(nol, (x_0 + 220 , y_0 + 220))
                pygame.display.update()
                sleep(0.3)
                mas[4] = 'X'
                ans_mas.append(None)
                block_5 = False
                hod = True

            elif x_mouse >= (x_0 + 420) and x_mouse <= (x_0 + 600) and y_mouse >= (y_0 + 220) and y_mouse <= (y_0 + 400) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_6 == True:
                click.play()
                play_game.blit(nol, (x_0 + 420 , y_0 + 220))
                pygame.display.update()
                sleep(0.3)
                mas[5] = 'X'
                ans_mas.append(None)
                block_6 = False
                hod = True

            elif x_mouse >= (x_0 + 20) and x_mouse <= (x_0 + 220) and y_mouse >= (y_0 + 420) and y_mouse <= (y_0 + 600) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_7 == True:
                click.play()
                play_game.blit(nol, (x_0 + 20 , y_0 + 420))
                pygame.display.update()
                sleep(0.3)
                mas[6] = 'X'
                ans_mas.append(None)
                block_7 = False
                hod = True

            elif x_mouse >= (x_0 + 220) and x_mouse <= (x_0 + 400) and y_mouse >= (y_0 + 420) and y_mouse <= (y_0 + 600)\
            and event.type == pygame.MOUSEBUTTONDOWN and block_8 == True:
                click.play()
                play_game.blit(nol, (x_0 + 220 , y_0 + 420))
                pygame.display.update()
                sleep(0.3)
                mas[7] = 'X'
                ans_mas.append(None)
                block_8 = False
                hod = True

            elif x_mouse >= (x_0 + 420) and x_mouse <= (x_0 + 600) and y_mouse >= (y_0 + 420) and y_mouse <= (y_0 + 600) \
            and event.type == pygame.MOUSEBUTTONDOWN and block_9 == True:
                click.play()
                play_game.blit(nol, (x_0 + 420 , y_0 + 420))
                pygame.display.update()
                sleep(0.3)
                mas[8] = 'X'
                block_9 = False
                ans_mas.append(None)
                hod = True

            if hod == True and len(ans_mas) != 9:
                while True:
                    bot_hod = choice(mas)
                    if bot_hod == 'X' or bot_hod == '0':
                        continue
                    else:
                        break
                if bot_hod == 1:
                    play_game.blit(cros, (x_0 + 20, y_0 + 20))
                    mas[0] = '0'
                    ans_mas.append(None)
                    block_1 = False

                elif bot_hod == 2:
                    play_game.blit(cros, (x_0 + 220, y_0 + 20))
                    mas[1] = '0'
                    ans_mas.append(None)
                    block_2 = False

                elif bot_hod == 3:
                    play_game.blit(cros, (x_0 + 420, y_0 + 20))
                    mas[2] = '0'
                    ans_mas.append(None)
                    block_3 = False

                elif bot_hod == 4:
                    play_game.blit(cros, (x_0 + 20, y_0 + 220))
                    mas[3] = '0'
                    ans_mas.append(None)
                    block_4 = False

                elif bot_hod == 5:
                    play_game.blit(cros, (x_0 + 220, y_0 + 220))
                    mas[4] = '0'
                    ans_mas.append(None)
                    block_5 = False

                elif bot_hod == 6:
                    play_game.blit(cros, (x_0 + 420, y_0 + 220))
                    mas[5] = '0'
                    ans_mas.append(None)
                    block_6 = False

                elif bot_hod == 7:
                    play_game.blit(cros, (x_0 + 20, y_0 + 420))
                    mas[6] = '0'
                    ans_mas.append(None)
                    block_7 = False

                elif bot_hod == 8:
                    play_game.blit(cros, (x_0 + 220, y_0 + 420))
                    mas[7] = '0'
                    ans_mas.append(None)
                    block_8 = False

                elif bot_hod == 9:
                    play_game.blit(cros, (x_0 + 420, y_0 + 420))
                    mas[8] = '0'
                    ans_mas.append(None)
                    block_9 = False
                hod = False

        if (mas[0] == mas[1] == mas[2] == 'X') or (mas[3] == mas[4] == mas[5] == 'X') or (mas[6] == mas[7] == mas[8] == 'X') or\
        (mas[0] == mas[3] == mas[6] == 'X') or (mas[2] == mas[5] == mas[8] == 'X') or (mas[0] == mas[4] == mas[8] == 'X') or\
        (mas[2] == mas[4] == mas[6] == 'X'):
            game = False
            sleep(1)
            pygame.mixer.music.stop()
            winner_b_nol.winner_cros()
        if (mas[0] == mas[1] == mas[2] == '0') or (mas[3] == mas[4] == mas[5] == '0') or (mas[6] == mas[7] == mas[8] == '0') or\
        (mas[0] == mas[3] == mas[6] == '0') or (mas[2] == mas[5] == mas[8] == '0') or (mas[0] == mas[4] == mas[8] == '0') or\
        (mas[2] == mas[4] == mas[6] == '0'):
            pygame.display.update()
            game = False
            sleep(1)
            pygame.mixer.music.stop()
            loser_b_o.winner_nol()
        elif len(ans_mas) == 9:
            pygame.display.update()
            game = False
            sleep(1)
            pygame.mixer.music.stop()
            draw_b_o.winner_draw()
        pygame.display.update()