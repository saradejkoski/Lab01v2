import math


# https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
def is_puzzle_solvable(array):
    inversion_counter = 0  # initialize a variable to count inversions
    empty_value = []  # empty list --> to store puzzle

    for i in array:
        empty_value += i  # 2D array into 1D list

    # use loops to count the number of inversions
    for i in range(8):
        for j in range(i + 1, 9):
            if empty_value[j] and empty_value[i] and empty_value[i] > empty_value[j]:
                inversion_counter += 1

    # if puzzle is solvable --> return true (inversion count is even), otherwise false
    return inversion_counter % 2 == 0


def calculate_manhattan_distance(puzzle):
    manhattan_distance = 0
    # use loop --> to calculate the Manhattan distance for each tile
    for i in range(9):
        if puzzle[i] == 0:
            continue

        current_row = math.floor(i / 3)  # calculate the current row of the tile
        current_column = i % 3  # calculate the current column of the tile

        goal_row = math.floor(puzzle[i] / 3)  # calculate the goal row of the tile
        goal_column = puzzle[i] % 3  # calculate the goal column of the tile

        distance = abs(goal_row - current_row) + abs(goal_column - current_column)  # calculate --> Manhattan distance

        distance += distance

    return distance  # return --> total Manhattan distance


def calculate_hamming_distance(puzzle):
    distance = 0  # a variable to store --> Hamming distance
    # use loop --> to calculate the Hamming distance for each tile
    for i in range(0, 9):
        if puzzle[i] != i:
            distance += 1  # increase the Hamming distance --> if tile is not in the correct position

    return distance  # return --> total Hamming distance
