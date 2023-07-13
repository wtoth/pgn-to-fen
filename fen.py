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
        #print(pgn.moves)
        parsed_pgn = pgn_format_parse(pgn.moves)
        #print(parsed_pgn)
        first_move = True
        self.rank_file.append(generate_first_position(parsed_pgn[1]))
        self.game.append([generate_fen_from_rank_file(self.rank_file[-1]), parsed_pgn[0]])

        for i in range(len(parsed_pgn)):
            #print(parsed_pgn[i])
            self.rank_file.append(generate_next_move(self.rank_file[-1][0], parsed_pgn[i]))
            if i + 1 < len(parsed_pgn):
                self.game.append([generate_fen_from_rank_file(self.rank_file[-1]), parsed_pgn[i+1]])
            else:
                self.game.append([generate_fen_from_rank_file(self.rank_file[-1]), None])