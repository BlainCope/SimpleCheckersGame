
# Author: Blain Cope
# GitHub username: BlainCope
# Date: 3/19/2023
# Description: This program creates a game of checkers. It uses the Checkers class to create a board and update it.
# It uses the Player class to create players and update their stats. It uses the InvalidPlayer, InvalidPiece,
# InvalidSquare, and OutofTurn exceptions to handle errors.


class OutofTurn(Exception):
    """This is a class that represents an exception that is raised when a player tries to move a piece that is not
    theirs."""
    pass


class InvalidSquare(Exception):
    """This is a class that represents an exception that is raised when a player tries to move a piece to a location that is
not valid."""
    pass


class InvalidPlayer(Exception):
    """This is a class that represents an exception that is raised when a player_name is not valid."""
    pass


class InvalidPiece(Exception):
    """This is a class that represents an exception that is raised when a player tries to move a piece that is not
    theirs."""
    pass


class Player:
    """This is a class that represents a player in the game. It uses the parent class Checkers to update the board."""
    pass

    def __init__(self, player_name, checker_color):
        """This method initializes the player name and checker color, and other variables, all of which are private."""
        self._player_name = player_name
        self._checker_color = checker_color
        self._king_count = 0
        self._triple_king_count = 0
        self._captured_pieces_count = 0

    def get_player_name(self):
        """This method returns the name of the player."""
        return self._player_name

    def set_player_name(self, player_name):
        """This method sets the name of the player."""
        self._player_name = player_name

    def get_checker_color(self):
        """This method returns the color of the player's pieces."""
        return self._checker_color

    def get_king_count(self):
        """This method returns the number of king pieces a player has."""
        return self._king_count

    def get_triple_king_count(self):
        """This method returns the number of triple king pieces a player has."""
        return self._triple_king_count

    def get_captured_pieces_count(self):
        """This method returns the number of opponent pieces that a player has captured."""
        return self._captured_pieces_count

    def set_captured_pieces_count(self, captured_pieces_count):
        """This method sets the number of opponent pieces that a player has captured."""
        self._captured_pieces_count = captured_pieces_count

    def set_checker_color(self, value):
        """This method sets the color of the player's pieces."""
        self._checker_color = value

    def set_king_count(self, value):
        """This method sets the number of king pieces a player has."""
        self._king_count = value

    def set_triple_king_count(self, count):
        """This method sets the number of triple king pieces a player has."""
        self._triple_king_count = count


class Checkers:
    """This is a class that represents the checkers gameboard. It is a super class for all classes, and draws the
    board on a vertical/horizontal axis in an 8x8 square."""

    def __init__(self):
        """This method initializes all the required data members, all of which are private."""
        self._colors = ["Black", "White"]
        self._players = {}
        self._board = [
            ["None", "White", "None", "White", "None", "White", "None", "White"],
            ["White", "None", "White", "None", "White", "None", "White", "None"],
            ["None", "White", "None", "White", "None", "White", "None", "White"],
            ["None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "None", "None", "None", "None", "None", "None", "None"],
            ["Black", "None", "Black", "None", "Black", "None", "Black", "None"],
            ["None", "Black", "None", "Black", "None", "Black", "None", "Black"],
            ["Black", "None", "Black", "None", "Black", "None", "Black", "None"],
        ]

    def create_player(self, player_name, checker_color):
        """This method creates a player object and returns it."""
        player = Player(player_name, checker_color)
        self.add_player_to_dict(player, player_name)
        return player

    def add_player_to_dict(self, player, name):
        """This method adds a player to the dictionary of players."""
        self._players[name] = player

    def get_dict(self):
        """This method returns the dictionary of players."""
        return self._players

    def get_board(self):
        """This method returns the board."""
        return self._board

    def set_board(self, value):
        """This method sets the board."""
        self._board = value

    def board_iterate(self, player_name, position):
        """This method iterates through the board and returns the position of the piece that is being moved."""
        for row_index, row in enumerate(self._board):
            for col_index, col in enumerate(self._board[row_index]):
                if (row_index, col_index) == position and not None:
                    if (row_index, col_index) != self._players[player_name].get_checkers_color():
                        pass

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """This method plays the game and updates the board."""
        if player_name not in self._players:
            raise InvalidPlayer

        player_color = self._players[player_name].get_checker_color()
        starting_row, starting_col = starting_square_location
        destination_row, destination_col = destination_square_location
        start = self._board[starting_row][starting_col]
        end = self._board[destination_row][destination_col]

        if start != player_color:
            raise InvalidPiece

        direction_map = {"Black": 1, "White": -1}
        direction = direction_map[player_color]

        captured_pieces = 0
        if start == "Black" or start == "White":
            if self.is_valid_move(starting_square_location, destination_square_location, direction):
                self.move_piece(starting_square_location, destination_square_location)
                self.promote_piece(player_name, destination_square_location)
            elif self.is_valid_capture(starting_square_location, destination_square_location, direction):
                captured_pieces = self.capture_piece(starting_square_location, destination_square_location, player_name,
                                                     direction)
                self.promote_piece(player_name, destination_square_location)
            else:
                raise InvalidSquare

            return captured_pieces
        elif start == "Black_King" or start == "White_King":
            if self.is_valid_move(starting_square_location, destination_square_location, direction):
                self.move_piece(starting_square_location, destination_square_location)
                self.promote_piece(player_name, destination_square_location)
            elif self.is_valid_capture(starting_square_location, destination_square_location, direction):
                captured_pieces = self.capture_piece(starting_square_location, destination_square_location, player_name,
                                                     direction)
                self.promote_piece(player_name, destination_square_location)
            else:
                raise InvalidSquare

            return captured_pieces

    def is_valid_move_king(self, start, end, direction):
        """This method checks if the move is valid for a king piece."""
        starting_row, starting_col = start
        destination_row, destination_col = end
        if starting_row + direction == destination_row and (
                starting_col + 1 == destination_col or starting_col - 1 == destination_col):
            return self._board[destination_row][destination_col] == "None"
        elif starting_row - direction == destination_row and (
                starting_col + 1 == destination_col or starting_col - 1 == destination_col):
            return self._board[destination_row][destination_col] == "None"
        return False

    def is_valid_move(self, start, end, direction):
        """This method checks if the move is valid for a regular piece."""
        starting_row, starting_col = start
        destination_row, destination_col = end
        if starting_row + direction == destination_row and (
                starting_col + 1 == destination_col or starting_col - 1 == destination_col):
            return self._board[destination_row][destination_col] == "None"
        elif starting_row - direction == destination_row and (
                starting_col + 1 == destination_col or starting_col - 1 == destination_col):
            return self._board[destination_row][destination_col] == "None"
        return False

    def move_piece(self, start, end):
        """This method moves a piece from one position to another."""
        starting_row, starting_col = start
        destination_row, destination_col = end
        temp = self._board[starting_row][starting_col]
        self._board[starting_row][starting_col] = "None"
        self._board[destination_row][destination_col] = temp

    def is_valid_capture(self, start, end, direction):
        """This method checks if the capture is valid for a regular piece."""
        starting_row, starting_col = start
        destination_row, destination_col = end
        opponent_color = "Black" if direction == -1 else "White"
        if starting_row + (direction * 2) == destination_row and (
                starting_col + 2 == destination_col or starting_col - 2 == destination_col):
            captured_row = starting_row + direction
            captured_col = starting_col + 1 if destination_col > starting_col else starting_col - 1
            return self._board[captured_row][captured_col] == opponent_color
        elif starting_row - (direction * 2) == destination_row and (
                starting_col + 2 == destination_col or starting_col - 2 == destination_col):
            captured_row = starting_row - direction
            captured_col = starting_col + 1 if destination_col > starting_col else starting_col - 1
            return self._board[captured_row][captured_col] == opponent_color
        return False

    def capture_piece(self, start, end, player_name, direction):
        """This method captures a piece and updates the board."""
        starting_row, starting_col = start
        destination_row, destination_col = end
        if self._players[player_name].get_checker_color() == "Black":
            captured_row = starting_row - 1
            captured_col = destination_col - 1 if destination_col > starting_col else destination_col + 1
            temp = self._board[starting_row][starting_col]
            self._board[starting_row][starting_col] = "None"
            self._board[captured_row][captured_col] = "None"
            self._board[destination_row][destination_col] = self._players[player_name].get_checker_color()
            self._players[player_name].set_captured_pieces_count(
                self._players[player_name].get_captured_pieces_count() + 1)
            return 1
        elif self._players[player_name].get_checker_color() == "White":
            captured_row = starting_row + 1
            captured_col = starting_col + 1 if destination_col > starting_col else starting_col - 1
            temp = self._board[starting_row][starting_col]
            self._board[starting_row][starting_col] = "None"
            self._board[captured_row][captured_col] = "None"
            self._board[destination_row][destination_col] = temp
            self._players[player_name].set_captured_pieces_count(
                self._players[player_name].get_captured_pieces_count() + 1)
            return 1

    def promote_piece(self, player_name, destination_square_location):
        """This method promotes a piece to a king piece if it reaches the end of the board."""
        destination_row, destination_col = destination_square_location
        piece_color = self._board[destination_row][destination_col]
        player_color = self._players[player_name].get_checker_color()

        if piece_color == player_color:
            if player_color == "White" and destination_row == 7:
                self._board[destination_row][destination_col] = "White_King"
                self._players[player_name].set_king_count(self._players[player_name].get_king_count() + 1)
            elif player_color == "Black" and destination_row == 0:
                self._board[destination_row][destination_col] = "Black_King"
                self._players[player_name].set_king_count(self._players[player_name].get_king_count() + 1)
            elif piece_color == "White_King" and destination_row == 0:
                self._board[destination_row][destination_col] = "Triple_White_King"
                self._players[player_name].set_king_count(self._players[player_name].get_triple_king_count() + 1)
            elif piece_color == "Black_King" and destination_row == 7:
                self._board[destination_row][destination_col] = "Triple_Black_King"
                self._players[player_name].set_king_count(self._players[player_name].get_triple_king_count() + 1)

    def get_checker_details(self, square_location):
        """This method returns details of the input coordinates, like what color piece is there, if it is a king,
        or if a piece exists there or not."""
        if square_location not in self._board:
            return None

        for row_index, row in enumerate(self._board):
            for col_index, col in enumerate(self._board[row_index]):
                if (row_index, col_index) == square_location:
                    print(f"There is a {col} piece in that location.")

    def print_board(self):
        """This method prints the current board, with pieces identified with either Black or White based on current
        positions."""
        for row in self._board:
            print(row)

    def game_winner(self):
        """This method returns the name of the player who has won the game. If the game is not over, it returns 'game
        has not ended'."""
        if self._players["Player1"].get_captured_pieces_count() == 12:
            return "Player2"
        elif self._players["Player2"].get_captured_pieces_count() == 12:
            return "Player1"
        else:
            return "Game has not ended"


def main():
    pass


if __name__ == "__main__":
    main()
