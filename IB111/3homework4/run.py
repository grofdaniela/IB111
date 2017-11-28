import re
from controller import Controller
from player import Player
from plan import Plan
from strategy import Strategy


def get_players_info():
    name = input('Player name (nothing for computer): ') or 'computer'
    is_smart = False
    possible_colors = ['blue', 'red', 'cyan', 'green', 'black', 'magenta', 'white', 'yellow']
    if re.match('[Cc][oO][mM][Pp][Uu][Tt][Ee][Rr]', name):
        is_smart = input('Should be computer be smart? *Yes (1) or No (0). ') or 1
    while True:
        color = input('Player color: ')
        if color in possible_colors:
            break
        else:
            print('Wrong color, try again. ')
    return name, color, is_smart == 1


def size_of_plan():
    while True:
        size = input('Size of plan (n m): ')
        try:
            return int(size.split()[0]), int(size.split()[1])
        except ValueError:
            print('Invalid input.')


if __name__ == '__main__':
    n, m = size_of_plan()
    name, color, is_smart = get_players_info()
    player1 = Player(name, 1, color, is_smart)
    name, color, is_smart = get_players_info()
    player2 = Player(name, 2, color, is_smart)
    plan = Plan(n, m, player1, player2)
    strategy = Strategy(plan)
    game = Controller(plan, strategy)
    game.game()