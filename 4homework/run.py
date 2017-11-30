from company import Company
from colorama import Fore


def demo(file_path, company_name):
    """
    :param file_path:
    :param company_name:
    :return:
    """
    print(Fore.CYAN + '\nNow you will experience the true power of Mordor.\nSit tight and watch the magic.'
          + Fore.RESET)
    company_name = Company(file_path, company_name)
    company_name.make_logo()
    print(Fore.CYAN + '\nThere is whole hierarchy of company: ' + Fore.RESET)
    company_name.hierarchy('Elon')
    print(Fore.CYAN + '\nNumber of subordinates of Patricia: ' + Fore.RESET, end='')
    print(str(company_name.number_of_subordinates('Patricia')))
    print(Fore.CYAN + '\nTeams that missing skills sql and test: ' + Fore.RESET)
    company_name.missing_skills(['sql', 'test'])
    print(Fore.CYAN + '\nThe eldest employee{} '.format(' is' if len(company_name.get_the_oldest()) == 1 else 's are')
          + Fore.RESET, end='')
    print(', '.join(company_name.get_the_oldest()))
    print(Fore.CYAN + '\nDo Helen and Mark have the same supervisor?' + Fore.RESET, end=' ')
    print(company_name.having_the_same_supervisor('Helen', 'Mark'))
    print(Fore.CYAN + '\nAnd do Anna and Janet have the same supervisor?' + Fore.RESET, end=' ')
    print(company_name.having_the_same_supervisor('Anna', 'Janet'))
    print(Fore.CYAN + '\nAverage age of members of Support team is ' + Fore.RESET, end='')
    print(company_name.average_age('Support'))


if __name__ == '__main__':
    demo('import.txt', 'moneyhell')


