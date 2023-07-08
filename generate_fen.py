import re


def generate_first_position(next_move, turn):
    fen = ["rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"]
    return [position, next_move]


"""Generates the next FEN position from the previous FEN position and the next move.

    Args:
        previous_position (string): fen representation of the previous position
        next_move (string): the next move in standard algebraic notation
        turn (string): the color of the player whose turn it is (w or b)

    Returns:
        updated_position (string): fen representation of the updated position
"""
def generate_next_move(previous_position, next_move, turn):
    updated_position = ""
    return updated_position


"""Parses the pgn format to create a readable format for the generate_next_move function.

    Args:
        pgn_moves (string): string containing the pgn moves

    Returns:
        parsed_pgn (list[move, player (w or b), ]): fen representation of the updated position
"""
def pgn_format_parse(pgn_moves):
    moves = []
    split_by_move = re.split('\d+(\.) ', pgn_moves)
    for move in split_by_move:
        move = move.split(' ')
        if len(move) == 1:
            moves.append([move[0], "w"])
        else:
            moves.append([move[0], "w"])
            moves.append([move[1], "b"])
    return moves