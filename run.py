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

#def random_num():
'''
random number generator to  set the com ships location and for com guess
'''
    #num = round((random.random()) * 10, )
   # return num

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
            
def display_boards():
    print(" Display players board enter p, for the computers board enter c")
    board_selection = input()
    pick = True
    while pick:
        if board_selection == 'p':
            print(" Players Board ")
            for x in range(board_size):
                print("        " + f"{x}", end='')
            print(" ")
            for x in range(board_size):
                print(f"{x}   ", end="")
                print(f"{player_board[x]}")
                print("")
            print("would you like to see the computers board y/n")
            option = input()
            if option == 'y':
                board_selection = 'c'
            elif option == 'n':
                print("would you like to make a guess y/n")
                guess = input()
                if guess == 'y':
                    pick = False
                else:
                    board_selection = 'p'
            else:
                print("thats not a selection")

        elif board_selection == 'c':
            print(" Computers Board ")

            for x in range(board_size):
                print("       " + f"{x}", end='  ')
            print(" ")
            for x in range(board_size):
                print(f"{x}   ", end="")
                print(f"{com_board[x]}")
                print("")
            print("would you like to see the players board y/n")
            option = input()
            if option == 'y':
                board_selection = 'p'
            elif option == 'n':
                print("would you like to make a guess y/n")
                guess = input()
                if guess == 'y':
                    pick = False
                else:
                    board_selection = 'c'
            else:
                print("thats not a selection")        
        else:
            print("that is an incorrect selection")
'''
#def main():
    print("-----------------------")
    print("Welcome to battleships\n")
    print("please select a\n   board size\nbetween 8 and 20")


#def test_1():
    list =[]
    print(list)
    print("select a position number between 0-8")
    selection = int(input())
    for x in range(0,8):
        if x != selection:
            list.append(1)
        else:
            list.append("x")
    print(list)


#def board_selection():
    col = []
    row = []

    print("select a column")
    col_selection = int(input())
    print("select a row")
    row_selection = int(input())

    print("    0   1   2   3   4   5   6   7   8")
    for x in range(0,9):

        print('\n ' + str(x), end="|")
        target = False
        if x == row_selection:
            target = True
        for y in range(0, 9):
            if y != col_selection:
                print(" = ", end="|")
            elif target == True:
                print(" @ ", end="|")
            else:
                print(" = ", end="|")
        print("\n")

#def list_iteration():
    # 4x4 list testing targeting and resetting values
    list=[[[],[],[],["end"]],
        [[],[],[],["end"]],
        [[],[],[],["end"]],
        [[],[],[],["end"]]]           
    print(list)
    print("\n")
    list[1][3] = ("hit")
    print(list)
    
    board = 5
    col = []
    print(col)
    for x in range(board):
        col.append([],)
        col[x].append([],)
        water = "-" * board
        
    print(col)
    print("\n")

    row = ["miss"] * board
    print(row)
    print("\n")
    for y in range(board):
        col[y].append(row, )
    print(col)
    print("\n")

    col[0][0] = "hit"
    print(col)
    print(col[0])


    for x in range(0,1):
        print("outer", end="")
        for y in range(board):
            player_list.append("water")
        print(player_list)
    
#print("\n put in strike co-ordinates 0-4")
#strike1 = input()
#strike2 = input()
#print(strike1, strike2)
#select = player_list[int(strike1)]
#print(select)
#select[int(strike2)] = "hit"
#print(select)
#player_list[int(strike1)] = select
#player_list[0][0] = "hit"
#print(player_list)



#num = 3
#for x in range(0, num):
    #print("hello")
#def set_board_size():
    list = []
    board_set = True
    while board_set:
        print("\nSelect a board size: A number between 5-14")
        count = int(input())
        print(count)
        if count in range(5, 15):
            print("good choice")
            for num in range(count):
                list.append([])
                board_set = False
        else:
            print("\nsorry that is an incorrect value")
            print("you need to pick a number")
        print(list)
            
   
    
    print(list, end="\n")
    water = "--"
    for x in range(len(list)):
        for y in range(len(list)):
            list[x].append(water)
    # this for loop prints out list grid
    for x in range(len(list)):
        print(list[x], end="\n")
    
    print(list[0][0])
    list[0][3] = "miss"
    print(list[0][0])
    print(list[1][0])
    for x in range(len(list)):
        print(list[x], end="\n")
'''
def set_ships():
    #this is the conditional so that ships do not occupy the same space
    print("Please select the locations of your ships")
    
    last_boat = []
    for key, value in player_ships.items():
        ship = key
        selection = True
        while selection:
            print(f"select {ship} position")
            print("please select a column")
            col_pick = True
            while col_pick:
                col = int(input())
                if col not in range(0, board_size):
                    print("nope out of range try again")
                else:
                    col_pick = False
                    
            print("please select a row")
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
                print("This position is taken sailor")
            else:
                print("Yep, looks good setting up here captain")
                last_boat.append(boat)
                check = 0
                selection = False
        player_ships[key] = [col], [row]
        print(player_ships)
        print(player_board[col][row])
        player_board[row][col] = [' @ ']
        print(player_board[col][row])
        display_boards()
    
    
    #place ships location on the board for display
    '''
    player_ships['battleship'] = [[2], [4]]
    print(player_ships)
    print(player_ships['battleship'][0])
    print("\n")
    player_ships['destroyer'] = [[3], [4]]
    print(player_ships)
    print(player_ships['destroyer'][0])
    if player_ships['battleship'] == player_ships['destroyer']:
        print("they are the same")
    else:
        print("its all good")
    
    player = {'battleship': 0, 'destroyer': 0, 'submarine': 0, 'patrol boat': 0}
    com = {'battleship': 0, 'destroyer': 0, 'submarine': 0, 'patrol boat': 0}
    print(player)
    print("\n")
    print("To set your ship positions choose a column and then a row")
    
    print(f"set battleship position")
    print("select a column")
    col = input()
    print("select a row")
    row = input()
    combo = col, row
    player['battleship'] = combo
    
    print(player['battleship'])
    print("\n")
    
    # now to make it quicker and set the ships
    last_ship_selection = 0
    for key, value in player_ships.items():
        print("\n" + f"set {key} position")
        print(last_ship_selection)
        print("\nselect a column")
        col = input()
        print("select a row")
        row = input()
        combo = col, row
        if combo == last_ship_selection:
            print("please try again")
        else:
            last_ship_selection = combo
            player_ships[key] = combo
    print(player_ships)
'''

def main():
    board_size = get_board_size()
    set_board_size()
    display_boards()
    set_ships()
    print("\n")
    for x in range(board_size):
        print(f'     {x}', end=" ")
    print("")
    for x in range(board_size):
        print(f'{x}', end=" | ")
        for y in range(board_size):
            print(f'{player_board[x][y][0]}', end=" | ")
        print("")
        print("")
main()

#set_ships()