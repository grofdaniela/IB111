from __future__ import print_function
import turtle

def sequence(n):
    a = 0
    b = 1
    c = 5 * b - 4 * a
    print(a, b, end=' ')
    for _ in range(n-2):
        x = c
        c = 5 * b - 4 * a
        a = b
        b = c
        print (c, end=' ')
sequence(10)
# g_products(15)

def part_of_tree(l):
    for i in range(1,l+1):
        for j in range(1,2*l):
            if i > j - l and j > l-i:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()
def tree(n,l):
    for _ in range(1,n+1):
        part_of_tree(l)
# tree(3,4)


def honey_bee(length, n):
    angle = 360/n
    for _ in range(n):
        for _ in range(n):
            turtle.forward(length)
            turtle.left(angle)
        turtle.forward(length)
        turtle.right(angle)
    turtle.done()
# honey_bee(34,5)

def show_figure(row, col, x, y):
    if x > row or y > col:
        print('[x,y] is out of coordinates.')
    else:
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if i == x and j == y:
                    print('o', end=' ')
                else:
                    print('#', end=' ')
            print()
# show_figure(5,7,3,4)