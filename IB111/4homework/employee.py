import datetime


class Employee:
    def __init__(self, number, name, birth_year, skills):
        self.name = name
        self.birth_year = birth_year
        self.age = datetime.date.today().year - self.birth_year
        self.skills = skills.split(';')
        self.eid = number
        self.supervisor = ''

    def add_supervisor(self, name):
        self.supervisor = name
