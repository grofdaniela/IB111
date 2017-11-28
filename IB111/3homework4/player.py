import re

class Player:
    def __init__(self, name, number, color, is_smart=True):
        self.name = name
        self.number = number
        self.color = color
        if re.match('[Cc][oO][mM][Pp][Uu][Tt][Ee][Rr]', self.name):
            if is_smart:
                self.type = 1
            else:
                self.type = 2
        else:
            self.type = 0
