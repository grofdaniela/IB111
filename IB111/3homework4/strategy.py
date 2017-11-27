import random
from plan import Plan

class Strategy:
    def __init__(self, plan):
        self.plan = plan

    def random(self):
        while True:
            x, y = random.randrange(self.plan.rows), random.randrange(self.plan.cols)
            if self.plan.check_turn(x, y):
                return x, y

    def partial_smart(self, x, y):
        num_to_fill = 0
        for i in self.plan.get_xrange(x):
            for j in self.plan.get_yrange(y):
                if self.plan.plan[i][j] == 0:
                    num_to_fill += 1
        return num_to_fill

    def smart(self):
        best_move = [0, 0]
        best_move_value = 0
        for i in range(self.plan.rows):
            for j in range(self.plan.cols):
                if self.plan.check_turn(i, j):
                    i_j_value = self.partial_smart(i, j)
                    if i_j_value == 9:
                        return i, j
                    elif best_move_value < i_j_value:
                        best_move_value = i_j_value
                        best_move = [i, j]
        return best_move[0], best_move[1]

    def human(self):
        while True:
            while True:
                move = input('Insert your next turn! ').split()
                try:
                    x, y = int(move[0]), int(move[1])
                    assert len(move) == 2
                    break
                except ValueError:
                    print('Number, please. ')
                except (AssertionError, IndexError):
                    print('This is 2D game.\nPlease, give me 2 coordinates.')

            if self.plan.check_turn(x, y):
                return x, y
            print('It is not valid turn, dummy!\nTry it again and do better.')
