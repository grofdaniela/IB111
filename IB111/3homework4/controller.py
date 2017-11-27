from plan import Plan
from strategy import Strategy
from time import sleep


class Controller:
    def __init__(self, plan, strategy):
        self.plan = plan
        self.strategy = strategy

    def print_header(self, number_of_leg):
        print('---', number_of_leg, '. leg ---\n' +
              self.plan.current_player.name + ' plays.')

    def who_plays(self):
        if self.plan.current_player.type == 1:
            sleep(1)
            x, y = self.strategy.smart()
        elif self.plan.current_player.type == 2:
            x, y = self.strategy.random()
        else:
            x, y = self.strategy.human()
        self.plan.make_turn(x, y)

    def game(self):
        number_of_turn = 0
        plan = self.plan
        self.plan.print_plan()
        while not plan.game_over():
            self.print_header(int(number_of_turn/2+1))
            self.who_plays()
            self.plan.print_plan()
            self.plan.swap_players()
            number_of_turn += 1
        self.plan.swap_players()
        print(self.plan.current_player.name, 'won.')





