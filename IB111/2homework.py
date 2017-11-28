from __future__ import print_function
import random

# The program is commented to perform the pix() function. To perform pix_analysis()
# you need to comment all print statements (it is not necessary,
# however, I recommend it, that it does not show course of each individual games.
# Comment lines: 93, 96, 97, 98, 112, 115, 118
# Uncomment lines: 148
# Documentation for functions is available.



def dice():
    """
    It make one throw with a dice.
    :return: number of dots on dice
    """
    return random.randrange(1, 7)


def one_line_print(length, player, pos):
    """
    If make print output of one player in one leg.
    :param length: length of playing field
    :param player: name (sign) of particular player
    :param pos: int position of player
    :return:
    """
    if pos == 0:
        print(player, 'in Home', end=' ')
    else:
        print('Home', end=' ')
    for i in range(1, length):
        if i == pos:
            print(player, end=' ')
        else:
            print('.', end=' ')
    if pos == length:
        print(player, 'in Finish')
    else:
        print('Finish')


def one_player_leg(length, pos):
    """
    It make a process of one player leg. Player throws a dice. If it is 6, he continues until he throws diff number.
     If he throws number higher then difference between his position and end of playing field, he stay on his current
     place. If the number on dice is equal to difference between his position and end of playing field, he wins a game.
    :param length: length of playing field
    :param pos: int position of player before a leg
    :return: pos: int position of player after a leg
            moves: list of moves/throws
    """
    throw = dice()
    moves = []
    while throw == 6:
        if pos + throw < length:
            pos += throw
            moves.append(throw)
        elif pos + throw == length:
            pos += throw
            moves.append(throw)
            return pos, moves
        else:
            moves.append(throw)
        throw = dice()
    else:
        if pos + throw < length:
            pos += throw
            moves.append(throw)
        elif pos + throw == length:
            pos += throw
            moves.append(throw)
            return pos, moves
        else:
            moves.append(throw)
    return pos, moves


def one_leg(length, pos_m, pos_p):
    """
    It make a process of one leg for both the players. If first player takes a position of the second one, the second
    player goes Home. It is
    :param length: length of playing field
    :param pos_m: int position of Mat before a leg
    :param pos_p: int position of Pat before a leg
    :return: pos_m: int position of Mat after a leg
            pos_p: int position of Pat after a leg
    """
    pos_m, mat_moves = one_player_leg(length, pos_m)
    if pos_p == pos_m:
        pos_p = 0
    pos_p, pat_moves = one_player_leg(length, pos_p)
    print('Mat:', end=' ')
    for move in mat_moves:
        print(move, end=' ')
    print('Pat:', end=' ')
    for move in pat_moves:
        print(move, end=' ')
    if pos_m == pos_p:
        pos_m = 0
    print('\n')
    one_line_print(length, 'M', pos_m)
    one_line_print(length, 'P', pos_p)
    print('\n')
    return pos_m, pos_p


def pix(length, legs):
    """
    It make a process of one game. If one player wins before end of the legs, game stops and return number (for analyisi)
    :param length: length of playing field
    :param legs: max number of legs in one game
    :return: int 1 if Mat wins, int -1 if Pat wins, int 0 if nobody wins.
    """
    pos_m = 0
    pos_p = 0
    for i in range(1, legs+1):
        print(i, '. leg')
        pos_m, pos_p = one_leg(length, pos_m, pos_p)
        if pos_m == length:
            print('Mat wins')
            return 1
        elif pos_p == length:
            print('Pat wins')
            return -1
    return 0


pix(30, 20)


def pix_analysis(length, legs, count):
    """
    It co runs count times pix function and summarize the ends of each game. Then print the count of wins and ties.
    :param length: length of playing field
    :param legs: max number of legs in one game
    :param count: number of repetitions
    :return: mats_wins: number of games that Mat wins
             pats_wins: number of games that Pat wins
             ties: number of games that nobody wins
    """
    mats_wins = 0
    pats_wins = 0
    ties = 0
    for _ in range(count):
        end_of_game = pix(length, legs)
        if end_of_game == 1:
            mats_wins += 1
        elif end_of_game == -1:
            pats_wins += 1
        else:
            ties += 1
    print('Mats wins:', mats_wins, '\nPats wins:', pats_wins, '\nTies:', ties)

# pix_analysis(20,10,10)
