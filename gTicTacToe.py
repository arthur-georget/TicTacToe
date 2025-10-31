# A GUI for TicTacToe
import pygame
import random
import time

##############################################################################
# Variables init

grid_coordinates = (((0,0),(160,160)),((160,0),(320,160)),((320,0),(480,160)),
                    ((0,160),(160,320)),((160,160),(320,320)),((320,160),(480,320)),
                    ((0,320),(160,480)),((160,320),(320,480)),((320,320),(480,480)))

centers = ((80,80),(240,80),(400,80),
           (80,240),(240,240),(400,240),
           (80,400),(240,400),(400,400))

game = True
play_again = True
game_count = 0
p1_win_count = 0
p2_win_count = 0 
board = [" "," "," "," "," "," "," "," "," "]
single_player = True
player_1 = True # player_1 True is 1st player, player_1 False is 2nd player.
valid_user_input = False
valid_user_symbol = False
ai_taunts = ("Hmmmm you weak pathetic fool!","You're too slow!",
            "Nice try!","You can't beat me!","Are you sure about that?",
            "What do you say about that?","Too easy!")
ai_taunts_lvl_1 = ("I learnt from my mistakes!","From now I'll focus a little bit more.","I'm not a noob anymore.","I'm starting to understand!")
ai_taunts_lvl_2 = ("Fear the TicTacToe expert!","I'm still getting better and better!","I could give you several tips if you want.","hehe!")
ai_taunts_lvl_3 = ("I won't lose anymore.","You should give up!","TicTacToe has no secrets for me.","I'm a TicTacToe master!")

##############################################################################
# Functions

def display_board(board):
    ''' This function displays the board in user's console '''
    for i in range(3):
        print(f"| {board[0+3*i]} {board[1+3*i]} {board[2+3*i]} | {0+3*i} {1+3*i} {2+3*i}")

def draw_cross(center):
    pygame.draw.line(screen,"white",(center[0]-60,center[1]-60),(center[0]+60,center[1]+60),width=5)
    pygame.draw.line(screen,"white",(center[0]+60,center[1]-60),(center[0]-60,center[1]+60),width=5)

def check_board(board):
    ''' This function check if a victorious sequence is detected in the board '''
    o_indexes = []
    x_indexes = []
    # Storing "O" and "X" indexes in two differents lists
    for i in range(len(board)):
        if board[i] == "O":
            o_indexes.append(i)
        elif board[i] == "X":
            x_indexes.append(i)
    # Looping twice to check O then X player victories
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
                        return "O"
                    else:
                        return "X"
    if (len(o_indexes) + len(x_indexes)) > 8:   # Check if there's cells left.
        return "DRAW"
    else:
        return "NO_WINNER_YET"

def check_game(game,running,game_state,p1_win_count,p2_win_count):
    '''End the game if check_board return anything else than "NO_WINNER_YET" and increment''' 
    if game_state != ("NO_WINNER_YET"):
        game = False
        running = False
        match game_state:
            case "DRAW":
                print("It's a draw! Well done you two.")
            case "O":
                print("The O player won the game!")
                if player_1_symbol == "O":
                    print("Well done player 1.")
                    p1_win_count +=1
                    if single_player:
                        print("AI: Nooooooooooo!")
                else:
                    print("Well done player 2.")
                    p2_win_count +=1
                    if single_player:
                        print("AI: Hehe I knew I could win!")
            case "X":
                print("The X player won the game!")
                if player_1_symbol == "X":
                    print("Well done player 1.")
                    p1_win_count +=1
                    if single_player:
                        print("AI: Nooooooooooo!")
                else:
                    print("Well done player 2.")
                    p2_win_count +=1
                    if single_player:
                        print("AI: Hehe I knew I could win!")
    return game,running,p1_win_count,p2_win_count

def ia(board,signe,force):
    ''' This function return a board index depending on the board state, the symbol and force provided '''   
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

def ask_game_mode():
    ''' This function ask the user if he/she wants to play in single or multiplayer mode, 
        return single_player boolean '''
    valid_user_input = False
    
    print("How many players are you?")
    while not valid_user_input:
        user_input = input("Please choose (1p/2p): ")
        single_input = ["1","1p","1 player","1player"]
        multi_input = ["2","2p","2 player","2player","2 players","2players"]
        if user_input.lower() in single_input:
            single_player = True
            valid_user_input = True
        elif user_input.lower() in multi_input:
            single_player = False
            valid_user_input = True
        else:
            print(f"{user_input} is different from 1p and 2p, you should type 1p or 2p. ")
    return single_player

def ask_symbol():
    '''This function ask the user which symbol he wants to play.
       Return player_1_symbol and player_2_symbol'''
    valid_user_symbol = False
    while not valid_user_symbol:
        user_input = input("Player 1, with which symbol do you want to play? (O/X): ")
        if user_input.lower() == "o":
            player_1_symbol = "O"
            player_2_symbol = "X"
            valid_user_symbol = True
        elif user_input.lower() == "x":
            player_1_symbol = "X"
            player_2_symbol = "O"
            valid_user_symbol = True
        else:
            print(f"{user_input} is not a valid symbol, you should type O or X.")
    return player_1_symbol,player_2_symbol

def set_move(board,player_1,single_player,player_1_symbol,player_2_symbol,index):
    '''Ask players to select a cell to play. 
       Verify the input or ask again if cell already occupied 
       or not an int or out of range.'''
    if player_1:
        board[index] = player_1_symbol # Update board with corresponding item.
    elif single_player:
        print("AI, please select a cell from 0 to 8: ")
        time.sleep(2)
        print(f"AI: {random.choice(ai_taunts)}")
        time.sleep(1)
        force = game_count // 2
        match force:
            case 1:
                print(f"AI: {random.choice(ai_taunts_lvl_1)}")
                time.sleep(1)
            case 2:
                print(f"AI: {random.choice(ai_taunts_lvl_2)}")
                time.sleep(1)
            case 3:
                print(f"AI: {random.choice(ai_taunts_lvl_3)}")
                time.sleep(1)
        board[ia(board,player_2_symbol,force)] = player_2_symbol
    else:
        board[index] = player_2_symbol
    
    player_1 = not player_1 # Switch player
    
    return board,player_1

def ask_continue():
    '''Function to ask user if he wants to continue and reset all games variables.'''
    valid_user_input = False
    while not valid_user_input:
        user_input = input("Do you want to play again? (yes/no): ")
        yes_input = ["y","yes","oui","o","yup","hell yeah","hell yeah!"]
        no_input = ["n","no","non","nope","no way","hell no","hell no!"]
        if user_input.lower() in yes_input:
            game = True
            play_again = True
            running = True
            valid_user_input = True
        elif user_input.lower() in no_input:
            game = False
            play_again = False
            running = False
            valid_user_input = True
        else:
            print(f"{user_input} is different from yes or no, you should type yes or no.")
    board = [" "," "," "," "," "," "," "," "," "] # Board reset
    game_state = "NO_WINNER_YET" # Game state reset
    return game,play_again,running,board,game_state

### Game init ###
single_player = ask_game_mode()
player_1_symbol,player_2_symbol = ask_symbol()

while play_again:
    while game:
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode((480, 480))
        clock = pygame.time.Clock()
        running = True
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #print(pygame.mouse.get_pos())
                    for i,coordinate in enumerate(grid_coordinates):
                        if ((coordinate[0][0] < pygame.mouse.get_pos()[0] < coordinate[1][0])
                        and (coordinate[0][1] < pygame.mouse.get_pos()[1] < coordinate[1][1])):
                            board,player_1 = set_move(board,player_1,single_player,player_1_symbol,player_2_symbol,i)
                            game_state = check_board(board) # Check the board to know if someone won or not.
                            game,running,p1_win_count,p2_win_count = check_game(game,running,game_state,p1_win_count,p2_win_count) # Check game_state to end the game if necessary and congrats the winners.
            # fill the screen with a color to wipe away anything from last frame
            screen.fill(pygame.Color(29, 135, 79, 255))
            for i in range(1,3):
                pygame.draw.line(screen,"white",(i*160-2,0),(i*160-2,480),width=4)
                pygame.draw.line(screen,"white",(0,i*160-2),(480,i*160-2),width=4)

            # RENDER YOUR GAME HERE  
            for i, symbol in enumerate(board):
                if symbol == "X":
                    draw_cross(centers[i])
                elif symbol == "O":
                    pygame.draw.circle(screen,"white",centers[i],60,width=5)

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60
    
    game_count += 1
    game,play_again,running,board,game_state = ask_continue() # Ask user if he wants to continue, and resets games variables

print(f"Thank you for playing TicTacToe, here's the final score p1: {p1_win_count} p2: {p2_win_count}")