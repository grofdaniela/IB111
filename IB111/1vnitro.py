from __future__ import print_function
import random


def digit_sum(n):
    """
    Calculate sum of digit in number
    :param n: import number
    :return: x = digit sum
    """
    x = 0
    while(n>0):
        x += n % 10
        n = n / 10
    return x


def evenciphersum(n):
    """
    Calculate sum of numbers that has even digit sum
    :param n: Upper bound
    :return: sum of numbers
    """
    result = 0
    for i in range(n+1):
        if digit_sum(i) % 2 == 0:
            result += i
    return result
# print(evenciphersum(24))


def tabulka(n):
    """
    Print table n x n
    :param n:
    :return:
    """
    for i in range(1, n+1):
        num_to_print = 1
        for _ in range(n):
            print(num_to_print, end='')
            if num_to_print == i:
                num_to_print = 1
            else:
                num_to_print += 1
        print()
# tabulka(9)

def test(text1, text2):
    """
    Print signs that are on the same position in both text
    :param text1:
    :param text2:
    :return: string
    """
    result = ''
    for i in range(len(text1)):
        if text1[i] == text2[i]:
            result += text1[i]
    return result
# print(test("Programovani nas dost bavi", "Prezit to chceme ve zdravi"))

def nearest(list, value):
    """
    Find the nearest value in list
    :param list:
    :param value:
    :return:
    """
    result = list[0]
    for num in list:
        if abs(result - value) > abs(num - value):
            result = num
    return print(result)
# nearest([1, 6, 7, 9, 0, 1, 12, 50], 1)

def gen_hist(n, x, y):
    """
    Make a histogram of random numbers
    :param n:
    :param x:
    :param y:
    :return:
    """
    dict = {}
    for j in range(x, y+1):
        dict[j] = 0
    for _ in range(n):
        ran_num = random.randrange(x, y+1)
        dict[ran_num] += 1
    for j in range(x, y+1):
        print(j, end=' ')
        for _ in range(dict[j]):
            print('#', end='')
        print()
# gen_hist(20, 1,5)

def gen_hist_2(n,x,y):
    """
    :param n:
    :param x:
    :param y:
    :return:
    """
    dict = {}
    for j in range(x, y+1):
        dict[j] = 0
    for _ in range(n):
        ran_num = random.randrange(x, y+1)
        dict[ran_num] += 1
    for i in reversed(range(max(dict.values())+1)):
        for j in range(x, y+1):
            if i == 0:
                print(j, end=' ')
            elif dict[j] >= i:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()


gen_hist_2(20,1,5)