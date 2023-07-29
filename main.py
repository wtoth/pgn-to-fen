import import_pgn
import fen
import pgn

def main():
    Hikaru_raw_pgns = import_pgn.import_from_pgn_file("data/Nakamura_short.pgn")
    Hikaru_pgns = []
    for i in range(len(Hikaru_raw_pgns)):
        pgn_game = pgn.PGN(Hikaru_raw_pgns[i])
        Hikaru_pgns.append(pgn_game)
    Hikaru_fens = []
    for i in range(len(Hikaru_pgns)):
        Hikaru_fens.append(fen.FEN(Hikaru_pgns[i]))


def debug():
    pass

if __name__ == "__main__":
    main()