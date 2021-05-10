# Game setup, the board is initialized and global.  User names are defined.

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def print_board():
    print("\n_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_\n {} | {} | {} \n".format(board[0], board[1], board[2], board[3], board[4],
                                                                      board[5], board[6], board[7], board[8]))


print("Welcome to Tic-Tac-Toe")
print_board()

print(" Enter the name of first player. You are X's")
user_one = input()

print("\n Enter the name of the second player. You are O's")
user_two = input()

print_board()


# Game mechanics for two players.  The game asks for moves from both players until there are no spots left or someone  gets  three in a row.

class Usermove:
    def __init__(self, user):
        self.user = user

    move_on = 0

    def player_move(self, user):
        print("{} select your move!".format(self.user))
        move = int(input())
        move_on = 0
        if board.count(move) == 0 and move < 10:
            if board[move - 1] == "X" or board[move - 1] == "O":
                print("That is not a valid move.")
                Usermove.player_move(self, self.user)
            elif self.user == user_one:
                board[move - 1] = "X"
                print_board()
            elif self.user == user_two:
                board[move - 1] = "O"
                print_board()
            else:
                print("That is not a valid move.")
                Usermove.player_move(self, self.user)
        else:
            print("That is not a valid move.")
            Usermove.player_move(self, self.user)


game_on = True


def game_tracker():
    x_tracking = []
    y_tracking = []
    x_tracking.append([board[0], board[1], board[2]] == ['X', 'X', 'X'])
    x_tracking.append([board[3], board[4], board[5]] == ['X', 'X', 'X'])
    x_tracking.append([board[6], board[7], board[8]] == ['X', 'X', 'X'])
    x_tracking.append([board[0], board[3], board[6]] == ['X', 'X', 'X'])
    x_tracking.append([board[1], board[4], board[2]] == ['X', 'X', 'X'])
    x_tracking.append([board[2], board[5], board[8]] == ['X', 'X', 'X'])
    x_tracking.append([board[0], board[4], board[8]] == ['X', 'X', 'X'])
    x_tracking.append([board[2], board[4], board[6]] == ['X', 'X', 'X'])

    y_tracking.append([board[0], board[1], board[2]] == ['O', 'O', 'O'])
    y_tracking.append([board[3], board[4], board[5]] == ['O', 'O', 'O'])
    y_tracking.append([board[6], board[7], board[8]] == ['O', 'O', 'O'])
    y_tracking.append([board[0], board[3], board[6]] == ['O', 'O', 'O'])
    y_tracking.append([board[1], board[4], board[2]] == ['O', 'O', 'O'])
    y_tracking.append([board[2], board[5], board[8]] == ['O', 'O', 'O'])
    y_tracking.append([board[0], board[4], board[8]] == ['O', 'O', 'O'])
    y_tracking.append([board[2], board[4], board[6]] == ['O', 'O', 'O'])

    if x_tracking.count(True) == 1:
        game_on = False
        print("{} is the winner!".format(user_one))
        exit()

    elif y_tracking.count(True) == 1:
        game_on = False
        print("{} is the winner!".format(user_two))
        exit()
    else:
        return


game_tracker()

one = Usermove(user_one)
two = Usermove(user_two)

moves_counter = 0
while moves_counter != 9 and game_on == True:
    one.player_move(one)
    moves_counter += 1
    game_tracker()
    if moves_counter != 9:
        two.player_move(two)
        moves_counter += 1
        game_tracker()
    else:
        print("Game over. No declared winner!")
        exit()