from controller import Controller
from player import Player
from plan import Plan
from strategy import Strategy
from colorama import Fore, init as colorama_init
colorama_init()


def game_start():
    name = input('Player name ("Nothing for computer"): ')
    return name


def size_of_plan():
    while True:
        plan_size = input('Size of plan (n m): ').split()
        if len(plan_size) == 2:
            return int(plan_size[0]), int(plan_size[1])
        else:
            print(Fore.RED + 'WRONG! 2 numbers needed.' + Fore.RESET)


n, m = size_of_plan()
name = game_start()
player1 = Player(name, 1)
name = game_start()
player2 = Player(name, 2)
plan = Plan(n, m, player1, player2)
strategy = Strategy(plan)
game = Controller(plan, strategy)

game.game()
