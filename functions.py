import math


# https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
def is_puzzle_solvable(array):
    inversion_counter = 0
    empty_value = []

    for i in array:
        empty_value += i

    for i in range(8):
        for j in range(i + 1, 9):
            if empty_value[j] and empty_value[i] and empty_value[i] > empty_value[j]:
                inversion_counter += 1

    return inversion_counter % 2 == 0


def calculate_manhattan_distance(puzzle):
    manhattan_distance = 0

    for i in range(9):
        if puzzle[i] == 0:
            continue

        current_row = math.floor(i / 3)
        current_column = i % 3

        goal_row = math.floor(puzzle[i] / 3)
        goal_column = puzzle[i] % 3

        distance = abs(goal_row - current_row) + abs(goal_column - current_column)

        distance += distance

    return distance


def calculate_hamming_distance(puzzle):
    distance = 0

    for i in range(0, 9):
        if puzzle[i] != i:
            distance += 1

    return distance
