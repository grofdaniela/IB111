from employee import Emplyee
from team import Team


class Firm:
    def __init__(self):
        self.employees = []
        self.teams = []

    def add_employee_to_organization(self, file):
        for i, line in file:
            one_line = line.split(',')
            self.employees.append(Emplyee(i, one_line[0], one_line[1], one_line[2]))

    def make_structure(self, file):
        for line in file:
            one_line = str(line).split('->')
            for employee in self.employees:
                if employee.name == one_line[1]:
                    employee.supervisor = one_line[0]

    def add_team_to_organization(self, file):
        for line in file:
            one_line = str(line).split(': ')
            self.teams.append(Team(one_line[0]))
            for name in one_line[1].split(', '):
                for employee in self.employees:
                    if employee.name == name:
                        self.teams[-1].add_employee_to_team(employee)

    def having_the_same_supervisor(self, name1, name2):
        employees = [employee for employee in self.employees if employee.name == name1 or employee.name == name2]
        return employees[0].supervisor == employees[1].supervisor

    def print_team_sorted_by_age(self):
        for team in self.teams:
            team.sort_by_age()
            print(team.project + ': ')
            for employee in team:
                print(employee)

    def get_the_oldest(self):
        oldest = [employee for employee in self.employees if employee.age == max([employee.age for employee in self.employees])]
        return oldest

