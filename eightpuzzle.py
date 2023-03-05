import random
import time
import copy
import math
from functions import *

variations = []


def create_puzzle():
    tiles = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    arrangement = []

    for i in range(9):
        random_tile = random.choice(tiles)
        tiles.remove(random_tile)
        arrangement.append(random_tile)
    return arrangement


def draw_puzzle_start(puzzle):
    for i, number in enumerate(puzzle):
        print(" ", end="")
        print(number, end="")
        if (i + 1) % 3 != 0:
            print(" |", end="")
        else:
            print("\n", end="")


def check_solvability(checkPuzzle):
    evenOrOdd = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if checkPuzzle[i] != 0 and checkPuzzle[j] != 0 and checkPuzzle[i] > checkPuzzle[j]:
                evenOrOdd += 1

    return evenOrOdd % 2 == 0


def create100Variations():
    while len(variations) < 100:

        tempArray = create_puzzle()

        if check_solvability(tempArray):
            variations.append(tempArray)

    return variations


def generate_puzzle_variations():
    variations = []
    while len(variations) < 100:
        temp_puzzle = create_puzzle()
        if check_solvability(temp_puzzle):
            variations.append(temp_puzzle)

    return variations


class puzzleStateManhattan:

    def __init__(self, puzzle, manhattan_distance, generation, f_score):
        self.puzzle = puzzle
        self.manhattan_distance = manhattan_distance
        self.generation = generation
        self.f_score = f_score
        self.closed = False


class puzzleStateHamming:

    def __init__(self, puzzle, hamming_distance, generation, f_score):
        self.puzzle = puzzle
        self.hamming_distance = hamming_distance
        self.generation = generation
        self.f_score = f_score


class finishStats:

    def __init__(self, expansions, time):
        self.expansions = expansions
        self.time = time


def hamming(puzzle):
    start = time.time()
    startState = puzzleStateHamming(puzzle, calculate_hamming_distance(puzzle), 0, calculate_hamming_distance(puzzle))
    expansions = [startState]
    open = [startState]

    while True:
        if expand(expansions, open, "hamming"):
            break

    end = time.time()
    elapsedTime = end - start
    return finishStats(len(expansions), elapsedTime)


def manhattan(puzzle):
    start = time.time()
    startState = puzzleStateManhattan(puzzle, calculate_manhattan_distance(puzzle), 0,
                                      calculate_manhattan_distance(puzzle))
    expansions = [startState]
    open_list = [startState]

    while True:
        if expand(expansions, open_list, "manhattan"):
            break

    end = time.time()
    elapsed_time = end - start
    return finishStats(len(expansions), elapsed_time)


def expand(expansions, open_list, algorithm):
    current_state = min(open_list, key=lambda x: x.f_score)
    puzzle = current_state.puzzle
    blankIndex = puzzle.index(0)
    blankRow = blankIndex // 3
    blankColumn = blankIndex % 3
    generation = current_state.generation

    moves = []
    if blankRow > 0:
        moves.append((-3, 'down'))
    if blankRow < 2:
        moves.append((3, 'up'))
    if blankColumn > 0:
        moves.append((-1, 'right'))
    if blankColumn < 2:
        moves.append((1, 'left'))

    for move in moves:
        new_puzzle = puzzle[:]
        new_puzzle[blankIndex] = new_puzzle[blankIndex + move[0]]
        new_puzzle[blankIndex + move[0]] = 0
        if addNewState(expansions, open_list, generation, new_puzzle, algorithm):
            return True

    open_list.remove(current_state)
    open_list = [s for s in open_list if s.generation != generation - 1]


def addNewState(expansions, open, generation, puzzle, algorithm):
    if algorithm == "manhattan":
        h = calculate_manhattan_distance(puzzle)
        state = puzzleStateManhattan(puzzle, h, generation + 1, h + generation)
    else:
        h = calculate_hamming_distance(puzzle)
        state = puzzleStateHamming(puzzle, h, generation + 1, h + generation)

    if not checkDuplicate(expansions, puzzle):
        expansions.append(state)
        open.append(state)
        if h == 0:
            return True

    return False


def checkDuplicate(expansions, puzzle):
    return any(x.puzzle == puzzle for x in expansions)
