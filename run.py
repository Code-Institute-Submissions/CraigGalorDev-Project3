import random

# creating the global variables
# the player sets the numerical value of the board size
# this then sets the size of the playable board size to be displayed
board_size = 6
# player board displays were the player positioned thier ships and updated information miss and hits 
player_board = []
# only the pseudo board is displayed on screen showing only updated miss and hits 
# the com board has the ships locations
com_board = []
com_pseudo_board = []
# in this basic version of battleships each ship equals a life 
# when all 4 lives/ships are gone its game over
player_lives = 4
com_lives = 4
# these dictionaries will hold the positions of the ships location on the board
player_ships = {'battleship': [], 'destroyer': [], 'submarine': [], 'patrol boat': []}
com_ships = {'battleship': 0, 'destroyer': 0, 'submarine': 0, 'patrol boat': 0}

def random_num():
    '''
    random number generator to  set the com ships location and for com guess
    '''
    in_range = True
    while in_range:
        num = round((random.random()) * 10, )
        if num in range(0, 6):
            in_range = False

    return num

def get_board_size():

    board_set = True
    while board_set:
        print("\nSelect a board size: A number between 5-14")
        count = int(input())
        if count in range(5, 15):
            print("good choice")
            count += 1 
            board_set = False
        else:
            print("\nsorry that is an incorrect value")
            print("you need to pick a number between 5-14")
    return count

def set_board_size():       
    for x in range(board_size):
        player_board.append([])
        com_board.append([])
        for y in range(board_size):
            player_board[x].append([' - '])
            com_board[x].append([' - '])
            
def set_ships():
    #this is the conditional so that ships do not occupy the same space
    print("Please select the locations of your ships")
    
    last_boat = []
    for key, value in player_ships.items():
        ship = key
        selection = True
        while selection:
            print("\n" + f"select {ship} position")
            column = board_size
            column -= 1
            print(f"please select a column from 0 to {column}")
            col_pick = True
            while col_pick:
                col = int(input())
                if col not in range(0, board_size):
                    print("nope out of range try again")
                else:
                    col_pick = False
            rows = board_size
            rows -= 1        
            print(f"please select a row from 0 to {rows}")
            row_pick = True
            while row_pick:
                row = int(input())
                if row not in range(0, board_size):
                    print("nope out of range, try again")
                else:
                    row_pick = False
            boat = row, col
            check = 0
            for x in range(len(last_boat)):
                if boat == last_boat[x]:
                    check += 1 
            if check > 0:
                print("\nThis position is taken sailor\n")
            else:
                print("\nYep, looks good setting up here captain\n")
                last_boat.append(boat)
                check = 0
                selection = False
        player_ships[key] = [col], [row]
        print("")
        print("your current ship locations")
        print(player_ships)
        player_board[row][col] = [' @ ']
        display_ships()

def set_com_ships():
    col = random_num()
    row = random_num()
    print(col)
    print(row)
    com_board[row][col] = [' @ ']
    display_ships()
    print(player_ships)
    
    
def display_ships():
    print("")
    print("Display boards")
    blue = True
    while blue:
        
        print("To display players board select 'p'")
        print("To display computers board select 'c'")
        print("To skip board display select 's'")
        selection = input()
        if selection == 'p':
            print("\n")
            print("   Player Board")
            print("  ", end=" ")
            for x in range(board_size):
                
                print('-----', end="-")
            print("")
            print("")
            print("  ", end=" ")
            for x in range(board_size):
                
                print(f'  {x}', end="   ")
            print("")
            print("")
            for x in range(board_size):
                print(f'{x}', end=" | ")
                for y in range(board_size):
                    print(f'{player_board[x][y][0]}', end=" | ")
                print("")
                print("")

        elif selection == 'c':
            print("\n")
            print("   Computers Board")
            print("  ", end=" ")
            for x in range(board_size):
                
                print('-----', end="-")
            print("")
            print("")
            print("  ", end=" ")
            for x in range(board_size):
                
                print(f'  {x}', end="   ")
            print("")
            print("")
            for x in range(board_size):
                print(f'{x}', end=" | ")
                for y in range(board_size):
                    print(f'{com_board[x][y][0]}', end=" | ")
                print("")
                print("")
        elif selection == 's':
            print("")
            blue = False
        else:
            print("that selection is not supported")

def main():
    board_size = get_board_size()
    set_board_size()
    display_ships()
    set_ships()
    '''
    print("\n")
    print("Player Board")
    print("  ", end=" ")
    for x in range(board_size):
        
        print('-----', end="---")
    print("")
    print("")
    print("  ", end=" ")
    for x in range(board_size):
        
        print(f'  {x}', end="   ")
    print("")
    print("")
    for x in range(board_size):
        print(f'{x}', end=" | ")
        for y in range(board_size):
            print(f'{player_board[x][y][0]}', end=" | ")
        print("")
        print("")
        '''
#main()

set_com_ships()

