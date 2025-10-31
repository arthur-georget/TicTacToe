# A TicTacToe game
There's a list of size 9 that can store " ", "O" or "X".  
At first, the user choose how many players will play.  
Then he/she chooses which symbol he wants to play with.  
He/she can choose between 1p and 2p.  
The empty list is displayed on three lines in the console.  
The players play one at a time.  
They have to choose an **empty** cell containing " " from 0 to 8.  
After each stroke, we check if a victory sequence is present in the game matrix  
for on of the player O or X.  
[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]  
Then the list is displayed updated.  
If one of the player is victorious, a victory message is displayed in the console.  
If no player is victorious, the game continues.  
If there's not empty cell anymore and no victory sequence is detected  
then the game is draw.  
After a draw or a victory, the user is asked if he wants to play again.  
When playing in single user mode, an ai function plays instead of the second player.  
Its intelligence grow game after game and its taunts evolves depending on its strength.  

# Variables:
    game: bool (Define if a game is on)  
    play_again: bool (Define if the whole game sequence is on or not)  
    game_count: int (Count games played)  
    p1_win_count: int (Count Player 1 victories)  
    p2_win_count: int (Count Player 2 victories)  
    single_player: bool (Define if the game is in single or multiplayer mode)  
    player_1: bool (Define which player has to play)  
    game_state: string (Define who won or if it's draw)  
    board: list[string] (Store game information, occupied and free cells)  
    o_indexes: list[string] (Store player 1 occupied cells indexes)  
    x_indexes: list[string] (Store player 2 occupied cells indexes)  
    ai_taunts: tuple(string) (Store all standard ai taunts)  
    ai_taunts_lvl_1: tuple(string) (Store all ai taunts displayed when force == 1)  
    ai_taunts_lvl_2: tuple(string) (Store all ai taunts displayed when force == 2)  
    ai_taunts_lvl_3: tuple(string) (Store all ai taunts displayed when force == 3)  

# Functions:
    display_board(board): Display the game matrix in user's console  
    check_board(board) -> String: Check if a victorious sequence is detected in the game matrix and return a string:  
     * "O"  
     * "X"  
     * "NO_WINNER_YET"  
     * "DRAW"  
    ia(board,signe,force): Return a board index depending on its sign and strength  
    check_game(game,game_state,p1_win_count,p2_win_count): Return game = False game_state anything else than "NO_WINNER_YET" and increment win counts if necessary
    ask_game_mode(): Return single_player boolean. Ask the user if he/she wants to play in single or multiplayer mode.
    ask_symbol(): Return player_1_symbol and player_2_symbol. Ask user which symbol he wants to play.
    ask_move(board,player_1,single_player,player_1_symbol,player_2_symbol): Return board,player_1. Ask users or AI which cell they wants to play depending on their symbols.
    ask_continue(): Return game,play_again,board,game_state. Ask user if he wants to play again and reset the game variables.