
def import_from_pgn_file(pgn_file):
    """Import a game from a pgn file.

    Args:
        pgn_file (str): The pgn file to import from.

    Returns:
        (list of lists): A list of games separated into [metadata, pgn moves].
    """
    games = []
    with open(pgn_file, 'r') as f:
        game = f.read()
        game = game.split('\n\n')
        i = 0
        while i < len(game)-1:
            games.append([game[i], game[i+1]])
            i += 2
    return games