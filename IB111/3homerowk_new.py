import random


PLAN_WIDTH = 7
PLAN_HEIGHT = 5


def main():
    """
    A main function with the game logic, which is automatically executed when
    the script starts. This function uses all the functions defined below.
    """
    print("Hello. It's me. I was wondering if you would like to play a little game.\nOk, now seriously.\n")
    print("Asterisk marks default option (press Return to confirm).")
    while True:
        type_of_game = int(input("Would you like to play *Multiplayer (press 0) or Singleplayer (press 1)? ") or 0)
        if type_of_game in (0, 1):
            break
    while True:
        pc_strategy = int(input("Computer: Should I be smart? *Yes (1), No (0). ") or 1)
        if pc_strategy in (0, 1):
            break
    while True:
        who_starts = int(input("Who should start the game? *You (0) or me (1)? ") or 0)
        if who_starts in (0, 1):
            break
    game_plan = new_game_plan()
    show_game_plan(game_plan)
    print('May the Force be with you.')
    if type_of_game == 0:
        while is_playable(game_plan):
            row, col = get_player_input(game_plan)
            occupy(game_plan, row, col)
            show_game_plan(game_plan)
        else:
            print('Game finished.')
    else:
        if pc_strategy == 0:
            while is_playable(game_plan):
                if who_starts == 0:
                    row, col = get_player_input(game_plan)
                    occupy(game_plan, row, col)
                    show_game_plan(game_plan)
                if is_playable(game_plan):
                    row, col = computer_random_strategy(game_plan)
                    print('PC: My turn is ' + str(row) + ' ' + str(col))
                    occupy(game_plan, row, col)
                    show_game_plan(game_plan)
                    who_starts = 0
            else:
                print('Game finished.')
        else:
            while is_playable(game_plan):
                if who_starts == 0:
                    row, col = get_player_input(game_plan)
                    occupy(game_plan, row, col)
                    show_game_plan(game_plan)
                if is_playable(game_plan):
                    row, col, count_of_filled = computer_smart_strategy(game_plan)
                    print('PC: My turn is ' + str(row) + ' ' + str(col) +
                          ' because, obviously, I am smart and I can fill ' + str(count_of_filled) + ' positions there.')
                    occupy(game_plan, row, col)
                    show_game_plan(game_plan)
                    who_starts = 0
            else:
                print('Game finished.')


def new_game_plan():
    """
    Return a list of lists representing an initial (empty) game plan at the
    start of a new game. The availability of each square is a bool variable.
    Therefore, an empty plan of size 4 rows x 2 columns can be represented as:

    [
        [True, True, True, True],
        [True, True, True, True]
    ]

    or

    [
        [True, True],
        [True, True],
        [True, True],
        [True, True]
    ]

    Select whatever you prefer. (Is one option better than the other?)
    """
    return [[True for _ in range(PLAN_WIDTH)] for _ in range(PLAN_HEIGHT)]


def is_playable(game_plan):
    """
    Return True if the game plan contains at least one square that is free
    (not occupied). Otherwise return False.
    """
    for i in range(PLAN_HEIGHT):
        for j in range(PLAN_WIDTH):
            if game_plan[i][j]:
                return True
    return False


def show_game_plan(game_plan):
    """
    Graphically display the game plan. For example, an empty 4 x 2 plan can be
    displayed as:

    □□□□
    □□□□

    Select any representation (ASCII characters) you prefer. (You can even do
    Turtle graphics!)
    """
    print('\t'+'\t'.join([str(i) for i in range(PLAN_WIDTH)]))
    for i in range(PLAN_HEIGHT):
        print(i, end='\t')
        for j in range(PLAN_WIDTH):
            if not game_plan[i][j]:
                print("■", end="\t" )
            else:
                print("□", end="\t")
        print()

# show_game_plan(new_game_plan())


def get_player_input(game_plan):
    """
    Return a tuple of two indices representing the position (that is, the
    row and column index) that the player wants to occupy. The indices must
    be *valid* for the given game plan. For example, given a 4 x 2 plan,
    indices (1, 1) are valid, but indices (3, 2) are invalid. Moreover, the
    selected position must be free (not occupied).
    """
    while True:
        row = int(input("Select the row: "))
        col = int(input("Select the column: "))
        if row > PLAN_HEIGHT-1 or row < 0 or col > PLAN_WIDTH-1 or col < 0:
            print("Invalid input.")
        elif not (game_plan[row][col]):
            print("Invalid input.")
        else:
            return row, col


def occupy(game_plan, row, col):
    """
    Occupy a position on the game plan given by indices of the row and column.
    For example, after selecting indices (1, 1) on an empty 4 x 2 plan, that
    position, along with all the surrounding are occupied.

    If the plan would be printed afterward, it can look like this:

    ■■■□
    ■■■□
    """
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= j < PLAN_WIDTH and 0 <= i < PLAN_HEIGHT:
                game_plan[i][j] = False


def computer_random_strategy(game_plan):
    while True:
        row = random.randrange(0, PLAN_HEIGHT)
        col = random.randrange(0, PLAN_WIDTH)
        if game_plan[row][col]:
            return row, col


def computer_partial_smart_strategy(game_plan, row, col):
    num_to_fill = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= j < PLAN_WIDTH and 0 <= i < PLAN_HEIGHT:
                if game_plan[i][j]:
                    num_to_fill += 1
    return num_to_fill


def computer_smart_strategy(game_plan):
    best_move = [0, 0]
    best_move_value = 0
    for i in range(PLAN_HEIGHT):
        for j in range(PLAN_WIDTH):
            i_j_value = computer_partial_smart_strategy(game_plan, i, j)
            if i_j_value == 9:
                return i, j, 9
            elif best_move_value < i_j_value:
                best_move_value = i_j_value
                best_move = [i, j]
    return best_move[0], best_move[1], best_move_value


# Run the game by calling the main function after running the script
if __name__ == '__main__':
    main()
