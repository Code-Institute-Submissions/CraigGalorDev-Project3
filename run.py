
def check_board_size(size):
    if int(size) in range(8, 20):
        scaling = 0
        print('good choice')
        scaling = int(size)
        print(type(scaling))
    else:
        print('incorrect please try again')
    
    return scaling

def create_boards(scale):
    for size in scale:
        size = "-"
        print(size)

def ship_placement():
    pass

#def main():
    print("-----------------------")
    print("Welcome to battleships\n")
    print("please select a\n   board size\nbetween 8 and 20")

    board_size = input()
    board_scale = check_board_size(board_size)
    print(board_scale)
    print(type(board_scale))

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


#player_list = [["water", "water", "water", "water", "water"], ["water", "water", "water", "water", "water"], 
#["water", "water", "water", "water", "water"], 
#["water", "water", "water", "water", "water"],
#["water", "water", "water", "water", "water"]]
#print(player_list)
#print("\n")
#player_list[0].insert(1, "hit")
#print(player_list)
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
def set_board_size():
    list = []
    print("\nSelect a board size: A number between 5-14")
    count = int(input())
    print(count)
    if count in range(5, 15):
        print("good choice")
        for num in range(count):
            list.append([])
    else:
        print("\nsorry that is an incorrect value")
    print(list)
    
    print(list, end="\n")
    water = "water"
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

def set_player_ships():
    player_ships = []
def main():
    set_board_size()
    set_player_ships()
    set_com_ships()
    display_boards()
    guess_position()
    check_lives()
    
    
main()