from employee import Employee


class Team:
    def __init__(self, project):
        self.project = project
        self.members = []

    def add_employee_to_team(self, employee):
        self.members.append(employee)

    def average_age(self):
        age = [employee.age for employee in self.members]
        return sum(age)/len(self.members)

    def sort_by_age(self):
        self.members = sorted(self.members, key=lambda employee: employee.age)

    def having_skills(self, skill):
        for employee in self.members:
            if skill in employee.skills:
                return True
        return False
