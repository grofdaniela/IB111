from company import Company
from colorama import Fore


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
    name = input('\tTell me name of employee to show all his/her subordinates. ')
    company_name.hierarchy(name)
    name = input('\n\tTell me name of employee to show number of his/her subordinates. ')
    print(company_name.number_of_subordinates(name))
    skills_to_check = input('\n\tWhat skills you want to check? (separate with space) ').split()
    company_name.missing_skills(skills_to_check)
    want_to_know = int(input('\n\tDo you want to know the eldest employee of company? *1 (yes) 0 (no)'))
    if want_to_know == 1:
        print(', '.join(company_name.get_the_oldest()))
    names = input('\n\tGive me two employees to check if they have same supervisor. (separate with space)').split()
    print('\n' + str(company_name.having_the_same_supervisor(names[0], names[1])))
    team = input('\nAverage age of which team you want to know? ')
    print(company_name.average_age(team))


if __name__ == '__main__':
    demo()


