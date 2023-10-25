-------Simple Python Sudoku--------

->   Introduction

This repository contains a simple, console-based Sudoku game implemented in Python. The game allows players to interact with a text-based interface to solve a randomly generated Sudoku puzzle. It's designed as a fun and interactive way to engage with Sudoku puzzles directly in your console!

Libraries Used

The script primarily uses the following Python libraries:

random: This is used for generating random numbers, shuffling lists, and selecting random elements, crucial for creating the random Sudoku board each game.
numpy (optional): Though not required, numpy can be used for more efficient numerical operations if the board logic gets complex in future iterations.
These standard libraries help in randomizing elements within the game, ensuring that each new game provides a unique experience.

Function Descriptions

generate_board(): This function sets up a random Sudoku board, ensuring that the initial state adheres to Sudoku rules. It returns a 9x9 nested list representing the game board.

print_board(board): Accepts the current game board as an argument and prints it in the console in a readable format, allowing players to see the state of their game.

check_board(board): A basic function to visually check the board's state. It calls print_board(board) to display the board. This function can be expanded for more comprehensive game state validations.

play_game(): This is the main game loop that initializes the game board, accepts user inputs for their moves, and updates the board state accordingly



----------How to Play----------

Start the Game: Run the script in your terminal
The game will display a randomly generated Sudoku board with several numbers missing, indicating the start of a new game.

Making a Move: The game will prompt you to enter the row number, column number, and the value you want to insert. Here's how the prompt looks:
Enter row number (0-8): 
Enter column number (0-8): 
Enter the value (1-9): 

Game Progress: After each move, the updated board is printed to show the current game state. For example:

5 . . . . . . . .
. . . 7 9 . . . .
8 1 . . . . . . .
. . . . 5 . 8 . .
. . 4 . . . 2 . .
. . . . . . . . .
. . . . . 7 . . .
2 . . . . . . . .
. 4 . . . . . . .
Continue making moves by specifying the row, column, and value. The game currently does not have an end condition check, so you can keep playing as long as you want.

Sample Move: Here's a sample move and the corresponding output:
Enter row number (0-8): 0
Enter column number (0-8): 1
Enter the value (1-9): 3

5 3 . . . . . . .
. . . 7 9 . . . .
8 1 . . . . . . .
. . . . 5 . 8 . .
. . 4 . . . 2 . .
. . . . . . . . .
. . . . . 7 . . .
2 . . . . . . . .
. 4 . . . . . . .
The board reflects the new move, and you continue accordingly.

Remember, this version of the game is a simplified representation. It doesn't fully enforce Sudoku rules and doesn't notify the player of game completion. It's a starting point for Sudoku enthusiasts and developers to build upon!



