import game_mode
import music_file
import pygame
import sys
from time import sleep

pygame.init()


def get_lobby():
    programIcon = pygame.image.load(r'C:\Users\Natalja\Downloads\icon.png')
    pygame.display.set_icon(programIcon)

    lobby = pygame.display.set_mode((1173, 660))
    pygame.display.set_caption('Lobby')

    x, y = 0, 0

    clock = pygame.time.Clock()
    FPS = 60

    pygame.mixer.music.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Music\bs_music_.mp3')
    pygame.mixer.music.play(-1)

    fon_lobby = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\FON.png')
    lobby.blit(fon_lobby, (x, y))

    play_game = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\play_game.png')
    lobby.blit(play_game, (x + 310, y + 230))

    exit_lobby = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\exit_lobby_.png')
    lobby.blit(exit_lobby, (x + 950, y + 575))

    non_off_m = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\non_off_music.png')
    off_m = pygame.image.load(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Photo\off_music_.png')

    if music_file.music_value == True:
        music_const = non_off_m
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
        music_const = off_m
    lobby.blit(music_const, (x + 30, y + 560))
    click = pygame.mixer.Sound(r'C:\Users\Natalja\PycharmProjects\КРЕСТИКИ - НОЛИКИ\Music\click.ogg')
    game = True
    while game:
        for event in pygame.event.get():
            (x1, y1) = pygame.mouse.get_pos()
            if x1 >= (x + 30) and x1 <= (x + 105) and y1 >= (y + 560) and y1 <= (y + 635) and event.type == pygame.MOUSEBUTTONDOWN:  # звук в игре
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
                lobby.blit(music_const, (30, 560))
            if x1 >= (x + 310) and x1 <= (x + 710) and y1 >= (y + 230) and y1 <= (y + 330) and event.type == pygame.MOUSEBUTTONDOWN:  # кнопка play
                pygame.mixer.music.stop()
                click.play()
                game_mode.get_game_mode()
            elif x1 >= (x + 950) and x1 <= (x + 1150) and y1 >= (y + 575) and y1 <= (y + 625) and event.type == pygame.MOUSEBUTTONDOWN:             # кнопка exit
                pygame.mixer.music.stop()
                click.play()
                sleep(0.1)
                sys.exit()
            elif event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
    clock.tick(FPS)
