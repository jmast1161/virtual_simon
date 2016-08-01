#===========================================================================================#
#   IMPORTS                                                                                 #
#===========================================================================================#

import pygame
from pygame import *
import random
import os, sys
import time

#===========================================================================================#
#   GLOBAL DECLARATIONS                                                                     #
#===========================================================================================#

screen = display.set_mode((800, 600))
running = True

one = 'one.png'
one = pygame.image.load(one).convert()
one.set_colorkey((0, 0, 0))

two = 'two.png'
two = pygame.image.load(two).convert()
two.set_colorkey((0, 0, 0))

three = 'three.png'
three = pygame.image.load(three).convert()
three.set_colorkey((0, 0, 0))

four = 'four.png'
four = pygame.image.load(four).convert()
four.set_colorkey((0, 0, 0))

five = 'five.png'
five = pygame.image.load(five).convert()
five.set_colorkey((0, 0, 0))

six = 'six.png'
six = pygame.image.load(six).convert()
six.set_colorkey((0, 0, 0))

seven = 'seven.png'
seven = pygame.image.load(seven).convert()
seven.set_colorkey((0, 0, 0))

eight = 'eight.png'
eight = pygame.image.load(eight).convert()
eight.set_colorkey((0, 0, 0))

nine = 'nine.png'
nine = pygame.image.load(nine).convert()
nine.set_colorkey((0, 0, 0))

zero = 'zero.png'
zero = pygame.image.load(zero).convert()
zero.set_colorkey((0, 0, 0))

nums = []
nums.append(zero)
nums.append(one)
nums.append(two)
nums.append(three)
nums.append(four)
nums.append(five)
nums.append(six)
nums.append(seven)
nums.append(eight)
nums.append(nine)

pygame.font.init()

#===========================================================================================#
#   CLASS DEFINITIONS                                                                       #
#===========================================================================================#

class game_board():
    def border(self):
        screen.lock()
        draw.line(screen,(165, 165, 165), (200, 100), (600, 100), 3)
        draw.line(screen,(165, 165, 165), (200, 500), (600, 500), 3)
        draw.line(screen,(165, 165, 165), (200, 100), (200, 500), 3)
        draw.line(screen,(165, 165, 165), (600, 100), (600, 500), 3)
        screen.unlock()
    def grid_lines(self, difficulty):
        if difficulty == 'easy':
            screen.lock()
            draw.line(screen,(165, 165, 165), (200, 300), (600, 300), 3)
            draw.line(screen,(165, 165, 165), (400, 100), (400, 500), 3)
            screen.unlock()
        if difficulty == 'medium':
            screen.lock()
            draw.line(screen,(165, 165, 165), (200, 233), (600, 233), 3)
            draw.line(screen,(165, 165, 165), (200, 367), (600, 367), 3)
            draw.line(screen,(165, 165, 165), (333, 100), (333, 500), 3)
            draw.line(screen,(165, 165, 165), (467, 100), (467, 500), 3)
            screen.unlock()
        if difficulty == 'hard':
            screen.lock()
            draw.line(screen,(165, 165, 165), (200, 200), (600, 200), 3)
            draw.line(screen,(165, 165, 165), (200, 300), (600, 300), 3)
            draw.line(screen,(165, 165, 165), (200, 400), (600, 400), 3)
            draw.line(screen,(165, 165, 165), (300, 100), (300, 500), 3)
            draw.line(screen,(165, 165, 165), (400, 100), (400, 500), 3)
            draw.line(screen,(165, 165, 165), (500, 100), (500, 500), 3)
            screen.unlock()
    def spaces(self, difficulty):
        if difficulty == 'easy':
            spaces = [(Rect(202, 102, 197, 197), (255, 0, 0)),
                      (Rect(402, 102, 197, 197), (0, 255, 0)),
                      (Rect(202, 302, 197, 197), (0, 0, 255)),
                      (Rect(402, 302, 197, 197), (255, 255, 0))]
            return spaces
        if difficulty == 'medium':
            return [(Rect(202, 102, 130, 130), (255, 0, 0)),
                    (Rect(335, 102, 131, 130), (127, 127, 255)),
                    (Rect(469, 102, 130, 130), (0, 255, 0)),
                    (Rect(202, 235, 130, 131), (255, 0, 255)),
                    (Rect(335, 235, 131, 131), (255, 255, 255)),
                    (Rect(469, 235, 130, 131), (0, 255, 255)),
                    (Rect(202, 369, 130, 130), (0, 0, 255)),
                    (Rect(335, 369, 131, 130), (255, 127, 127)),
                    (Rect(469, 369, 130, 130), (255, 255, 0))]
        if difficulty == 'hard':
            return [(Rect(202, 102, 97, 97), (255, 0, 0)),
                    (Rect(302, 102, 97, 97), (127, 127, 255)),
                    (Rect(402, 102, 97, 97), (127, 127, 0)),
                    (Rect(502, 102, 97, 97), (0, 255, 0)),
                    (Rect(202, 202, 97, 97), (255, 0, 255)),
                    (Rect(302, 202, 97, 97), (255, 255, 255)),
                    (Rect(402, 202, 97, 97), (127, 255, 127,)),
                    (Rect(502, 202, 97, 97), (127, 0, 127)),
                    (Rect(202, 302, 97, 97), (0, 127, 0)),
                    (Rect(302, 302, 97, 97), (255, 127, 0)),
                    (Rect(402, 302, 97, 97), (127, 127, 127)),
                    (Rect(502, 302, 97, 97), (0, 255, 255)),
                    (Rect(202, 402, 97, 97), (0, 0, 255)),
                    (Rect(302, 402, 97, 97), (255, 127, 127)),
                    (Rect(402, 402, 97, 97), (0, 127, 127)),
                    (Rect(502, 402, 97, 97), (255, 255, 0))]

#===========================================================================================#
#   FUNCTION DEFINITIONS                                                                    #
#===========================================================================================#

def show_position(spots, position):
    draw.rect(screen, spots[0][1], spots[0][0])

def clear_position(spots, position):
    draw.rect(screen, (0, 0, 0), spots[position][0])

def draw_easy():
    draw.rect(screen, (0, 0, 0), (25, 250, 200, 200))

    draw.line(screen, (165, 165, 165), (25, 250), (225, 250), 2)
    draw.line(screen, (165, 165, 165), (25, 250), (25, 450), 2)
    draw.line(screen, (165, 165, 165), (225, 250), (225, 450), 2)
    draw.line(screen, (165, 165, 165), (25, 450), (225, 450), 2)
    
    draw.line(screen, (165, 165, 165), (125, 250), (125, 450), 2)
    draw.line(screen, (165, 165, 165), (25, 350), (225, 350), 2)
    
    return Rect(25, 250, 200, 200)

def draw_medium():
    draw.rect(screen, (0, 0, 0), (300, 250, 200, 200))
    
    draw.line(screen, (165, 165, 165), (300, 250), (500, 250), 2)
    draw.line(screen, (165, 165, 165), (300, 250), (300, 450), 2)
    draw.line(screen, (165, 165, 165), (500, 250), (500, 450), 2)
    draw.line(screen, (165, 165, 165), (300, 450), (500, 450), 2)
    
    draw.line(screen, (165, 165, 165), (366, 250), (366, 450), 2)
    draw.line(screen, (165, 165, 165), (433, 250), (433, 450), 2)
    draw.line(screen, (165, 165, 165), (300, 316), (500, 316), 2)
    draw.line(screen, (165, 165, 165), (300, 383), (500, 383), 2)

    return Rect(300, 250, 200, 200)

def draw_hard():
    draw.rect(screen, (0, 0, 0), (575, 250, 200, 200))
    
    draw.line(screen, (165, 165, 165), (575, 250), (775, 250), 2)
    draw.line(screen, (165, 165, 165), (575, 250), (575, 450), 2)
    draw.line(screen, (165, 165, 165), (775, 250), (775, 450), 2)
    draw.line(screen, (165, 165, 165), (575, 450), (775, 450), 2)
    
    draw.line(screen, (165, 165, 165), (625, 250), (625, 450), 2)
    draw.line(screen, (165, 165, 165), (675, 250), (675, 450), 2)
    draw.line(screen, (165, 165, 165), (725, 250), (725, 450), 2)
    draw.line(screen, (165, 165, 165), (575, 300), (775, 300), 2)
    draw.line(screen, (165, 165, 165), (575, 350), (775, 350), 2)
    draw.line(screen, (165, 165, 165), (575, 400), (775, 400), 2)

    return Rect(575, 250, 200, 200)

def display_score(score, score_background):
    score = str(score)
    screen.blit(score_background, (300, 525), (300, 525, 200, 50))
    display.flip()
    if len(score) == 2:
        screen.blit(nums[int(score[0])], (360, 525))
        screen.blit(nums[int(score[1])], (400, 525))
        display.flip()
    elif len(score) == 3:
        screen.blit(nums[int(score[0])], (340, 525))
        screen.blit(nums[int(score[1])], (380, 525))
        screen.blit(nums[int(score[2])], (420, 525))
        display.flip()
    elif len(score) == 4:
        screen.blit(nums[int(score[0])], (320, 525))
        screen.blit(nums[int(score[1])], (360, 525))
        screen.blit(nums[int(score[2])], (400, 525))
        screen.blit(nums[int(score[3])], (440, 525))
        display.flip()

def get_high_scores(high_score_list, difficulty):
    if difficulty == 'easy':
        for score in open('high_scores_easy.txt', 'r'):
            temp = score
            high_score_list.append(int(temp.strip()))
    elif difficulty == 'medium':
        for score in open('high_scores_medium.txt', 'r'):
            temp = score
            high_score_list.append(int(temp.strip()))
    elif difficulty == 'hard':
        for score in open('high_scores_hard.txt', 'r'):
            temp = score
            high_score_list.append(int(temp.strip()))
    return high_score_list

def update_high_scores(current_score, high_score_list):
    if current_score > high_score_list[-1]:
        high_score_list.append(current_score)
        temp_list = sorted(high_score_list)
        temp_list = temp_list[::-1]
        temp_list.pop()
    else:
        temp_list = high_score_list
    return temp_list

def write_scores_to_file(high_scores, difficulty):
    if difficulty == 'easy':
        f = open('high_scores_easy.txt', 'w')
        for score in high_scores:
            f.write(str(score)+'\n')
    elif difficulty == 'medium':
        f = open('high_scores_medium.txt', 'w')
        for score in high_scores:
            f.write(str(score)+'\n')
    elif difficulty == 'hard':
        f = open('high_scores_hard.txt', 'w')
        for score in high_scores:
            f.write(str(score)+'\n')

def show_scores(high_score_easy, high_score_medium, high_score_hard):
    font = pygame.font.SysFont("calibri", 20)
    y_pos = 225
    for num in range(1, 11):
        show_num = font.render(str(num) + '.', True, (255, 255, 255))
        screen.blit(show_num, (80, y_pos))
        screen.blit(show_num, (360, y_pos))
        screen.blit(show_num, (630, y_pos))
        y_pos += 25
        display.flip()
    y_pos = 225
    for score in high_score_easy:
        show_score = font.render(str(score).strip(), True, (255, 255, 255))
        screen.blit(show_score, (115, y_pos))
        y_pos += 25
        display.flip()
    y_pos = 225
    for score in high_score_medium:
        show_score = font.render(str(score).strip(), True, (255, 255, 255))
        screen.blit(show_score, (395, y_pos))
        y_pos += 25
        display.flip()
    y_pos = 225
    for score in high_score_hard:
        show_score = font.render(str(score).strip(), True, (255, 255, 255))
        screen.blit(show_score, (670, y_pos))
        y_pos += 25
        display.flip()

#===========================================================================================#
#   MAIN FUNCTION                                                                           #
#===========================================================================================#

def main():
    #song: Thunk by Simon Mathewson
    screen_objects = []
    music = 'Thunk.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1, 0.0)
    
    high_score_list = []
    high_scores_easy = []
    high_scores_medium = []
    high_scores_hard = []

    high_score_list = get_high_scores(high_score_list, 'easy')
    high_scores_easy = get_high_scores(high_scores_easy, 'easy')
    high_scores_medium = get_high_scores(high_scores_medium, 'medium')
    high_scores_hard = get_high_scores(high_scores_hard, 'hard')

    background = 'black-background_00313351.jpg'
    background = pygame.image.load(background).convert()
    score_background = background
    
    logo = 'cooltext1158257068.png'
    logo = pygame.image.load(logo).convert()
    logo.set_colorkey((0,0,0))
    
    play_game = 'cooltext1159386129.png'
    play_game = pygame.image.load(play_game).convert()
    play_game.set_colorkey((0,0,0))

    high_scores = 'cooltext1159388036.png'
    high_scores = pygame.image.load(high_scores).convert()
    high_scores.set_colorkey((0, 0, 0))

    music_on = 'music_on.png'
    music_on = pygame.image.load(music_on).convert()
    music_on.set_colorkey((0, 0, 0,))

    music_off = 'music_off.png'
    music_off = pygame.image.load(music_off).convert()
    music_off.set_colorkey((0, 0, 0))

    directions = 'cooltext1159388957.png'
    directions = pygame.image.load(directions).convert()
    directions.set_colorkey((0, 0, 0))

    credits = 'cooltext1159389392.png'
    credits = pygame.image.load(credits).convert()
    credits.set_colorkey((0, 0, 0))

    easy_mode = 'easy.png'
    easy_mode = pygame.image.load(easy_mode).convert()
    easy_mode.set_colorkey((0, 0, 0))

    medium_mode = 'medium.png'
    medium_mode = pygame.image.load(medium_mode).convert()
    medium_mode.set_colorkey((0, 0, 0))

    hard_mode = 'hard.png'
    hard_mode = pygame.image.load(hard_mode).convert()
    hard_mode.set_colorkey((0, 0, 0))
    
    back_btn = 'back.png'
    back_btn = pygame.image.load(back_btn).convert()
    back_btn.set_colorkey((0, 0, 0))

    prog_and_dev = 'prog_and_dev.png'
    prog_and_dev = pygame.image.load(prog_and_dev).convert()
    prog_and_dev.set_colorkey((0, 0, 0))

    josh = 'josh.png'
    josh = pygame.image.load(josh).convert()
    josh.set_colorkey((0, 0, 0))

    music_cred = 'music.png'
    music_cred = pygame.image.load(music_cred).convert()
    music_cred.set_colorkey((0, 0, 0))

    thunk = 'thunk.png'
    thunk = pygame.image.load(thunk).convert()
    thunk.set_colorkey((0, 0, 0))

    dir_1 = 'dir_1.png'
    dir_1 = pygame.image.load(dir_1).convert()
    dir_1.set_colorkey((0, 0, 0))

    dir_2 = 'dir_2.png'
    dir_2 = pygame.image.load(dir_2).convert()
    dir_2.set_colorkey((0, 0, 0))

    dir_3 = 'dir_3.png'
    dir_3 = pygame.image.load(dir_3).convert()
    dir_3.set_colorkey((0, 0, 0))

    dir_4 = 'dir_4.png'
    dir_4 = pygame.image.load(dir_4).convert()
    dir_4.set_colorkey((0, 0, 0))

    dir_5 = 'dir_5.png'
    dir_5 = pygame.image.load(dir_5).convert()
    dir_5.set_colorkey((0, 0, 0))

    dir_6 = 'dir_6.png'
    dir_6 = pygame.image.load(dir_6).convert()
    dir_6.set_colorkey((0, 0, 0))

    dir_7 = 'dir_7.png'
    dir_7 = pygame.image.load(dir_7).convert()
    dir_7.set_colorkey((0, 0, 0))

    test_mini = 'test_your_mind_mini.png'
    test_mini = pygame.image.load(test_mini).convert()
    test_mini.set_colorkey((0, 0, 0))

    game_over = 'game_over.png'
    game_over = pygame.image.load(game_over).convert()
    game_over.set_colorkey((0, 0, 0))

    play_again = 'play_again.png'
    play_again = pygame.image.load(play_again).convert()
    play_again.set_colorkey((0, 0, 0))

    menu_display = 'main_menu.png'
    menu_display = pygame.image.load(menu_display).convert()
    menu_display.set_colorkey((0, 0, 0))

    new_high_score = 'new_high_score.png'
    new_high_score = pygame.image.load(new_high_score).convert()
    new_high_score.set_colorkey((0, 0, 0))

    screen.fill((0,0,0))
    background_rect = screen.blit(background, (0, 0))
    logo_rect = screen.blit(logo, (125,15))
    play_rect = screen.blit(play_game, (338, 200))
    high_scores_rect = screen.blit(high_scores, (250, 250))
    music_rect = screen.blit(music_on, (280, 300))
    directions_rect = screen.blit(directions, (260, 350))
    credits_rect = screen.blit(credits, (300, 400))

    screen_objects.append((background, (0, 0)))
    screen_objects.append((logo, (125, 15)))
    screen_objects.append((play_game, (338, 200)))
    screen_objects.append((high_scores, (250, 250)))
    screen_objects.append((directions, (260, 350)))
    screen_objects.append((credits, (300, 400)))
    display.flip()

    music_toggle = True
    board = game_board()
    main_menu = True
    spots = []
    clicked_time = 0
    first = True
    clear_spot = 0
    show = True
    hide = False
    chain = []
    something = 0
    append_chain = True
    clock = pygame.time.Clock()
    playtime = 0
    counter = 0
    computer_turn = True
    player_turn = False
    draw_time = 0
    start_game = False
    select_difficulty = False
    show_credits = False
    show_directions = False
    show_high_scores = False
    game_over_menu = False
    first_turn = False
    write_scores = True
    score = 0
    difficulty = ''
    wait_time = 0.0

    while running:

        playtime = pygame.time.get_ticks() / 1000.0
        while main_menu:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if play_rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(background, (0, 0))
                        screen.blit(logo, (125, 15))
                        global easy_rect, medium_rect, hard_rect
                        easy_rect = screen.blit(easy_mode, (60, 150))
                        easy_btn_rect = draw_easy()
                        medium_rect = screen.blit(medium_mode, (310, 150))
                        medium_btn_rect = draw_medium()
                        hard_rect = screen.blit(hard_mode, (605, 150))
                        hard_btn_rect = draw_hard()
                        back_rect = screen.blit(back_btn, (10, 550))
                        display.flip()
                        main_menu = False
                        select_difficulty = True
                    if high_scores_rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(background, (0, 0))
                        screen.blit(logo, (125, 15))
                        easy_score_rect = screen.blit(easy_mode, (60, 150))
                        medium_score_rect = screen.blit(medium_mode, (310, 150))
                        hard_score_rect = screen.blit(hard_mode, (605, 150))
                        show_scores(high_scores_easy, high_scores_medium, high_scores_hard)
                        back_rect = screen.blit(back_btn, (10, 550))
                        display.flip()
                        main_menu = False
                        show_high_scores = True
                    if music_rect.collidepoint(pygame.mouse.get_pos()) and music_toggle:
                        pygame.mixer.music.stop()
                        screen.blit(background, (0, 0))
                        for so in screen_objects:
                            screen.blit(so[0], so[1])
                        music_rect = screen.blit(music_off, (280, 300))
                        music_toggle = False
                        display.flip()
                    elif music_rect.collidepoint(pygame.mouse.get_pos()) and not music_toggle:
                        pygame.mixer.music.play(-1, 0.0)
                        for so in screen_objects:
                            screen.blit(so[0], so[1])
                        music_rect = screen.blit(music_on, (280, 300))
                        music_toggle = False
                        display.flip()
                        music_toggle = True
                        display.flip()
                    if directions_rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(background, (0, 0))
                        screen.blit(logo, (125, 15))
                        global dir_1_rect, dir_2_rect, dir_3_rect, dir_4_rect, dir_5_rect, dir_6_rect, dir_7_rect
                        dir_1_rect = screen.blit(dir_1, (75, 150))
                        test_mini_rect = screen.blit(test_mini, (75, 150))
                        dir_2_rect = screen.blit(dir_2, (75, 200))
                        dir_3_rect = screen.blit(dir_3, (75, 250))
                        dir_4_rect = screen.blit(dir_4, (75, 300))
                        dir_5_rect = screen.blit(dir_5, (75, 350))
                        dir_6_rect = screen.blit(dir_6, (75, 400))
                        dir_7_rect = screen.blit(dir_7, (75, 450))
                        back_rect = screen.blit(back_btn, (10, 550))
                        display.flip()
                        show_directions = True
                        main_menu = False
                    if credits_rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(background, (0, 0))
                        screen.blit(logo, (125, 15))
                        global prog_and_dev_rect, josh_rect, music_cred_rect, thunk_rect
                        prog_and_dev_rect = screen.blit(prog_and_dev, (4, 175))
                        josh_rect = screen.blit(josh, (220, 225))
                        music_cred_rect = screen.blit(music_cred, (325, 325))
                        thunk_rect = screen.blit(thunk, (50, 375))
                        back_rect = screen.blit(back_btn, (10, 550))
                        display.flip()
                        show_credits = True
                        main_menu = False
                if event.type == QUIT:
                    quit()
                    sys.exit()

        if select_difficulty:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if easy_rect.collidepoint(pygame.mouse.get_pos()) or easy_btn_rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(background, (0, 0))
                        screen.blit(logo, (125, 15))
                        board.border()
                        difficulty = 'easy'
                        board.grid_lines(difficulty)
                        spots = board.spaces(difficulty)
                        for spot in spots:
                            draw.rect(screen, (0, 0, 0), spot[0])
                        select_difficulty = False
                        computer_turn = True
                        first_turn = True
                        start_game = True
                        display.flip()
                    if medium_rect.collidepoint(pygame.mouse.get_pos()) or medium_btn_rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(background, (0, 0))
                        screen.blit(logo, (125, 15))
                        board.border()
                        difficulty = 'medium'
                        board.grid_lines(difficulty)
                        spots = board.spaces(difficulty)
                        for spot in spots:
                            draw.rect(screen, (0, 0, 0), spot[0])
                        select_difficulty = False
                        computer_turn = True
                        first_turn = True
                        start_game = True
                        display.flip()
                    if hard_rect.collidepoint(pygame.mouse.get_pos()) or hard_btn_rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(background, (0, 0))
                        screen.blit(logo, (125, 15))
                        board.border()
                        difficulty = 'hard'
                        board.grid_lines(difficulty)
                        spots = board.spaces(difficulty)
                        for spot in spots:
                            draw.rect(screen, (0, 0, 0), spot[0])
                        select_difficulty = False
                        computer_turn = True
                        first_turn = True
                        start_game = True
                        display.flip()
                    if back_rect.collidepoint(pygame.mouse.get_pos()):
                        main_menu = True
                        select_difficulty = False
                        for so in screen_objects:
                            screen.blit(so[0], so[1])
                        if music_toggle:
                            music_rect = screen.blit(music_on, (280, 300))
                        else:
                            music_rect = screen.blit(music_off, (280, 300))
                        display.flip()
                if event.type == QUIT:
                    quit()
                    sys.exit()

        if show_high_scores:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if back_rect.collidepoint(pygame.mouse.get_pos()):
                        main_menu = True
                        show_high_scores = False
                        for so in screen_objects:
                            screen.blit(so[0], so[1])
                        if music_toggle:
                            music_rect = screen.blit(music_on, (280, 300))
                        else:
                            music_rect = screen.blit(music_off, (280, 300))
                        display.flip()
                if event.type == QUIT:
                    quit()
                    sys.exit()

        if show_directions:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if back_rect.collidepoint(pygame.mouse.get_pos()):
                        main_menu = True
                        show_directions = False
                        for so in screen_objects:
                            screen.blit(so[0], so[1])
                        if music_toggle:
                            music_rect = screen.blit(music_on, (280, 300))
                        else:
                            music_rect = screen.blit(music_off, (280, 300))
                        display.flip()
                if event.type == QUIT:
                    quit()
                    sys.exit()

        if show_credits:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if back_rect.collidepoint(pygame.mouse.get_pos()):
                        main_menu = True
                        show_credits = False
                        for so in screen_objects:
                            screen.blit(so[0], so[1])
                        if music_toggle:
                            music_rect = screen.blit(music_on, (280, 300))
                        else:
                            music_rect = screen.blit(music_off, (280, 300))
                        display.flip()

        if computer_turn and start_game:
            if first_turn:
                screen.blit(zero, (377, 525))
                first_turn = False
            if append_chain:
                chain.append(random.randint(0, len(spots) - 1))
                append_chain = False
                show == True
                show_time = playtime
                counter = 0
                position = chain[counter]
            if show == True and show_time + 0.1 < playtime:
                draw.rect(screen, spots[position][1], spots[position][0])
                hide_time = playtime
                show = False
                hide = True
            if hide == True and hide_time + 1.0 < playtime:
                draw.rect(screen, (0, 0, 0), spots[position][0])
                show = True
                hide = False
                show_time = playtime
                counter += 1
                if counter > len(chain) - 1:
                    append_chain = True
                    computer_turn = False
                    player_turn = True
                    counter = 0
                    wait_time = playtime
                else:
                    position = chain[counter]

        if player_turn and start_game:
            for event in pygame.event.get():
                position = pygame.mouse.get_pos()
                for spot, color in spots:
                    if spot.collidepoint(position):
                        draw.rect(screen, color, spot)
                        display.flip()
                        draw_time = time.time()
                        if event.type == pygame.MOUSEBUTTONUP:
                            mouse_position = pygame.mouse.get_pos()
                            if spots[chain[counter]][0].collidepoint(mouse_position):
                                counter += 1
                                score += 10
                                display_score(score, score_background)
                                wait_time = playtime
                                if counter > len(chain) - 1:
                                    draw.rect(screen, (0, 0, 0), spots[chain[counter - 1]][0])
                                    computer_turn = True
                                    player_turn = False
                                    counter = 0
                            else:
                                screen.blit(game_over, (25, 200))
                                global play_again_rect, menu_display_rect
                                play_again_rect = screen.blit(play_again, (228, 325))
                                menu_display_rect = screen.blit(menu_display, (232, 390))
                                display.flip()
                                game_over_menu = True
                                player_turn = False
                                break
                    else:
                        draw.rect(screen, (0, 0, 0), spot)
                if event.type == QUIT:
                    quit()
                    sys.exit()
            if wait_time + 1.0 < playtime:
                screen.blit(game_over, (25, 200))
                play_again_rect = screen.blit(play_again, (228, 325))
                menu_display_rect = screen.blit(menu_display, (232, 390))
                display.flip()
                game_over_menu = True
                player_turn = False
                computer_turn = False
        
        if game_over_menu:
            if write_scores:
                if difficulty == 'easy':
                    if score > high_scores_easy[-1]:
                        screen.blit(new_high_score, (142, 110))
                    high_scores_easy = update_high_scores(score, high_scores_easy)
                    write_scores_to_file(high_scores_easy, difficulty)
                    write_scores = False
                elif difficulty == 'medium':
                    if score > high_scores_medium[-1]:
                        screen.blit(new_high_score, (142, 110))
                    high_scores_medium = update_high_scores(score, high_scores_medium)
                    write_scores_to_file(high_scores_medium, difficulty)
                    write_scores = False
                elif difficulty == 'hard':
                    if score > high_scores_hard[-1]:
                        screen.blit(new_high_score, (142, 110))
                    high_scores_hard = update_high_scores(score, high_scores_hard)
                    write_scores_to_file(high_scores_hard, difficulty)
                    write_scores = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if play_again_rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(background, (0, 0))
                        screen.blit(logo, (125, 15))
                        board.border()
                        board.grid_lines(difficulty)
                        spots = board.spaces(difficulty)
                        for spot in spots:
                            draw.rect(screen, (0, 0, 0), spot[0])
                        select_difficulty = False
                        start_game = True
                        display.flip()
                        computer_turn = True
                        start_game = True
                        game_over_menu = False
                        chain = []
                        score = 0
                        first_turn = True
                        write_scores = True
                    if menu_display_rect.collidepoint(pygame.mouse.get_pos()):
                        main_menu = True
                        game_over_menu = False
                        for so in screen_objects:
                            screen.blit(so[0], so[1])
                        if music_toggle:
                            music_rect = screen.blit(music_on, (280, 300))
                        else:
                            music_rect = screen.blit(music_off, (280, 300))
                        chain = []
                        score = 0
                        write_scores = True
                        display.flip()
                if event.type == QUIT:
                    quit()
                    sys.exit()

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()

        display.flip()

#===========================================================================================#
#   MAIN BODY                                                                               #
#===========================================================================================#

if __name__ == '__main__':
    main()
