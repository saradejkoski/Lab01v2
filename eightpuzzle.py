import random
import time
import copy
import math
from functions import *

# Global variable
variations = []


# Create a random puzzle arrangement
def create_puzzle():
    tiles = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    arrangement = []

    # Randomly select tiles and remove them from the list until there are none left
    for i in range(9):
        random_tile = random.choice(tiles)
        tiles.remove(random_tile)
        arrangement.append(random_tile)
    return arrangement


# Draw initial puzzle
def draw_puzzle_start(puzzle):
    # Iterate through the puzzle and print each number
    for i, number in enumerate(puzzle):
        print(" ", end="")
        print(number, end="")
        if (i + 1) % 3 != 0:
            print(" |", end="")
        else:
            print("\n", end="")


# Check if given puzzle is solveable
def check_solvability(checkPuzzle):
    evenOrOdd = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if checkPuzzle[i] != 0 and checkPuzzle[j] != 0 and checkPuzzle[i] > checkPuzzle[j]:
                evenOrOdd += 1

    return evenOrOdd % 2 == 0


# Create 100 solvable puzzle variations
def create100Variations():
    while len(variations) < 100:
        tempArray = create_puzzle()
        if check_solvability(tempArray):
            variations.append(tempArray)

    return variations


# Generate 100 solvable puzzles
def generate_puzzle_variations():
    variations = []
    while len(variations) < 100:
        temp_puzzle = create_puzzle()
        if check_solvability(temp_puzzle):
            variations.append(temp_puzzle)

    return variations


# Class to represent a puzzle state with Manhattan heuristic
class puzzleStateManhattan:

    def __init__(self, puzzle, manhattan_distance, generation, f_score):
        self.puzzle = puzzle
        self.manhattan_distance = manhattan_distance
        self.generation = generation
        self.f_score = f_score
        self.closed = False


# Class to represent a puzzle state with Hamming heuristic
class puzzleStateHamming:

    def __init__(self, puzzle, hamming_distance, generation, f_score):
        self.puzzle = puzzle
        self.hamming_distance = hamming_distance
        self.generation = generation
        self.f_score = f_score


# Class to show statistics of puzzle solving
class finishStats:

    def __init__(self, expansions, time):
        self.expansions = expansions
        self.time = time


# Function to solve the puzzle using Hamming heuristic
def hamming(puzzle):
    start = time.time()
    startState = puzzleStateHamming(puzzle, calculate_hamming_distance(puzzle), 0, calculate_hamming_distance(puzzle))
    expansions = [startState]
    open = [startState]

    # Run the A* search algorithm by expanding the search tree until a goal state is found
    while True:
        if expand(expansions, open, "hamming"):
            break

    # Calculate the elapsed time for the search and return the statistics for the final state
    end = time.time()
    elapsedTime = end - start
    return finishStats(len(expansions), elapsedTime)


# Function to solve the puzzle using the Manhattan heuristic
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


# Define a function to expand the search tree by generating new states from the current state
def expand(expansions, open_list, algorithm):
    # Select the state with the lowest f-score from the open list as the current state
    current_state = min(open_list, key=lambda x: x.f_score)
    puzzle = current_state.puzzle

    # Find the index of the blank tile in the puzzle
    blankIndex = puzzle.index(0)
    blankRow = blankIndex // 3
    blankColumn = blankIndex % 3
    generation = current_state.generation

    # Generate all possible moves by moving the blank tile in all directions
    moves = []
    if blankRow > 0:
        moves.append((-3, 'down'))
    if blankRow < 2:
        moves.append((3, 'up'))
    if blankColumn > 0:
        moves.append((-1, 'right'))
    if blankColumn < 2:
        moves.append((1, 'left'))

    # Generate new states from the current state by making each possible move
    for move in moves:
        new_puzzle = puzzle[:]
        new_puzzle[blankIndex] = new_puzzle[blankIndex + move[0]]
        new_puzzle[blankIndex + move[0]] = 0
        if addNewState(expansions, open_list, generation, new_puzzle, algorithm):
            return True

    open_list.remove(current_state)
    open_list = [s for s in open_list if s.generation != generation - 1]


# This function adds a new state to the search tree based on the specified puzzle and algorithm
# It returns True if the goal state has been reached
def addNewState(expansions, open, generation, puzzle, algorithm):
    # Calculate the h value based on the algorithm specified
    if algorithm == "manhattan":
        h = calculate_manhattan_distance(puzzle)
        state = puzzleStateManhattan(puzzle, h, generation + 1, h + generation)
    else:
        h = calculate_hamming_distance(puzzle)
        state = puzzleStateHamming(puzzle, h, generation + 1, h + generation)

    # Check if the puzzle has already been expanded, and if not, add the new state to expansions
    if not checkDuplicate(expansions, puzzle):
        expansions.append(state)
        open.append(state)
        if h == 0:
            return True

    return False


# Function to check if the puzzle has already been expanded
def checkDuplicate(expansions, puzzle):
    return any(x.puzzle == puzzle for x in expansions)
