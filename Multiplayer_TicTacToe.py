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

# This function display the game matrix in user's console
def display_game_matrix(game_matrix):
    for i in range(3):
        print(f"| {game_matrix[0+3*i]} {game_matrix[1+3*i]} {game_matrix[2+3*i]} | {0+3*i} {1+3*i} {2+3*i}")

# This function check if a victorious sequence is detected in the game matrix
def check_game_matrix(game_matrix):
    o_indexes = []
    x_indexes = []
    # Storing "O" and "X" indexes in two differents lists
    for i in range(len(game_matrix)):
        if game_matrix[i] == "O":
            o_indexes.append(i)
            #print(f"o_indexes: {o_indexes}")
        elif game_matrix[i] == "X":
            x_indexes.append(i)
            #print(f"x_indexes: {x_indexes}")
    # Looping twice to check player 1 and player 2 victories
    for p in range(2):
        if p == 0:
            indexes = o_indexes
        else:
            indexes = x_indexes
        #print(f"indexes: {indexes} p: {p}")
        # Verifying that the player played at least two times
        if len(indexes) > 2:
            # Checking presence of victory sequences in indexes
            for i in range(3):
                    # Horizontally [0,1,2],[3,4,5],[6,7,8]
                if (((0+3*i) in indexes and (1+3*i) in indexes and (2+3*i) in indexes) 
                    # Vertically [0,3,6],[1,4,7],[2,5,8]
                    or ((0+i) in indexes and (3+i) in indexes and (6+i) in indexes)
                    # Diagonally [0,4,8],[6,4,2]
                    or ((0+6*i) in indexes and 4 in indexes and (8-6*i) in indexes)
                ):
                    if p == 0:          # p:0 for 1st player
                        #print(indexes)
                        return "The 1st player won the game!"
                    else:
                        #print("2nd")
                        return "The 2nd player won the game!"
    if (len(o_indexes) + len(x_indexes)) > 8:   # Check if there's squares left.
        #print(len(o_indexes)+len(x_indexes))
        return "Draw!"
    else:
        return "Play again!"

# Game variables init
game = True
game_matrix = [" "," "," "," "," "," "," "," "," "]
# player False is 1st player, player True is 2nd player.
player = False

print("Welcome in TicTacToe")
# Game loop, that runs as long as there's something left to play
while game == True:
    # Display the game_matrix in the console
    display_game_matrix(game_matrix)
    # Ask players to select a cell to play. Verify the input or ask again if cell already occupied or not an int or out of range.
    if player == False:
        selected_cell = input("1st player, please select a cell from 0 to 8: ")
        while not selected_cell.isdigit() or int(selected_cell) not in range(0,9) or game_matrix[int(selected_cell)] != " ":  
            selected_cell = input(f"{selected_cell} is not in range or already occupied. Please select another one between 0 and 8: ")
        # Update game_matrix with new item.
        game_matrix[int(selected_cell)] = "O"
    else:
        selected_cell = input("2nd player, please select a cell from 0 to 8: ")
        while not selected_cell.isdigit() or int(selected_cell) not in range(0,9) or game_matrix[int(selected_cell)] != " ":  
            selected_cell = input(f"{selected_cell} is not in range or already occupied. Please select another one between 0 and 8: ")
        game_matrix[int(selected_cell)] = "X"
    # Switch player
    player = not player
    # Call check_game_matrix(game_matrix) to verify if someone won or not.
    game_state = check_game_matrix(game_matrix)
    print(game_state)
    # End the game if check_game_matrix return anything else tha "Play again!"
    if game_state != ("Play again!"):
        game = False
display_game_matrix(game_matrix)
print("Thank you for playing TicTacToe.")