import random
import os


def new_plan(n):
    return [[0 for _ in range(n)] for _ in range(n)]


def print_plan(plan):
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] == 1:
                print('*', end=' ')
            elif plan[i][j] == -1:
                print('x', end=' ')
            else:
                print('.', end=' ')
        print()
    print()


def game_over(plan):
    for line in plan:
        for place in line:
            if place == 0:
                return False
    return True


def check_turn(plan, x, y):
    return True if x < len(plan) and y < len(plan[0]) and plan[x][y] == 0 else False


def strategy(plan):
    while True:
        x, y = random.randrange(len(plan)), random.randrange(len(plan[0]))
        if check_turn(plan, x, y):
            return x, y


def smart_strategy(plan):
    def partial_smart_strategy(plan, irange, jrange):
        num_of_free = 0
        for i in irange:
            for j in jrange:
                if plan[i][j] == 0:
                    num_of_free += 1
        return num_of_free
    the_best_move = [0, 0]
    max_free = 0
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] == 0:
                if i in range(1, len(plan) - 1):
                    irange = range(i - 1, i + 2)
                elif i == 0:
                    irange = range(i + 2)
                elif i == len(plan) - 1:
                    irange = range(i - 1, i + 1)
                if j in range(1, len(plan[0]) - 1):
                    jrange = range(j - 1, j + 2)
                elif j == 0:
                    jrange = range(j + 2)
                elif j == len(plan[0]) - 1:
                    jrange = range(j - 1, j + 1)
                num_of_free = partial_smart_strategy(plan, irange, jrange)
                if num_of_free == 9:
                    return i, j
                if max_free <= num_of_free:
                    max_free = num_of_free
                    the_best_move = [i, j]
    return the_best_move[0], the_best_move[1]


def make_turn(plan, x, y):
    def partial_make_turn(plan, xrange, yrange):
        for i in xrange:
            for j in yrange:
                if plan[i][j] == 0:
                    plan[i][j] = -1
        return plan
    plan[x][y] = 1
    if x in range(1, len(plan)-1):
        xrange = range(x-1, x+2)
    elif x == 0:
        xrange = range(x+2)
    elif x == len(plan)-1:
        xrange = range(x-1, x+1)
    if y in range(1, len(plan[0])-1):
        yrange = range(y-1, y+2)
    elif y == 0:
        yrange = range(y+2)
    elif y == len(plan[0]) - 1:
        yrange = range(y-1, y+1)
    return partial_make_turn(plan, xrange, yrange)


def human_turn(plan):
    valid_turn = False
    while not valid_turn:
        again = True
        while again:
            move = input('Insert your next turn!').split()
            if len(move) == 2:
                again = False
            else:
                print('This is 2D game.\nPlease, give me 2 coordinates.')
        x, y = int(move[0]), int(move[1])
        if check_turn(plan, x, y):
            return x, y
        print('It is not valid turn, dummy!\nTry it again and do better.')


def play_the_game(size, player1='computer 1', player2='computer 2', be_smart=True):
    def partial_play(plan, player):
        if player == 'computer 1' or player == 'computer 2':
            if be_smart:
                x, y = smart_strategy(plan)
            else:
                x, y = strategy(plan)
        else:
            x, y = human_turn(plan)
        plan = make_turn(plan, x, y)
        print_plan(plan)
        return plan
    players = [player1, player2]
    plan = new_plan(size)
    print('--- The plan ---')
    print_plan(plan)
    leg = 0
    while not game_over(plan):
        print('---', int(leg/2+1), '. leg ---')
        print('---', players[0], 'plays ---')
        plan = partial_play(plan, players[0])
        players[0], players[1] = players[1], players[0]
        leg += 1
    print(players[1], 'won.')


play_the_game(7)
