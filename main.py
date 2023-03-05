from eightpuzzle import *


# Define a function called "menu" that prints out a list of options for solving a puzzle using different heuristic search algorithms
def menu():
    # Print out a title and the available options to the user
    print("---------------------------------------------------------------------------------")
    print("Eight Puzzle Implementation using Heuristic Search: ")
    print("---------------------------------------------------------------------------------")
    print("Choose a number from 1 to 5:")
    print("1. Solve the puzzle using the Manhattan Heuristic:")
    print("2. Solve the puzzle using the Hamming Heuristic:")
    print("3. Solve 100 puzzles using the Manhattan Heuristic: ")
    print("4. Solve 100 puzzles using the Hamming Heuristic:")
    print("5. Quit. ")
    print("---------------------------------------------------------------------------------")

    # Set the initial value of "choice" to 0
    choice = 0

    # Use a while loop to continually prompt the user for a choice until a valid choice is made
    while choice < 1 or choice > 5:
        try:
            # Try to get a choice from the user and convert it to an integer
            choice = int(input("Choose Option: "))
        except ValueError as ve:
            # If the user enters something that can't be converted to an integer, catch the error and print a message
            print("Please enter a number!")
        # If the user selects option 1, solve the puzzle using the Manhattan heuristic
        if choice == 1:
            printStatsInfo(manhattan(create100Variations()[0]))
            # Display the menu again and prompt the user for another choice
            menu()
            choice = (input("Enter an integer between 1-5: "))
        # If the user selects option 2, solve the puzzle using the Hamming heuristic
        elif choice == 2:
            printStatsInfo(hamming(create100Variations()[0]))
            # Display the menu again and prompt the user for another choice
            menu()
            choice = (input("Enter an integer between 1-5: "))
        # If the user selects option 3, solve 100 puzzles using the Manhattan heuristic
        elif choice == 3:
            puzzles = create100Variations()
            stats = []
            for x in puzzles:
                # Append the stats for each puzzle to a list
                stats.append(manhattan(x))
                # Print out the index of each puzzle
                print(puzzles.index(x), end=" ")
                if puzzles.index(x) == 49:
                    # Print a newline character after every 50 puzzles
                    print()
            # Print out the stats for all 100 puzzles
            print("\n" + "Manhattan (x100)")
            printAllStats(stats)
            # Display the menu again and prompt the user for another choice
            menu()
            choice = (input("Enter an integer between 1-5: "))

        # If the user selects option 4, solve 100 puzzles using the Hamming heuristic
        elif choice == 4:
            puzzles = create100Variations()
            stats = []
            for x in puzzles:
                # Append the stats for each puzzle to a list
                stats.append(hamming(x))
                # Print out the index of each puzzle
                print(puzzles.index(x), end=" ")
                if puzzles.index(x) == 49:
                    # Print a newline character after every 50 puzzles
                    print()
            # Print out the stats for all 100 puzzles
            print("\n" + "Hamming (x100)")
            printAllStats(stats)
            # Display the menu again and prompt the user for another choice
            menu()
        elif choice == 5:
            quit()



def printStatsInfo(stats):
    print("Expansions: " + str(stats.expansions))
    print("Time taken: " + str(round(stats.time, 3)))
    print()


def printAllStats(stats):
    expansions = 0
    time = 0
    expansionsList = []
    timeList = []



    for x in stats:
        expansions += x.expansions
        time += x.time
        expansionsList.append(x.expansions)
        timeList.append(x.time)


    expansionsMean = expansions / 100
    timeMean = time / 100

    print("Expansions [total/mean]: " + str(expansions) + " / " + str(expansionsMean))
    print("Time [total/mean]: " + str(round(time, 3)) + " / " + str(round(timeMean, 3)))
    print()


if __name__ == '__main__':
    menu()
