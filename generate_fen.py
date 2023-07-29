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
    position = [["R", "N", "B", "Q", "K", "B", "N", "R"],
                ["P", "P", "P", "P", "P", "P", "P", "P"],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                ["p", "p", "p", "p", "p", "p", "p", "p"],
                ["r", "n", "b", "q", "k", "b", "n", "r"]]

    return [position, next_move]

"""Generates the next FEN position from the previous FEN position and the next move.

    Args:
        previous_position (string): fen representation of the previous position
        next_move (string): the next move in standard algebraic notation
        turn (string): the color of the player whose turn it is (w or b)

    Returns:
        updated_position (string): fen representation of the updated position
"""
def generate_next_move(previous_position, next_move):
    if next_move[0] == "O-O":
        if next_move[1] == "b":
            previous_position[7][4] = " "
            previous_position[7][5] = "r"
            previous_position[7][6] = "k"
            previous_position[7][7] = " "
        else:
            previous_position[0][4] = " "
            previous_position[0][5] = "R"
            previous_position[0][6] = "K"
            previous_position[0][7] = " "
    elif next_move[0] == "O-O-O":
        if next_move[1] == "b":
            previous_position[7][4] = " "
            previous_position[7][3] = "r"
            previous_position[7][2] = "k"
            previous_position[7][0] = " "
        else:
            previous_position[0][4] = " "
            previous_position[0][3] = "R"
            previous_position[0][2] = "K"
            previous_position[0][0] = " "
    #Promotion Case
    elif "=" in next_move[0]:
        new_piece = next_move[0][-1]
        if next_move[1] == "b":
            new_piece = new_piece.lower()
        next_move[0] = next_move[0][:-2]
        movements = algebraic_notation_to_rank_file(next_move, previous_position, next_move[1])
        piece_to_move = movements[0]
        destination = movements[1]
        previous_position[piece_to_move[0]][piece_to_move[1]] = " "
        previous_position[destination[0]][destination[1]] = new_piece
    else:   
        movements = algebraic_notation_to_rank_file(next_move, previous_position, next_move[1])
        piece_to_move = movements[0]
        destination = movements[1]
        #en passant
        if len(movements) == 3:
            en_passant_movements = en_passant(piece_to_move, destination, previous_position)
            previous_position = en_passant_movements
        #standard case
        else:    
            piece_to_move_notation = previous_position[piece_to_move[0]][piece_to_move[1]]
            previous_position[piece_to_move[0]][piece_to_move[1]] = " "
            previous_position[destination[0]][destination[1]] = piece_to_move_notation
    return [previous_position, next_move]

"""Takes in a rank file notation of a board and generates the fen representation.

    Args:
        rank_file_notation (position[list of strings], next_move): multidimensional list representation of the position

    Returns:
        fen (string): fen representation of the updated position
"""
def generate_fen_from_rank_file(rank_file_notation):
    fen = ""
    rank = 7
    while rank >= 0:
        file_notation = ""
        blank_count = 0
        for j in range(len(rank_file_notation[0][rank])):
            if rank_file_notation[0][rank][j] == " ":
                blank_count += 1
            else:
                if blank_count != 0:
                    file_notation += (str(blank_count) + rank_file_notation[0][rank][j])
                    blank_count = 0
                else:
                    file_notation += rank_file_notation[0][rank][j]
            if blank_count == 8:
                file_notation = "8"
                blank_count = 0
        if blank_count != 0:
            file_notation += str(blank_count)
        if rank == 0:
            fen += file_notation
        else:
            fen += (file_notation + "/")
        rank -= 1
    return fen

def en_passant(piece_to_move, destination, previous_position):
    #[4,4] to [5,3]
    previous_position[piece_to_move[0]][destination[1]] = " "
    piece_to_move_notation = previous_position[piece_to_move[0]][piece_to_move[1]]
    previous_position[piece_to_move[0]][piece_to_move[1]] = " "
    previous_position[destination[0]][destination[1]] = piece_to_move_notation
    return previous_position