from generate_fen import generate_next_move, generate_first_position, generate_fen_from_rank_file
from notation_conversion import pgn_format_parse

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
        for i in range(len(parsed_pgn)-1):
            if first_move:
                self.rank_file.append(generate_first_position(parsed_pgn[i]))
                self.game.append(generate_fen_from_rank_file(self.rank_file[-1]))
                first_move = False
            else:
                self.rank_file.append(generate_next_move(self.rank_file[-1][0], parsed_pgn[i], parsed_pgn[i+1]))
                self.game.append([generate_fen_from_rank_file(self.rank_file[-1]), parsed_pgn[i+1]])