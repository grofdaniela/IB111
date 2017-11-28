import re

class Player:
    def __init__(self, name, number, color):
        self.name = 'computer' if name == '' else name
        self.number = number
        self.color = color
        self.type = 1 if self.name == 'computer' else 0

