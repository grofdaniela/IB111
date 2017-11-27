from __future__ import print_function
import copy

my_list = [6, 5, 11, 8]


def my_sum(list):
    result = 0
    for num in list:
        result += num
    return result
# print(my_sum(my_list))


def my_max(list):
    result = 0
    for num in list:
        if num > result:
            result = num
    return result
# print(my_max(my_list))


def my_in(x, list):
    for num in list:
        if x == num:
            return True
    return False
# print(my_in(3, my_list))


def nonzero_product(list):
    result = 1
    for num in list:
        if num != 0:
            result *= num
    return result
# print(nonzero_product([0, 0]))


def doubled_all(list):
    for i in range(len(list)):
        list[i] = list[i]*2
    return list
# my_list = doubled_all(my_list)
# print(my_list)


def create_double(list):
    new_list = copy.deepcopy(list)
    for i in range(len(list)):
        new_list[i] = list[i]*2
    return new_list
# b = create_double(my_list)
# print(my_list)
# print(b)


def flatten(list):
    result = []
    for sub_list in list:
        for num in sub_list:
            result.append(num)
    return result
# print(flatten([[2,3],[2]]))


def dummy(text, rubbish):
    result = ''
    for znak in text:
        result += znak
        result += rubbish
    return result[:-len(rubbish)]
# print(dummy('terez', 'XxX'))


def duplication(text):
    result = ''
    for znak in text:
        result += znak + znak
    return result
# print(duplication('lalala'))


def reverse(text):
    result = ''
    for i in range(1,len(text)+1):
        result += text[-i]
    return result
# print(reverse('ahoj'))


def censoship(text):
    result = ''
    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i]
        else:
            result += 'X'
    return result
# print(censoship('ahooooj'))


def count_a(text):
    result = 0
    for znak in text:
        if znak == 'a' or znak == 'A':
            result += 1
    return result
# print(count_a('Ahoj anjelik'))


def string_intersection(left, right):
    result = ''
    for i in range(len(right)):
        if right[i] == left[i]:
            result += right[i]
    return result
# print(string_intersection('ZIRAFA', 'KAFA'))


def diff_a(first, second):
    count_first = 0
    count_second = 0
    for znak in first:
        if znak == 'a' or znak == 'A':
            count_first += 1
    for znak in second:
        if znak == 'a' or znak == 'A':
            count_second += 1
    if count_first < count_second:
        print("First string contains less 'a'/'A':", abs(count_first-count_second))
    elif count_first > count_second:
        print("Second string contains less 'a'/'A':", abs(count_first - count_second))
    else:
        print("Both strings contain same number of 'a'/'A'")
# diff_a("", "")


def palindrom(text):
    if text == text[::-1]:
        return True
    return False
# print(palindrom('JELENOVIPIVONELEJ'))


def word_value(text):
    result = 0
    for znak in text:
        result += ord(znak) - 64
    return result
# print(word_value('AHOJ'))


def tuple_reverse(text, n):
    new_text = ''
    for i in range(0, len(text), n):
        if i == 0:
            new_text += text[n-1::-1]
        else:
            new_text += text[n+i-1:i-1:-1]
    return new_text

# print(tuple_reverse('HESLOJETAJEMNO', 3))


def search(needle, haystack):
    for i in range(len(haystack)):
        if needle == haystack[i:len(needle)+i]:
            return i
        else:
            return -1

print(search('tri','brati'))