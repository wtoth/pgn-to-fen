import re


def generate_first_position(next_move):
    position = [["r", "n", "b", "q", "k", "b", "n", "r"],
                ["p", "p", "p", "p", "p", "p", "p", "p"],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                ["P", "P", "P", "P", "P", "P", "P", "P"],
                ["R", "N", "B", "Q", "K", "B", "N", "R"]]

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
    split_by_move = re.sub('[^0-9a-zA-Z]+', split_by_move)
    for move in split_by_move:
        move = move.split(' ')
        if len(move) == 1:
            moves.append([move[0], "w"])
        else:
            moves.append([move[0], "w"])
            moves.append([move[1], "b"])
    return moves

"""Takes in the algebraic notation of a move and returns its current and new position.

    Args:
        alg_notation (string): string containing the pgn moves
        current_position (list[list[]]): multidimensional array representation of the current position

    Returns:
        movement (list[current_position, new_position]): give coordinates of the starting position and the new position
"""
def algebraic_notation_to_rank_file(alg_notation, current_position, turn):
    movement = []
    if alg_notation == "o-o" or alg_notation == "O-O":
        return ["castle short"]
    elif alg_notation == "o-o-o" or alg_notation == "O-O-O":
        return ["castle long"]
    else:
        pass