from company import Company
from colorama import Fore, init as colorama_init
colorama_init()


def demo():
    """
    :param file_path:
    :param company_name:
    :return:
    """
    print(Fore.CYAN + '\nNow you will experience the true power of Mordor.\nSit tight and watch the magic.'
          + Fore.RESET)
    file_path = input('\n\tTell me path to import file. ')
    company_name = input('\tTell me name of the company you want to create. ')
    company_name = Company(file_path, company_name)
    print(Fore.CYAN + 'This is a logo of your company. ')
    company_name.make_logo()
    while True:
        name = input('\tTell me name of employee to show all his/her subordinates. ').lower()
        if name in company_name.employees_names():
            break
        else:
            print('There is no such employee as ' + name)
    company_name.hierarchy(name)
    while True:
        name = input('\n\tTell me name of employee to show number of his/her subordinates. ').lower()
        if name in company_name.employees_names():
            break
        else:
            print('There is no such employee as ' + name)
    print(Fore.CYAN + str(company_name.number_of_subordinates(name)) + Fore.RESET)
    skills_to_check = input('\n\tWhat skills you want to check? (separate with space) ').lower().split()
    company_name.missing_skills(skills_to_check)
    while True:
        want_to_know = int(input('\n\tDo you want to know the eldest employee of company? *1 (yes) 0 (no)') or 1)
        if want_to_know in [0, 1]:
            break
        print('Invalid input. ')
    if want_to_know == 1:
        print(Fore.CYAN + ', '.join(company_name.get_the_oldest()) + Fore.RESET)
    while True:
        names = input('\n\tGive me two employees to check if they have same supervisor. (separate with space)').split()
        if len(names) == 2:
            if names[0] == names[1]:
                print('Ofc he/she has the same. OMG. ')
            elif names[0] in company_name.employees_names() and names[1] in company_name.employees_names():
                break
            else:
                print('Try different names. ')
        else:
            print('Give me 2 people. ')
    print(Fore.CYAN + '\n' + str(company_name.having_the_same_supervisor(names[0], names[1])) + Fore.RESET)
    while True:
        team = input('\nAverage age of which team you want to know? ').lower()
        if team in company_name.teams_projects():
            break
        else:
            print('There is no such team as ' + team + '. Try again. ')
    print(Fore.CYAN + str(company_name.average_age(team)) + Fore.RESET)


if __name__ == '__main__':
    demo()


