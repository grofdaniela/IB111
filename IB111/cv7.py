# from profilehooks import profile


def triangle(n):
    return [[1 for _ in range(i)] for i in range(1, n+1)]
# print(triangle(3))


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def binomial_coeff(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))


def pascal_binomial(n):
    return [[binomial_coeff(i, j) for j in range(i+1)] for i in range(n)]
# print(pascal_binomial(5))


def pascal(n):
    result = [[1]]
    for i in range(1, n+1):
        result.append([])
        result[i].append(1)
        result[i].extend([result[-2][j]+result[-2][j+1] for j in range(i-1)])
        result[i].append(1)
    return result if n != 0 else []


def print_pascal(pascal):
    max_number_size = len(str(pascal[-1][len(pascal) / 2])) + 2
    for row in pascal:
        line = ""
        for x in row:
            line += ("{0: ^" + str(max_number_size) + "}").format(x)
        print(("{0: ^" + str(max_number_size * len(pascal[-1])) + "}").format(line))
# print_pascal(pascal(7))

our_list = list([x for x in reversed(range(0,20))])


# def bubble_sort(list):
#     is_sorted = False
#     while not is_sorted:
#         is_sorted = True
#         for i in range(len(list)-1):
#             if list[i]>list[i+1]:
#                 list[i], list[i+1] = list[i+1], list[i]
#                 is_sorted = False
#     return list
# bubble_sort(our_list)


def bubble_sort(list):
    new_list = []
    while len(list) != 0:
        for i in range(len(list)-1):
            if list[i]>list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        new_list.append(list[-1])
        list = list[:-1]
    return new_list[::-1]

# bubble_sort(our_list)


def selection_sort(list):
    new_list = []
    while len(list) != 0:
        smallest_num_index = 0
        for i in range(len(list)):
            if list[i] < list[smallest_num_index]:
                smallest_num_index = i
        list[0], list[smallest_num_index] = list[smallest_num_index], list[0]
        new_list.append(list[0])
        list = list[1:]
    return new_list
# print(selection_sort(our_list))


def insert_sort(list):
    for i in range(1, len(list)):
        sorted_num = list[i]
        sorted_num_index = i
        while sorted_num_index > 0 and list[sorted_num_index-1] > sorted_num:
            list[sorted_num_index] = list[sorted_num_index-1]
            sorted_num_index = sorted_num_index -1
        list[sorted_num_index] = sorted_num
    return list
# print(insert_sort(our_list))


def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        last_sorted_index = 0
        for j in range(len(list)-1):
            if list[j+1] < pivot:
                list[j+1], list[last_sorted_index+1] = list[last_sorted_index+1], list[j+1]
                last_sorted_index += 1
        list[0], list[last_sorted_index] = list[last_sorted_index], list[0]
        smaller_than_pivot = quicksort(list[:last_sorted_index])
        larger_than_pivot = quicksort(list[last_sorted_index+1:])
        smaller_than_pivot.append(list[last_sorted_index])
        return smaller_than_pivot + larger_than_pivot
print(quicksort([1,4,3,5,3,1]))