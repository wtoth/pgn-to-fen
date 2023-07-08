import uuid

class PGN:
    def __init__(self, pgn_file):
        self.create_pgn(pgn_file)

    game_id = uuid.uuid1()
    metadata = {
        "Event": "",
        "Site": "",
        "Date": "",
        "Round": "",
        "White": "",
        "Black": "",
        "Result": "",
        "WhiteTitle": "",
        "BlackTitle": "",
        "WhiteElo": "",
        "BlackElo": "",
        "ECO": "",
        "NIC": "",
        "Opening": "",
        "Variation": "",
        "SubVariation": "",
        "WhiteFideId": "",
        "BlackFideId": "",
        "WhiteUSCF": "",
        "BlackUSCF": "",
        "WhiteNA": "",
        "BlackNA": "",
        "WhiteType": "",
        "BlackType": "",
        "EventDate": "",
        "EventSponsor": "",
        "Section": "",
        "Stage": "",
        "Board": "",
        "Time": "",
        "UTCTime": "",
        "UTCDate": "",
        "Setup":"",
        "FEN": "",
        "Annotator": "",
        "Mode": "",
        "PlyCount": "",
        "TimeControl": "",
        "Termination": "",
    }
    moves = []

    """Loads pgn data into the pgn object.

    Args:
        pgn_data (list): [metadata, pgn moves]

    Returns:
        (n/a)
    """
    def create_pgn(self, pgn_data):
        self.moves = pgn_data[1]
        self.metadata = pgn_data[0].split('\n')
        for line in self.metadata:
            line = line.replace('[', '').replace(']', '').split(' ')
            if line[0] in self.metadata.keys():
                self.pgn_dict[line[0]] = ' '.join(line[1:])