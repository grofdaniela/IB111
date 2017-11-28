from player import Player
from colorama import Fore, init as colorama_init
colorama_init(autoreset=True)

class Plan:
    def __init__(self, n, m, player1, player2):
        self.rows = n
        self.cols = m
        self.player1 = player1
        self.player2 = player2
        self.plan = [[0 for _ in range(m)] for _ in range(n)]
        self.current_player = self.player1

    def swap_players(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def make_turn(self, x, y):
        self.plan[x][y] = 1
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= j < self.rows and 0 <= i < self.cols:
                    self.plan[i][j] = 2

    def check_turn(self, x, y):
        return x < self.rows and y < self.cols and self.plan[x][y] == 0

    def game_over(self):
        for line in self.plan:
            if 0 in line:
                return False
        return True

    def print_plan(self):
        print(' ', ' '.join([str(i) for i in range(self.cols)]))
        for i in range(self.rows):
            print(i, end=' ')
            for j in range(self.cols):
                if self.plan[i][j] == 1:
                    print('*', end=' ')
                elif self.plan[i][j] == 2:
                    print('x', end=' ')
                else:
                    print('.', end=' ')
            print()
