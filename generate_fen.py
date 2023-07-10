from notation_conversion import algebraic_notation_to_rank_file


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
    movements = algebraic_notation_to_rank_file(next_move, previous_position, turn)
    piece_to_move = movements[0]
    destination = movements[1]
    piece_to_move_notation = previous_position[piece_to_move[0]][piece_to_move[1]]
    previous_position[piece_to_move[0]][piece_to_move[1]] == ""
    previous_position[destination[0]][destination[1]] == piece_to_move_notation
    return previous_position

"""Takes in a rank file notation of a board and generates the fen representation.

    Args:
        rank_file_notation (list[list[string]]): multidimensional list representation of the position

    Returns:
        fen (string): fen representation of the updated position
"""
def generate_fen_from_rank_file(rank_file_notation):
    pass