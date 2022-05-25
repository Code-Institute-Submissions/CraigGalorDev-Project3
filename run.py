import random

# creating the global variables
# the player sets the numerical value of the board size
# this then sets the size of the playable board size to be displayed
board_size = 0
# player board displays were the player positioned thier ships and updated information miss and hits 
player_board = 0
# only the pseudo board is displayed on screen showing only updated miss and hits 
# the com board has the ships locations
com_board = 0
com_pseudo_board = 0
# in this basic version of battleships each ship equals a life 
# when all 4 lives/ships are gone its game over
player_lives = 4
com_lives = 4
# these dictionaries will hold the positions of the ships location on the board
player_ships = {'battleship': 0, 'destroyer': 0, 'submarine': 0, 'patrol boat': 0}
com_ships = {'battleship': 0, 'destroyer': 0, 'submarine': 0, 'patrol boat': 0}

def random_num():
    '''
    random number generator to  set the com ships location and for com guess
    '''
    num = round((random.random()) * 10, )
    return num

#def ship_placement():
    pass

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
    """
    list=[[[],[],[],["end"]],
        [[],[],[],["end"]],
        [[],[],[],["end"]],
        [[],[],[],["end"]]]           
    print(list)
    print("\n")
    list[1][3] = ("hit")
    print(list)
    """
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

    """
    for x in range(0,1):
        print("outer", end="")
        for y in range(board):
            player_list.append("water")
        print(player_list)
    """
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

#def set_ships():
    '''
    this is the conditional so that ships do not occupy the same space
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
    '''
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
    '''
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


#def main():
    #set_board_size()
   # set_ships()
   # display_boards()
   # guess_position()
   #3
   # check_lives()
    
#main()
#set_ships()
