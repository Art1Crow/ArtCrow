import bot_game
import music_file
import lobby
import bot_game_o
import pygame
import sys
from time import sleep


pygame.init()


def get_cros_or_nol():
    programIcon = pygame.image.load(r'C:\Users\Natalja\Downloads\icon.png')
    pygame.display.set_icon(programIcon)

    game_mode = pygame.display.set_mode((1173, 660))
    pygame.display.set_caption('cross or nol')

    x, y = 0, 0

    clock = pygame.time.Clock()
    FPS = 60

    fon_lobby = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\FON.png')
    game_mode.blit(fon_lobby, (x, y))

    pygame.mixer.music.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Music\bs_music_.mp3')
    pygame.mixer.music.play(-1)

    replay = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\home_game.png')
    game_mode.blit(replay, (x + 1040, y + 530))

    nol_bot = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\nol_bot_.png')
    game_mode.blit(nol_bot, (x + 300, y + 350))

    cros_bot = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\cros_bot_.png')
    game_mode.blit(cros_bot, (x + 300, y + 200))

    non_off_m = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\non_off_music.png')
    off_m = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\off_music_.png')
    if music_file.music_value == True:
        music_const = non_off_m
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
        music_const = off_m
    game_mode.blit(music_const, (x + 30, y + 560))

    click = pygame.mixer.Sound(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Music\click.ogg')

    game = True
    while game:
        for event in pygame.event.get():
            (x1, y1) = pygame.mouse.get_pos()
            if x1 >= (x + 30) and x1 <= (x + 105) and y1 >= (y + 560) and y1 <= (y + 635) and event.type == pygame.MOUSEBUTTONDOWN:             # звук в игре
                if music_const == non_off_m:
                    music_file.music_value = False
                    click.play()
                    sleep(0.1)
                    music_const = off_m
                    pygame.mixer.music.pause()
                else:
                    music_file.music_value = True
                    click.play()
                    sleep(0.1)
                    music_const = non_off_m
                    pygame.mixer.music.unpause()
                game_mode.blit(music_const, (30, 560))
            elif x1 >= (x + 1040) and x1 <= (x + 1140) and y1 >= (y + 530) and y1 <= (y + 630) and event.type == pygame.MOUSEBUTTONDOWN:   # вернуться назад
                lobby.music_value = True
                click.play()
                lobby.get_lobby()
            elif x1 >= (x + 300) and x1 <= (x + 800) and y1 >= (y + 350) and y1 <= (y + 470) and event.type == pygame.MOUSEBUTTONDOWN:          # играть с ботом за ноликов
                pygame.mixer.music.stop()
                click.play()
                sleep(0.075)
                bot_game_o.bot_game_o()
            elif x1 >= (x + 300) and x1 <= (x + 800) and y1 >= (y + 200) and y1 <= (y + 320) and event.type == pygame.MOUSEBUTTONDOWN:          # играть с ботом за крестиков
                pygame.mixer.music.stop()
                click.play()
                sleep(0.075)
                bot_game.bot_game()
            elif event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
    clock.tick(FPS)


