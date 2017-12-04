from employee import Employee
from team import Team
from colorama import Fore
from pyfiglet import Figlet


class Company:
    def __init__(self, import_file, company_name):
        self.import_file = import_file
        self.name = company_name
        self.employees = []
        self.teams = []
        self.add_employees_to_organization(self.make_company()[0])
        self.make_structure(self.make_company()[1])
        self.add_team_to_organization(self.make_company()[2])

    def make_company(self):
        members = []
        structure = []
        teams = []
        list_of_files = [teams, structure, members]
        group = list_of_files.pop()
        with open(self.import_file) as file:
            for line in file:
                if line[0] == '#':
                    group = list_of_files.pop()
                    continue
                if line != '\n':
                    group.append(line.lower())
        return members, structure, teams

    def add_employees_to_organization(self, file):
        for line in file:
            one_line = line.split(',')
            self.employees.append(Employee(0, one_line[0], one_line[1], one_line[2]))

    def make_structure(self, file):
        for line in file:
            one_line = str(line).split('->')
            for employee in self.employees:
                if employee.name == one_line[1][:-1]:
                    employee.supervisor = one_line[0]

    def add_team_to_organization(self, file):
        for line in file:
            one_line = str(line).split(': ')
            self.teams.append(Team(one_line[0]))
            for name in one_line[1][:-1].split(', '):
                for employee in self.employees:
                    if employee.name == name:
                        self.teams[-1].add_employee_to_team(employee)

    def having_the_same_supervisor(self, name1, name2):
        employees = [employee for employee in self.employees if employee.name == name1 or employee.name == name2]
        return employees[0].supervisor == employees[1].supervisor


    def average_age(self, project):
        for team in self.teams:
            if team.project == project:
                return team.average_age()

    def print_team_sorted_by_age(self):
        for team in self.teams:
            team.sort_by_age()
            print(team.project + ': ')
            for employee in team:
                print(employee)

    def get_the_oldest(self):
        return [(employee.name + ' (born in ' + str(employee.birth_year) + ')') for employee in self.employees
                if employee.age == max([employee.age for employee in self.employees])]

    def find_birth_date(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee.birth_year

    def hierarchy(self, name, n=1):
        colors = {
            0: 'MAGENTA',
            1: 'YELLOW',
            2: 'BLUE',
            3: 'GREEN'
        }
        self.employees = sorted(self.employees, key=lambda employee: employee.name)
        if n == 1:
            print(Fore.RED + name.upper() + ' <' + str(self.find_birth_date(name)) + '>' + Fore.RESET)
        self.employees = sorted(self.employees, key=lambda employee: employee.name)
        for employee in self.employees:
            if employee.supervisor == name:
                print(eval('Fore.'+colors[n % 4]) + n*'\t' + employee.name[0].upper() + employee.name[1:] + ' <' + str(employee.birth_year) + '>' + Fore.RESET)
                self.hierarchy(employee.name, n+1)

    def number_of_subordinates(self, name, n=0):
        self.employees = sorted(self.employees, key=lambda employee: employee.name)
        for employee in self.employees:
            if employee.supervisor == name:
                n = self.number_of_subordinates(employee.name, n+1)
        return n

    def missing_skills(self, skills):
        for team in self.teams:
            if len(team.not_having_skills(skills)) > 0:
                print("{} team is missing {} skill.".format(team.project, ' and '.join(team.not_having_skills(skills))))

    def make_logo(self):
        f = Figlet(font="slant")
        print(Fore.RED + f.renderText(self.name) + Fore.RESET)

    def employees_names(self):
        return [employee.name for employee in self.employees]

    def teams_projects(self):
        return [team.project for team in self.teams]