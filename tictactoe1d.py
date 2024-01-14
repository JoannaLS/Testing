import random
from unittest.mock import patch

def print_board(board):
    print("".join(board))

def check_winner(board, mark):
    for i in range(len(board) - 2):
        if board[i:i+3] == [mark] * 3:
            return True
    return False

def player_move():
    return int(input("Please enter your move (1-20): ")) - 1

def pc_move():
    return random.randrange(21)

def tictactoe():
    board = ["-"] * 20
    mark = "X" or "O"

    print("This is the game board:")
    print_board(board)

    for play in range(20):  
        try:
            move = player_move()
            if move not in range(1, 21):
                print("That is not a valid number. Try again.")
            elif board[move] == "-":
                board[move] = mark
                print_board(board)

                if check_winner(board, mark):
                    print(f"Player {mark} wins!")
                    break

                pc_move = random.randrange(21)
                while board[pc_move] != "-":
                    pc_move = random.randrange(21)

                board[pc_move] = "O"
                print(f"Computer chose {pc_move + 1}")
                print_board(board)

                if check_winner(board, "O"):
                    print("Computer wins!")
                    break
            else:
                print("That position is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 20.")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    with patch('builtins.input', side_effect=["1", "3", "5", "7", "9", "11", "13", "15", "17", "19"]):
        tictactoe()
