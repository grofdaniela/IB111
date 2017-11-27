from __future__ import print_function

def powers(base,n):
    for i in range(n):
        result = 1
        for y in range(i):
            result *= base
        print(result)
def even_numbers(n):
    number=0
    for i in range(n):
        number += 2
        print(number)

def fibonacci(n):
    a=1
    b=0
    c=0
    for i in range(n):
       print(a)
       c=a
       a+=b
       b=c

def table_additions(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i+j, end=' ')
        print('')

def empty_square(n):
    for i in range(n):
        if i == 0 or i == n-1:
            for j in range(n):
                print('#', end=' ')
        else:
            for j in range(n):
                if j == 0 or j == n-1:
                    print('#', end = ' ')
                else:
                    print('.', end=' ')
        print('')

def sequence(n):
    a = 0
    b = 1
    print(a, b, end=' ')
    for _ in range(n-2):
        c = 5 * b - 4 * a
        a = b
        b = c
        print (c, end=' ')
sequence(10)



