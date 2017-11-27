from employee import Employee
from team import Team
from company import Company

if __name__ == '__main__':
    moneyhell = Company('import.txt')
    moneyhell.hierarchy('Elon')
    print(moneyhell.number_of_subordinates('Patricia'))
    moneyhell.missing_skills(['sql', 'test'])

