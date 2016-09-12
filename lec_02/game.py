# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    lst_numbers = range(1, 16)
    return random.sample(lst_numbers, len(lst_numbers)) + [EMPTY_MARK]


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for item in range(0, len(field), 4):
        print(field[item:item + 4])


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """

    if field == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x']:
        print_field(field)
        return True

    else:
        return False


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    index_EmptyMark = field.index(EMPTY_MARK)
    delta = MOVES[key]

    if (0 <= index_EmptyMark <= 3 and key == 'w') or \
        (12 <= index_EmptyMark <= 15 and key == 's') or \
            (index_EmptyMark % 4 == 0 and key == 'a') or \
            (index_EmptyMark % 4 == 3 and key == 'd'):
        raise IndexError

    new_index = index_EmptyMark + delta

    field[index_EmptyMark], field[new_index] = field[new_index], field[index_EmptyMark]

    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    while True:
        user_input = input("Enter next step ('w' - up, 's' - down, 'a' - left, 'd' - right): ")
        if user_input not in MOVES:
            print("Please enter only these letter ('w' - up, 's' - down, 'a' - left, 'd' - right)")
            continue
        else:
            return user_input


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    step = 0
    field = shuffle_field()
    while is_game_finished(field) is not True:
        print_field(field)
        try:
            user_input = handle_user_input()
            perform_move(field, user_input)
            step += 1
        except KeyboardInterrupt:
            print("\nShutting down. Your steps are {}".format(step))
            break
        except IndexError:
            print("Your step is out of field 4x4. Try again.")
    else:
        print("You are win. Your steps is {}".format(step))


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()
