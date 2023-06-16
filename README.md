Advanced Checkers Game Design
Created an object-oriented, Python-based variant of the classic board game, Checkers, suitable for two players, featuring a unique set of game rules as outlined in Checkers.pdf.

Checkers:

The Checkers class encapsulates the game, initializing the game board upon the creation of a Checkers object and managing information related to the board and the players.

This class includes the following methods:

* create_player(player_name, piece_color): Constructs a player object with the given player name and selected piece color ("Black" or "White"), and returns the created player object.
* play_game(player_name, starting_square_location, destination_square_location): Orchestrates the game movements as per player instructions, ensuring adherence to game rules. Also, raises various exceptions to maintain game integrity such as OutofTurn, InvalidSquare, and InvalidPlayer exceptions. This method returns the number of captured pieces or 0 if none.
* get_checker_details(square_location): Provides details about the piece present at a given location on the board. If no piece is present or if the location does not exist, returns appropriate responses or raises an InvalidSquare exception.
* print_board(): Displays the current board state as an array.
* game_winner(): Identifies and returns the winning player's name, if the game has concluded. Otherwise, it indicates the game is still ongoing.
Player:

The Player class represents the individual player, initialized with a chosen player_name and piece_color ("Black" or "White").

This class includes the following methods:

* get_king_count(): Returns the count of king pieces that the player currently possesses.
* get_triple_king_count(): Returns the count of triple king pieces that the player currently possesses.
* get_captured_pieces_count(): Returns the count of opponent pieces that the player has successfully captured.

* In addition to CheckersGame.py, which contains the main game code, I have also developed CheckersGameTester.py. This latter file comprises a robust suite of unit tests for the classes, including a minimum of five different unit tests that utilize at least two distinct assert functions.

Sample usage:

game = Checkers()

Player1 = game.create_player("Adam", "White")

Player2 = game.create_player("Lucy", "Black")

game.play_game("Lucy", (5, 6), (4, 7))

game.play_game("Adam", (2,1), (3,0))

game.get_checker_details((3,1))

Player1.get_captured_pieces_count()
