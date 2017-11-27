from __future__ import print_function
import operator

def evaluate_postfix(input):
    stack = []
    list_of_tokens = input.split()
    for token in list_of_tokens:
        if token in '1234567890':
            stack.append(int(token))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = calculate(token, operand1, operand2)
            stack.append(result)
    return stack.pop()



def calculate(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


# print(evaluate_postfix("8 7 * 6 5 + 2 * +"))
dummy = """Monty Python and Monty Python all over here."""

def freq_analysis(text):
    my_dict = {}
    for sign in text:
        if sign in my_dict.keys():
            my_dict[sign] += 1
        else:
            my_dict[sign] = 1
    sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)
    return [sorted_dict[i][0] for i in range(len(sorted_dict))]
# print(freq_analysis(dummy))

#hra na 2D planu - piskvorky

#globalni promenna, delka pole
N = 3

# vygenerovani prazdneho hraciho planu
def empty_plan():
    return [[0 for i in range(N)]
            for j in range(N)]

# kontrola vyhry
def determine_winner(plan):
    for i in range(N):
        all_same = True
        for j in range(N):
            if plan[i][j] != plan[i][0]:
                all_same = False
        if all_same and plan[i][0] != 0:
            return plan[i][0]

        all_same = True
        for j in range(N):
            if plan[j][i] != plan[0][i]:
                all_same = False
        if all_same and plan[0][i] != 0:
            return plan[0][i]

    all_same = True
    for i in range(N-1):
        if plan[i][i] != plan[i+1][i+1]:
            all_same = False
    if all_same and plan[0][0] != 0:
        return plan[0][0]
    all_same = True
    for i in range(1, N):
        if plan[N-i][i-1] != plan[N-i-1][i]:
            all_same = False
    if all_same and plan[1][1] != 0:
        return plan[0][0]
    return 0


# vypis hraciho planu
def print_plan(plan):
    symbol = {0: ".", 1: "X", 2: "O"}
    for i in range(N):
        for j in range(N):
            print(symbol[plan[i][j]], end=" ")
        print()
    return


# funkce, ktera spusti hru
def play():
    plan = empty_plan()
    player = 1
    while determine_winner(plan) == 0:
        print_plan(plan)
        move = input("Player " + str(player) + " move x y:")
        x, y = list(map(int, move.split(" ")))
        plan[y - 1][x - 1] = player
        player = 3 - player
    print_plan(plan)
    print("Player " + str(determine_winner(plan)) + " wins.")
    return


play()