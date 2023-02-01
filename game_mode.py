import cros_or_nol_mode
import music_file
import lobby
import cros_nol
import pygame
import sys
from time import sleep

pygame.init()


def get_game_mode():
    programIcon = pygame.image.load(r'C:\Users\Natalja\Downloads\icon.png')
    pygame.display.set_icon(programIcon)

    game_mode = pygame.display.set_mode((1173, 660))
    pygame.display.set_caption('Game Mode')

    x, y = 0, 0

    clock = pygame.time.Clock()
    FPS = 60

    fon_lobby = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\FON.png')
    game_mode.blit(fon_lobby, (x, y))

    pygame.mixer.music.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Music\bs_music_.mp3')
    pygame.mixer.music.play(-1)

    replay = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\home_game.png')
    game_mode.blit(replay, (x + 1040, y + 530))

    non_off_m = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\non_off_music.png')
    off_m = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\off_music_.png')
    if music_file.music_value == True:
        pygame.mixer.music.unpause()
        music_const = non_off_m
    else:
        pygame.mixer.music.pause()
        music_const = off_m
    game_mode.blit(music_const, (x + 30, y + 560))

    bot_player = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\bot_game.png')
    game_mode.blit(bot_player, (x + 310, y + 260))

    _1_vs_1_ = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\_1_vs_1_.png')
    game_mode.blit(_1_vs_1_, (x + 310, y + 355))

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
                click.play()
                lobby.get_lobby()
            elif x1 >= (x + 310) and x1 <= (x + 660) and y1 >= (y + 260) and y1 <= (y + 335) and event.type == pygame.MOUSEBUTTONDOWN:          # играть с ботом
                pygame.mixer.music.stop()
                click.play()
                sleep(0.075)
                cros_or_nol_mode.get_cros_or_nol()
            elif x1 >= (x + 310) and x1 <= (x + 660) and y1 >= (y + 355) and y1 <= (y + 430) and event.type == pygame.MOUSEBUTTONDOWN:          # играть 1 на 1
                pygame.mixer.music.stop()
                click.play()
                sleep(0.075)
                cros_nol.event_game()
            elif event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
    clock.tick(FPS)
