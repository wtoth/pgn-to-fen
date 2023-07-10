from generate_fen import generate_next_move, pgn_format_parse, generate_first_position, generate_fen_from_rank_file

class FEN:
    def __init__(self, pgn):
        self.create_fen(pgn)
    game_id = None
    metadata = {}
    rank_file = []
    game = []

    """Creates the FEN object from the pgn object."""
    def create_fen(self, pgn):
        self.metadata = pgn.metadata
        self.game_id = pgn.game_id
        parsed_pgn = pgn_format_parse(pgn.moves)
        first_move = True
        for move in parsed_pgn:
            if first_move:
                self.rank_file.append(generate_first_position(move[0]))
                self.game.append(generate_fen_from_rank_file(self.rank_file[-1]))
                first_move = False
            else:
                self.rank_file.append(generate_next_move(self.rank_file[-1][0], move[0], move[1]))
                self.game.append(generate_fen_from_rank_file(self.rank_file[-1]))
