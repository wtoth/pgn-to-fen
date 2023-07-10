
"""Initializes the .

    Args:
        previous_position (string): fen representation of the previous position
        next_move (string): the next move in standard algebraic notation
        turn (string): the color of the player whose turn it is (w or b)

    Returns:
        updated_position (string): fen representation of the updated position
"""
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

"""Takes in a rank file notation of a board and generates the fen representation.

    Args:
        rank_file_notation (list[list[string]]): multidimensional list representation of the position

    Returns:
        fen (string): fen representation of the updated position
"""
def generate_fen_from_rank_file(rank_file_notation):
    pass