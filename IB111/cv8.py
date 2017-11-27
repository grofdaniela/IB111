from __future__ import print_function
import turtle
import math


def series_sum(n):
    if n == 1:
        return 1
    else:
        return n + series_sum(n - 1)

# print(series_sum(100))


def sequence(n):
    if n == 0:
        return 5
    else:
        return 2 * sequence(n-1) - 1
# print(sequence(3))


def screwing(n):
    if n != 0:
        print('twist')
        screwing(n-1)
# screwing(3)


def list_sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + list_sum(list[1:])
# print(list_sum([1, 8, 2, 0, 4, 2]))



def binary_search(value, list):
    if len(list) == 0:
        return False
    else:
        bound = len(list)/2
        if value == list[bound]:
            return True
        else:
            if value < list[bound]:
                return binary_search(value, list[:bound])
            else:
                return binary_search(value, list[bound + 1:])
# print(binary_search(4, [1, 2, 5, 8]))



def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n-1, source, auxiliary, target)
        print(source, '->', target)
        hanoi(n-1, auxiliary, target, source)
# hanoi(3, 'Odtial', 'Sem', 'Pomocou')

def min_max(list):
    if len(list) <= 2:
        return min(list), max(list)
    first_half = min_max(list[:len(list)/2])
    second_half = min_max(list[len(list)/2:])
    return min(min(first_half), min(second_half)), max(max(first_half), max(second_half))

# print(min_max([1,3,2,9,4,9,2]))

def print_square(lenght):
    for i in range(4):
        turtle.forward(lenght)
        turtle.right(90)
# print_square(100)


def nested_squares(depth, length):
    if depth > 0:
        print_square(length)
        turtle.forward(length/2)
        turtle.right(45)
        new_lenght = int(math.sqrt(2*(length/2)**2))
        nested_squares(depth-1, new_lenght)
        turtle.bye()
# nested_squares(3,300)

def tree(lenght, n):
    if n > 0:
        turtle.forward(lenght/2)
        turtle.right(45)
        tree(lenght/2,n-1)
    turtle.done()
tree(100,4)