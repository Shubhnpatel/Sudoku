import numpy as np
import random


# Sudoku board generation
def generate_board():
    base = 3
    side = base * base

    # pattern for a baseline valid solution
    def pattern(r, c): return (base * (r % base) + r // base + c) % side

    def shuffle(s): return random.sample(s, len(s))

    r_base = range(base)
    rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(range(1, base * base + 1))

    # produce board using randomized baseline pattern
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    for _ in range(random.randint(40, 50)):  # Removing random numbers to create the puzzle
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        board[row][col] = 0

    return board


# Printing the board
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print()


# Check if the current state of the board is valid
def check_board(board):
    print_board(board)
    return True  # This is just a basic visual check. More advanced validity checks can be added


# Main game loop
def play_game():
    board = generate_board()
    while True:
        if check_board(board):
            # Get user input here
            try:  # Adding a try/except block to handle user input errors
                row = int(input("Enter row number (0-8): "))
                col = int(input("Enter column number (0-8): "))
                val = int(input("Enter the value (1-9): "))

                # Basic input validation, you can add more rules specific to Sudoku
                if 0 <= row < 9 and 0 <= col < 9 and 1 <= val <= 9:
                    board[row][col] = val  # Set the value on the board
                else:
                    print("Invalid input, please try again.")
            except ValueError:  # In case of non-integer inputs
                print("Invalid input, please enter an integer.")

        # The game doesn't end. You might want to implement a check for game completion
        # And break the loop when the game is solved


if __name__ == "__main__":
    play_game()
