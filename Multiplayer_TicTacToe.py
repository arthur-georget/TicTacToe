# A two player TicTacToe game
# There's a list of size 9 that can store " ", "O" or "X"
# At first the empty list is displayed on three lines in the console. 
# The players play one at a time.
# They have to choose an **empty** cell containing " " from 0 to 8.
# After each stroke, we check if a victory sequence is present in the game matrix
# for on of the player O or X.
# [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]
# Then the list is displayed updated.
# If one of the player is victorious, a victory message is displayed in the console.
# If no player is victorious, a message ask the players to continue.
# If there's not empty cell anymore and no victory sequence is detected
# then the game is draw.
# 
# Variables:
#   game: bool (Define if a game is on)
#   player: bool (Define which player has to play)
#   game_state: string (Define who won or if it's draw)
#   game_matrix: list[string] (Store game information, occupied and free cells)
#   o_indexes: list[string] (Store player 1 occupied cells indexes)
#   x_indexes: list[string] (Store player 2 occupied cells indexes)
#
# Functions:
#   display_game_matrix(game_matrix): Display the game matrix in user's console
#   check_game_matrix(game_matrix) -> String: Check if a victorious sequence is detected in the game matrix
#                                             and return a string. "The 1st player won the game!"
#                                                                  "The 2nd player won the game!"
#                                                                  "Draw!"
#

def display_game_matrix(game_matrix):
    for i in range(3):
        print(f"| {game_matrix[0+3*i]} {game_matrix[1+3*i]} {game_matrix[2+3*i]} | {0+3*i} {1+3*i} {2+3*i}")

def check_game_matrix(game_matrix):
    o_indexes = []
    x_indexes = []
    for i in range(len(game_matrix)):
        if game_matrix[i] == "O":
            o_indexes.append(i)
            #print(f"o_indexes: {o_indexes}")
        elif game_matrix[i] == "X":
            x_indexes.append(i)
            #print(f"x_indexes: {x_indexes}")
    for p in range(2):
        if p == 0:
            indexes = o_indexes
        else:
            indexes = x_indexes
        #print(f"indexes: {indexes} p: {p}")
        if len(indexes) > 2:
            for i in range(len(indexes)):
                if (((0+3*i) in indexes and (1+3*i) in indexes and (2+3*i) in indexes) 
                    or ((0+i) in indexes and (3+i) in indexes and (6+i) in indexes)
                    or ((0+6*i) in indexes and 4 in indexes and (8-6*i) in indexes)
                ):
                    if p == 0:
                        #print(indexes)
                        return "The 1st player won the game!"
                    else:
                        #print("2nd")
                        return "The 2nd player won the game!"
    if (len(o_indexes) + len(x_indexes)) > 8:
        #print(len(o_indexes)+len(x_indexes))
        return "Draw!"
    else:
        return "Play again!"

game = True
game_matrix = [" "," "," "," "," "," "," "," "," "]
player = False

print("Welcome in TicTacToe")
while game == True:
    display_game_matrix(game_matrix)
    if player == False:
        selected_cell = input("1st player, please select a cell from 0 to 8: ")
        while not selected_cell.isdigit() or int(selected_cell) not in range(0,9) or game_matrix[int(selected_cell)] != " ":  
            selected_cell = input(f"{selected_cell} is not in range or already occupied. Please select another one between 0 and 8: ")
        game_matrix[int(selected_cell)] = "O"
    else:
        selected_cell = input("2nd player, please select a cell from 0 to 8: ")
        while not selected_cell.isdigit() or int(selected_cell) not in range(0,9) or game_matrix[int(selected_cell)] != " ":  
            selected_cell = input(f"{selected_cell} is not in range or already occupied. Please select another one between 0 and 8: ")
        game_matrix[int(selected_cell)] = "X"
    player = not player
    game_state = check_game_matrix(game_matrix)
    print(game_state)
    if game_state != ("Play again!"):
        game = False
display_game_matrix(game_matrix)
print("Thank you for playing to TicTacToe.")