from __future__ import print_function
import random

def dice():
    return random.randint(1, 6)
# print(dice(), dice(), dice())


def turn():
    result = 0
    n = dice()
    while n % 2 == 0:
        result += n
        n = dice()
    return result
# print(turn())


def dice_freq(count, lower, upper):
    sum_of_nums = 0
    list_of_numbers = []
    for _ in range(count):
        list_of_numbers.append(random.randint(lower, upper))
    print(list_of_numbers)
    list_of_numbers.sort()
    mean = float(sum(list_of_numbers))/count
    if count % 2 != 0:
        median = list_of_numbers[count/2]
    else:
        median = (list_of_numbers[count/2] + list_of_numbers[(count/2)-1])/float(2)
        median = round(median, 2)

    return list_of_numbers[0], list_of_numbers[-1], mean, median
#print(dice_freq(9,1,10))


def one_step(distance, position):
    print('home', end=' ')
    for i in range(distance):
        if i == position:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print('pub')


def drunkman_simulator(distance, steps_to_sleep):
    position = distance // 2
    result = 0
    for i in range(1, steps_to_sleep+1):
        one_step(distance, position)
        if position == 0 or position == distance-1:
            break
        position += random.choice([-1, 1])
    return result
#drunkman_simulator(10,100)

def drunkman_analysis(distance, steps_to_sleep, reps):
    home = 0
    pub = 0
    for _ in range(reps):
        x = drunkman_simulator(distance, steps_to_sleep)
        if x == 1:
            home += 1
        elif x == -1:
            pub += 1
    print('Arriving home in', (home / reps) * 100, '% of cases.\nArriving to pub in ', (pub / reps) * 100, '% of cases.')
# drunkman_analysis(10, 100, 100)


def treasure_hunter(width, steps):
    result = 0
    treasure = (random.randint(0, width-1), random.randint(0, width-1))
    position = (0, 0)
    for _ in range(1, steps+1):
        if position == treasure:
            return True
        else:
            step = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            if position[0] + step[0] >= 0 and position[0] + step[0] <= width and position[1] + step[1] >= 0 and position[1] + step[1] <= width:
                position = position[0] + step[0], position[1] + step[1]
    return False
#print(treasure_hunter(10,100))


def treasure_hunter_analysis(width, steps, count):
    found_it = 0
    for _ in range(count):
        found_it += treasure_hunter(width, steps)
    print('Treasure found in ', (found_it/float(count))*100, '% of cases.')
treasure_hunter_analysis(10,100,100)