import itertools
from colorama import Fore, Back, Style, init
init()

def all_same(l):
    if l.count(l[0]) == len(l) and l[0] != 0:
        return True
    else:
        return False


def game_board(game_map,player = 0, row = 0, column = 0, just_display = False):
    try:
        if(game_map[row][column] != 0):
            print("Position occupied play at another location")
            return game_map, False
        if not just_display:
            game_map[row][column] = player
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        for count,row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 1:
                    colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
            print(count,colored_row)
        return game_map, True
    except Exception as e:
        print("Something went wrong ",e)
        return game_map, False
    

def win(current_game):
    # horizontal
    for row in current_game:
        if all_same(row):
            print(f"Player {row[0]} is the winner Horizontally (--)")
            return True
    # vertical
    for col in range(len(current_game)):
        cols = []
        for row1 in current_game:
            cols.append(row1[col])
        if all_same(cols):
            print(f"Player {cols[0]} is the winner vertically (|)")
            return True
    # diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)")
        return True

    diags = []
    for col,row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)")
        return True
    return False



play = True
players = [1,2]
while play:
    game_size = int(input("What size of TicTacToe do you want to play?"))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display = True)
    player_choice  = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player {current_player}")
        played = False
        while not played:
            column_choice = int(input("What column do you want to play? (0,1,2): "))
            row_choice = int(input("What row do you want to play? (0,1,2): "))
            game, played = game_board(game,current_player, row_choice, column_choice)
        if win(game):
            game_won = True
            again = input("The game is over, would you like to paly again? (y/n): ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Bye")
                play = False
            else:
                print("Not a valid answer. so... bye")
                play = False

#game_board(game,current_player, row_choice, column_choice, display_flag)
#2 methods to ge reversed game_map
#for col,row in enumerate(reversed(range(len(game)))):#method 1
#for col,row in zip(reversed(range(len(game)), range(len(game)))#method 2
