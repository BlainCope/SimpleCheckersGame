import unittest
from CheckersGame import OutofTurn, InvalidSquare, InvalidPlayer, InvalidPiece, Player, Checkers


class TestCheckers(unittest.TestCase):

    def test_player(self):
        player = Player("Alice", "Black")
        self.assertEqual(player.get_player_name(), "Alice")
        self.assertEqual(player.get_checker_color(), "Black")
        self.assertEqual(player.get_king_count(), 0)
        self.assertEqual(player.get_triple_king_count(), 0)
        self.assertEqual(player.get_captured_pieces_count(), 0)

        player.set_player_name("Bob")
        player.set_checker_color("White")
        player.set_king_count(2)
        player.set_triple_king_count(1)
        player.set_captured_pieces_count(3)

        self.assertEqual(player.get_player_name(), "Bob")
        self.assertEqual(player.get_checker_color(), "White")
        self.assertEqual(player.get_king_count(), 2)
        self.assertEqual(player.get_triple_king_count(), 1)
        self.assertEqual(player.get_captured_pieces_count(), 3)

    def test_checkers(self):
        game = Checkers()
        game.print_board()
        player1 = game.create_player("Player1", "Black")
        player2 = game.create_player("Player2", "White")
        self.assertEqual(game.get_board()[0][1], "White")
        self.assertEqual(game.get_board()[1][0], "White")

        # Test valid move
        captured_pieces = game.play_game("Player1", (5, 0), (4, 1))
        self.assertEqual(captured_pieces, 0)
        self.assertEqual(game.get_board()[5][0], "None")
        self.assertEqual(game.get_board()[4][1], "Black")

        # Test invalid player
        with self.assertRaises(InvalidPlayer):
            game.play_game("InvalidPlayer", (4, 1), (3, 2))

        # Test invalid piece
        with self.assertRaises(InvalidPiece):
            game.play_game("Player1", (1, 0), (2, 1))

        # Test valid capture
        game.set_board([
            ["None", "White", "None", "White", "None", "White", "None", "White"],
            ["White", "None", "White", "None", "White", "None", "White", "None"],
            ["None", "White", "None", "None", "None", "White", "None", "White"],
            ["None", "None", "White", "None", "None", "None", "None", "None"],
            ["None", "Black", "None", "None", "None", "None", "None", "None"],
            ["Black", "None", "Black", "None", "Black", "None", "Black", "None"],
            ["None", "Black", "None", "Black", "None", "Black", "None", "Black"],
            ["Black", "None", "Black", "None", "Black", "None", "Black", "None"],
        ])
        captured_pieces = game.play_game("Player1", (4, 1), (2, 3))
        self.assertEqual(captured_pieces, 1)
        self.assertEqual(game.get_board()[4][1], "None")
        self.assertEqual(game.get_board()[3][2], "None")
        self.assertEqual(game.get_board()[2][3], "Black")


            # Test valid promotion
        game.set_board([
            ["None", "None", "None", "White", "None", "White", "None", "White"],
            ["Black", "None", "White", "None", "White", "None", "White", "None"],
            ["None", "White", "None", "White", "None", "White", "None", "White"],
            ["None", "None", "White", "None", "None", "None", "None", "None"],
            ["None", "Black", "None", "None", "None", "None", "None", "None"],
            ["None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "None", "None", "Black", "None", "Black", "None", "Black"],
            ["Black", "None", "Black", "None", "Black", "None", "Black", "None"],
        ])
        captured_pieces = game.play_game("Player1", (1, 0), (0, 1))
        self.assertEqual(captured_pieces, 0)
        self.assertEqual(game.get_board()[1][0], "None")
        self.assertEqual(game.get_board()[0][1], "Black_King")
        self.assertEqual(player1.get_king_count(), 1)

        # Test valid triple king promotion
        game.set_board([
            ["None", "White", "None", "White", "None", "White", "None", "White"],
            ["White", "None", "White", "None", "White", "None", "White", "None"],
            ["None", "White", "None", "White", "None", "White", "None", "White"],
            ["None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "Black_King", "None", "None", "None", "None", "None", "None"],
            ["None", "None", "None", "Black", "None", "None", "None", "None"],
            ["None", "Black_King", "None", "Black", "None", "Black", "None", "Black"],
            ["Black", "None", "None", "None", "Black", "None", "Black", "None"],
        ])
        result = game.play_game("Player1", (6, 1), (7, 1))
        self.assertEqual(result, 0)
        self.assertEqual(game.get_board()[6][1], "None")
        self.assertEqual(game.get_board()[7][1], "Black_Triple_King")
        self.assertEqual(player1.get_king_count(), 1)
        self.assertEqual(player1.get_triple_king_count(), 1)


if __name__ == "__main__":
    unittest.main()
