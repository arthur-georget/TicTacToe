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
