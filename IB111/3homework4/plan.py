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

    def get_xrange(self, x):
        if x in range(1, self.rows - 1):
            return range(x - 1, x + 2)
        elif x == 0:
            return range(x + 2)
        elif x == self.rows - 1:
            return range(x - 1, x + 1)

    def get_yrange(self, y):
        if y in range(1, self.cols - 1):
            return range(y - 1, y + 2)
        elif y == 0:
            return range(y + 2)
        elif y == self.cols - 1:
            return range(y - 1, y + 1)

    def make_turn(self, x, y):
        self.plan[x][y] = self.current_player.number
        for i in self.get_xrange(x):
            for j in self.get_yrange(y):
                if self.plan[i][j] == 0:
                    self.plan[i][j] = -self.current_player.number

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
                    print(eval('Fore.' + self.player1.color.upper()) + '*', end=' ')
                elif self.plan[i][j] == -1:
                    print(eval('Fore.' + self.player1.color.upper()) + 'x', end=' ')
                elif self.plan[i][j] == 2:
                    print(eval('Fore.' + self.player2.color.upper()) + '*', end=' ')
                elif self.plan[i][j] == -2:
                    print(eval('Fore.' + self.player2.color.upper()) + 'x', end=' ')
                else:
                    print('.', end=' ')
            print()