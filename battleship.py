# Battleship! (from codecademy) for Python 2.7

from random import randint
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# print ship_row
# print ship_col

for turn in range(10):
    print
    print "Turn", turn + 1
    guess_r = int(raw_input("Guess Row (from 1 to 5): "))
    guess_row = guess_r - 1
    guess_c = int(raw_input("Guess Col (from 1 to 5): "))
    guess_col = guess_c - 1
    if guess_row == ship_row and guess_col == ship_col:
        print
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print
            print "Oops, that's not even in the ocean."
            print
        elif(board[guess_row][guess_col] == "X"):
            print
            print "You guessed that one already."
            print
        else:
            print
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print
        if turn == 9:
            print "Game Over"
            print "The correct location was (" + str(ship_row + 1) + "," + str(ship_col + 1) + ")"
            break
        turn + 1
        print_board(board)