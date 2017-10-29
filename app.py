#!/usr/bin/env python3
"""
tic tac toe v. 0.0.1
"""
class TicTacToeGame(object):
    def __init__(self):
        self.positions = """
   {} | {} | {}
   ---------
   {} | {} | {}
   ---------
   {} | {} | {}
""".format(
    1, 2, 3, 4, 5, 6, 7, 8, 9
)
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.next_player = "X"

    @property
    def winner(self):
        rotated = []
        rotated[:] = zip(*self.board[::-1])
        for row in self.board:
            if row.count("X") == 3 or row.count("O") == 3:
                return row[0]
        for row in rotated:
            if row.count("X") == 3 or row.count("O") == 3:
                return row[0]
        if (self.board[0][0] == self.board[1][1] and
            self.board[0][0] == self.board[2][2] and
            self.board[0][0] != " "):
            return self.board[0][0]
        if (self.board[0][2] == self.board[1][1] and
            self.board[0][2] == self.board[2][0] and
            self.board[0][2] != " "):
            return self.board[0][0]
        return None

    @winner.setter
    def winner(self):
        self.__winner = None

    def __repr__(self):
        b = self.board
        display = """
   {} | {} | {}
   ---------
   {} | {} | {}
   ---------
   {} | {} | {}
""".format(
    b[0][0], b[0][1], b[0][2],
    b[1][0], b[1][1], b[1][2],
    b[2][0], b[2][1], b[2][2]
)
        return display

    def make_move(self, position):
        b = self.board
        options = {
            1: b[0][0],
            2: b[0][1],
            3: b[0][2],
            4: b[1][0],
            5: b[1][1],
            6: b[1][2],
            7: b[2][0],
            8: b[2][1],
            9: b[2][2]
        }
        if options[position] != " ":
            return False
        i = 1
        row = 0
        for row in range(3):
            col = 0
            for col in range(3):
                if i == position:
                    self.board[row][col] = self.next_player
                    return True
                i += 1
        return False

    def switch_player(self):
        if self.next_player == "X":
            self.next_player = "O"
        else:
            self.next_player = "X"

def start_play():
    play = input("Would you like to play? Type 'Y' or 'y' to play: ")
    if "y" in play.lower():
        game = TicTacToeGame()
    else:
        print("Your selection was one of not selecting to play.  Goodbye!")
        exit(0)
    next_player = None
    while next_player is None:
        next_player = input("Who should be the first player? 'X' or 'O': ")
        if 'x' in next_player.lower():
            game.next_player = "X"
        elif 'o' in next_player.lower():
            game.next_player = "O"
        else:
            next_player = None
    game_loop(game)

def game_loop(game):
    while game.winner is None:
        print("It is now [ {} ] player's turn".format(game.next_player))
        print("What position would you like to play?")
        print(game.positions)
        position = input("your selection: ")
        if not position.isdigit() or int(position) > 9 or int(position) < 1:
            print("Please input a valid position")
            continue
        else:
            if not game.make_move(int(position)):
                print("Please input a valid position")
                continue
            else:
                print("Nice move")
                game.switch_player()
                print(game)
    print("And the winner is: {}".format(game.winner))


if __name__ == "__main__":
    start_play()
