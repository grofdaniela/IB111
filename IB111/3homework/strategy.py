import random
from plan import Plan


class Strategy:
    def __init__(self, plan):
        self.plan = plan

    def random(self):
        while True:
            x = random.randrange(self.plan.rows)
            y = random.randrange(self.plan.cols)
            if self.plan.check_turn(x, y):
                return x, y

    def partial_smart(self, x, y):
        num_to_fill = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= j < self.plan.rows and 0 <= i < self.plan.cols:
                    if self.plan.plan[i][j]:
                        num_to_fill += 1
        return num_to_fill

    def smart(self):
        best_move = [0, 0]
        best_move_value = 0
        for i in range(self.plan.rows):
            for j in range(self.plan.cols):
                i_j_value = self.partial_smart(i, j)
                if i_j_value == 9:
                    return i, j, 9
                elif best_move_value < i_j_value:
                    best_move_value = i_j_value
                    best_move = [i, j]
        return best_move[0], best_move[1]

    def human(self):
        while True:
            row = int(input("Select the row: "))
            col = int(input("Select the column: "))
            if row > self.plan.rows - 1 or row < 0 or col > self.plan.cols - 1 or col < 0:
                print("Invalid input.")
            elif not (self.plan.plan[row][col]):
                print("Invalid input.")
            else:
                return row, col
