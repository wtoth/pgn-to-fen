PGN to FEN
=====================

A chess library for generating fen data from a pgn file with the intention of using the fens to train an ml model 

## Load your data in from a Pgn File

parse a pgnFile that may have sveral pgn games. See `data/Nakamura_short.pgn` for an example

### Load and convert to fen from pgn file

```python
pgn_file = "data/Nakamura_short.pgn"
Hikaru_raw_pgns = import_pgn.import_from_pgn_file(pgn_file)
Hikaru_pgns = []
for i in range(len(Hikaru_raw_pgns)):
        pgn_game = pgn.PGN(Hikaru_raw_pgns[i])
        Hikaru_pgns.append(pgn_game)
Hikaru_fens = []
for i in range(len(Hikaru_pgns)):
    Hikaru_fens.append(fen.FEN(Hikaru_pgns[i]))
```
