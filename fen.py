from generate_fen import generate_next_move, pgn_format_parse, generate_first_position

class FEN:
    def __init__(self, pgn):
        self.create_fen(pgn)

    metadata = {}
    game = []

    """Creates the FEN object from the pgn object."""
    def create_fen(self, pgn):
        self.metadata = pgn.metadata
        parsed_pgn = pgn_format_parse(pgn.moves)
        first_move = True
        for move in parsed_pgn:
            if first_move:
                self.game.append(generate_first_position(move[0]))
                first_move = False
            else:
                self.game.append(generate_next_move(self.game[-1][0], move[0], move[1]))
