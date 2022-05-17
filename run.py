"""
board_size = 10


def create_game_board(game_board):
    print(f"    {board_size}")
    print("    -----------------")


    for row in range(9):
        game_board.append(["-"] * 9)
    letter = 0
    for letter in range(8):
        print(chr(letter + 65), end=" | ")
        for column in range(len(game_board[letter])):
            print(game_board[letter][column], end=" ")
        print("| ")
        letter += 1

    print("    -----------------")


game_board = []
create_game_board(game_board)
"""
"""
# the hidden board is the players board were they place thier battleships
hidden_board = [[" "] * 8 for x in range(8)]
#the guess board houses the computers ship locations and you guess were they are
guess_board = [[" "] * 8 for x in range(8)]

letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7 }

def print_board(board):
    print("  A B C D E F G H")
    print("  ---------------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
# 
def create_the_ships():
    pass

# we will ask the user for what row and column they want guess were the enemy ship is
def get_ship_location ():
    pass
# will count every time a ship is hit and if all 5 ships are hit then the game is over
def count_hit_ships():
    pass

create_the_ships()
turns = 10
#while turns > 0 :

"""
#to change size i will have to append and slice the lists
'''
row_number = [0, 0, 0, 0, 0, 0,]
column = [0, 0, 0, 0, 0, 0]
for row in row_number:
    print("|")
    for col in column:
        print("x", end="")
        
 print("    -----------------")
'''
game_board=[]
column = [0, 0, 0, 0, 0, 0]
print(str(range(0,8)))
for row in range(9):
    game_board.append(["-"] * 9)

letter = 0
for letter in range(8):
    print(chr(letter + 65), end=" | ")
    #  for column in range(len(game_board[letter])):
    #       print(game_board[letter][column], end=" ")
    for col in column:
        print(f" {col}", end="  ")

    print("| ")
    letter += 1

print("  -----------------")