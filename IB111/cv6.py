from __future__ import print_function
import random


def guess_number_human(upper_bound):
    my_num = random.randrange(upper_bound)
    guess = 0
    guess_num = 1
    while guess == 0:
        print(guess_num, '. pokus')
        number = int(input("Zadej svoj tip: "))
        if number > my_num:
            print('Moje cislo je mensie')
        elif number < my_num:
            print('Moje cislo je vacsie')
        else:
            print('Jop to je ono ')
            guess = 1
        guess_num += 1

# guess_number_human(10)


def guess_num_pc(upper_bound):
    the_range = [1,upper_bound]
    right_guess = 0
    while right_guess == 0:
        my_guess = (the_range[0] + the_range[1]) / 2
        print('Je cislo', my_guess, 'mensi (0), rovno (1), nebo vetsi (2) nez tvoje cislo?')
        result = int(input())
        if result == '0':
            right_guess = my_guess
        elif result == 0:
            the_range[0] = my_guess+1
            if the_range[1] - the_range[0] == 1:
                right_guess = my_guess + 1
        elif result == 2:
            the_range[1] = my_guess-1
            if the_range[1] - the_range[0] == 1:
                right_guess = my_guess - 1
    print('Tvoje cislo je', right_guess)
#guess_num_pc(10)

def binary_search(needle, haystack):
    the_list = haystack
    lower = 0
    upper = len(haystack)-1
    while lower != upper:
        if needle == the_list[(upper + lower)/2]:
            return (upper + lower)/2
        elif needle > the_list[(upper + lower)/2]:
            lower = (upper + lower)/2 + 1
        else:
            upper = (upper + lower)/2 - 1
    return -1
# print(binary_search(4, [1,4,5,6,7]))

def guess_num_pc_pc(upper_bound):
    the_num = random.randrange(1,upper_bound)
    the_range = [1, upper_bound]
    num_of_guess = 0
    right_guess = 0
    print(the_num)
    print('A: Myslim cislo od 1 do', upper_bound)
    while right_guess == 0:
        num_of_guess += 1
        print('--- Pokus c.',num_of_guess, '---')
        guess = sum(the_range)/2
        print('B: Tipujem', guess)
        if guess == the_num:
            right_guess = guess
        elif the_num < guess:
            print('A: Moje cislo je mensie')
            the_range[1]=guess
        else:
            print('A: Moje cislo je vacsie')
            the_range[0]= guess
    print('A: JO!')
    print('Uhadnute na', num_of_guess, 'pokusov')
# guess_num_pc_pc(10)



def number_of_coins(amount, coins):
    rest = amount
    result = 0
    while rest > 0:
        if rest - coins[-1] < 0:
            coins = coins[:-1]
        else:
            result += 1
            rest -= coins[-1]
    return result
#print(number_of_coins(6, [1, 3, 5]))
#print(number_of_coins(46, [1, 2, 5, 10, 20, 50]))

print(number_of_coins(8, [1,4,5]))