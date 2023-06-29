
def import_from_pgn_file(pgn_file):
    """Import a game from a pgn file.

    Args:
        pgn_file (str): The pgn file to import from.

    Returns:
        (list): A list of games.
    """
    games = []
    with open(pgn_file, 'r') as f:
        game = ''
        for line in f:
            if line.startswith('['):
                continue
            elif line == '\n':
                games.append(game)
                game = ''
            else:
                game += line
    return games