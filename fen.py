from generate_fen import generate_next_move

class FEN:
    def __init__(self, pgn):
        self.create_fen(pgn)

    metadata = {}
    game = []

    """Creates the FEN object from the pgn object."""
    def create_fen(self, pgn):
        self.metadata = pgn.metadata
        self.game = pgn.moves #placeholder - need to generate fen from pgn
        
