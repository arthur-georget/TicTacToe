import random
import time

# This function display the board in user's console
def display_board(board):
    for i in range(3):
        print(f"| {board[0+3*i]} {board[1+3*i]} {board[2+3*i]} | {0+3*i} {1+3*i} {2+3*i}")

# This function check if a victorious sequence is detected in the board
def check_board(board):
    o_indexes = []
    x_indexes = []
    # Storing "O" and "X" indexes in two differents lists
    for i in range(len(board)):
        if board[i] == "O":
            o_indexes.append(i)
        elif board[i] == "X":
            x_indexes.append(i)
    # Looping twice to check player 1 and player 2 victories
    for p in range(2):
        if p == 0:
            indexes = o_indexes
        else:
            indexes = x_indexes
        # Verifying that the player played at least two times
        if len(indexes) > 2:
            # Checking presence of victory sequences in indexes
            for i in range(3):
                    
                if (((0+3*i) in indexes and (1+3*i) in indexes and (2+3*i) in indexes) # Horizontally [0,1,2],[3,4,5],[6,7,8]
                    or ((0+i) in indexes and (3+i) in indexes and (6+i) in indexes) # Vertically [0,3,6],[1,4,7],[2,5,8]
                    or ((0+6*i) in indexes and 4 in indexes and (8-6*i) in indexes) # Diagonally [0,4,8],[6,4,2]
                ):
                    if p == 0: # p:0 for 1st player
                        return "The 1st player won the game!"
                    else:
                        return "The 2nd player won the game!"
    if (len(o_indexes) + len(x_indexes)) > 8:   # Check if there's cells left.
        return "Draw!"
    else:
        return "Play again!"

def ia(board,signe,force):
    
    if len(board) > 9: # board length verification
        return False
    if not (0 <= force <= 3): # force range verification
        return False
    
    o_indexes = []
    x_indexes = []
    free_indexes = []

    for i in range(len(board)):
        if board[i] == "O":
            o_indexes.append(i)
        elif board[i] == "X":
            x_indexes.append(i)
        elif board[i] == " ":
            free_indexes.append(i)
        else:
            return False
    
    if random.randrange(3) > force:         # return random answer depending on the ai strength
        return random.choice(free_indexes)  # 0:easy -> 100% random answer | 1:medium -> 50% random answer | 2:hard -> 25% random answer | 3:very hard -> 0% random answer
    elif signe == "O":
        ia_indexes = o_indexes
        player_indexes = x_indexes
    elif signe == "X":
        ia_indexes = x_indexes
        player_indexes = o_indexes
    else:
        return False
    # The first loop check if the ai is about to win and play the winning move, 
    # the second loop check if the player is about to win and play the blocking move.
    for p in range(2):
        if p == 0:
            indexes = ia_indexes
        else:
            indexes = player_indexes
        for i in range(3):
            if ((0+3*i) in indexes and (1+3*i) in indexes and (2+3*i) in free_indexes):
                return (2+3*i)
            elif ((0+3*i) in indexes and (2+3*i) in indexes and (1+3*i) in free_indexes):
                return (1+3*i)
            elif ((1+3*i) in indexes and (2+3*i) in indexes and (0+3*i) in free_indexes):
                return (0+3*i)
            elif ((0+i) in indexes and (3+i) in indexes and (6+i) in free_indexes):
                return (6+i)
            elif ((0+i) in indexes and (6+i) in indexes and (3+i) in free_indexes):
                return (3+i)
            elif ((3+i) in indexes and (6+i) in indexes and (0+i) in free_indexes):
                return (0+i)
            elif ((0+6*i) in indexes and 4 in indexes and (8-6*i) in free_indexes):
                return (8-6*i)
            elif ((0+6*i) in indexes and (8-6*i) in indexes and 4 in free_indexes):
                return 4
            elif (4 in indexes and (8-6*i) in indexes and (0+6*i) in free_indexes):
                return (0+6*i)

    if 4 in free_indexes: # If the function returned nothing already and the center cell is free then play the center cell
        return 4
    else:
        for index in free_indexes: # If the center cell is occupied, try to play one of the corner
            if index == 0 or index%2 == 0:
                return index
    return random.choice(free_indexes) # If none of the previous conditions were met, play a random move

###############################################################################################
# Variables init
game = True
board = [" "," "," "," "," "," "," "," "," "]
single_player = True
player_1 = True # player_1 True is 1st player, player_1 False is 2nd player.
valid_user_input = False
ai_taunts = ["Hmmmm you weak pathetic fool!","You’re too slow!",
             "Nice try!","You can't beat me!","Are you sure about that?",
             "What do you say about that?","Too easy!"]

###############################################################################################

print("Welcome in TicTacToe")

print('How many player are you?')
while not valid_user_input:
    user_input = input('Please choose (1p/2p): ')
    single_input = ["1","1p","1 player","1player"]
    multi_input = ["2","2p","2 player","2player","2 players","2players"]
    if user_input.lower() in single_input:
        single_player = True
        valid_user_input = True
    elif user_input.lower() in multi_input:
        single_player = False
        valid_user_input = True
    else:
        print(f'{user_input} is different from 1p and 2p, please type 1p or 2p: ')

# Game loop, that runs as long as there's something left to play
while game == True:
    display_board(board) # Display the board in the console
    # Ask players to select a cell to play. Verify the input or ask again if cell already occupied or not an int or out of range.
    if player_1:
        selected_cell = input("1st player, please select a cell from 0 to 8: ")
        while not selected_cell.isdigit() or int(selected_cell) not in range(0,9) or board[int(selected_cell)] != " ":  
            selected_cell = input(f"{selected_cell} is not in range or already occupied. Please select another one between 0 and 8: ")
        board[int(selected_cell)] = "O" # Update board with corresponding item.
    elif single_player:
        time.sleep(2)
        print(f"AI: {random.choice(ai_taunts)}")
        time.sleep(1)
        board[ia(board,"X",3)] = "X"
    else:
        selected_cell = input("2nd player, please select a cell from 0 to 8: ")
        while not selected_cell.isdigit() or int(selected_cell) not in range(0,9) or board[int(selected_cell)] != " ":  
            selected_cell = input(f"{selected_cell} is not in range or already occupied. Please select another one between 0 and 8: ")
        board[int(selected_cell)] = "X"
    player_1 = not player_1 # Switch player
    game_state = check_board(board) # Call check_board(board) to verify if someone won or not.
    print(game_state)
    # End the game if check_board return anything else tha "Play again!"
    if game_state != ("Play again!"):
        game = False

display_board(board)
print("Thank you for playing TicTacToe.")