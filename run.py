def create_game_board(game_board):
    print("    0 1 2 3 4 5 6 7 8")
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

if __name__ == "__main__":
    game_board = []
    create_game_board(game_board)
