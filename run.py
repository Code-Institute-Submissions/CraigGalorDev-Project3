
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



        
       


#num = 3
#for x in range(0, num):
    #print("hello")
    
"""
create_boards(board_scale)
players_board = 0
computers_board = 0
player_life = 0
com_life = 0
"""