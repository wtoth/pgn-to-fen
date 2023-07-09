import re

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
    movement = [None,None]
    if (alg_notation == "o-o") or (alg_notation == "O-O"):
        return ["castle short"]
    elif (alg_notation == "o-o-o") or (alg_notation == "O-O-O"):
        return ["castle long"]
    
    #process each move individually to determine the starting position
    if alg_notation[0] == "K":
        if turn == "b":
            for i in range(len(current_position)):
                for j in range(len(current_position[i])):
                    if current_position[i][j] == "k":
                        movement[0] = [i, j]
        else:
            for i in range(len(current_position)):
                for j in range(len(current_position[i])):
                    if current_position[i][j] == "K":
                        movement[0] = [i, j]

    elif alg_notation[0] == "Q":
        if turn == "b":
            for i in range(len(current_position)):
                for j in range(len(current_position[i])):
                    if current_position[i][j] == "q":
                        movement[0] = [i, j]
        else:
            for i in range(len(current_position)):
                for j in range(len(current_position[i])):
                    if current_position[i][j] == "Q":
                        movement[0] = [i, j]

        movement[1] = [alg_notation[2], alg_notation[3]]
    elif alg_notation[0] == "R":
        #case for when there are two rooks that can move to the same square
        if (len(alg_notation) == 4) and ("x" not in alg_notation):
            if turn == "b":
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0])] == "r":
                            movement[0] = [i, j]
                            break
            else:
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0])] == "R":
                            movement[0] = [i, j]
                            break
            movement[1] = [convert_to_rank_file(alg_notation[2]), convert_to_rank_file(alg_notation[3])]
        #case when a rook captures a piece
        elif (len(alg_notation) == 4) and ("x" in alg_notation):
            if turn == "b":
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0])] == "r":
                            movement[0] = [i, j]
                            break
                        elif current_position[convert_to_rank_file(alg_notation[0])][i] == "r":
                            movement[0] = [i, j]
                            break
            else:
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0])] == "R":
                            movement[0] = [i, j]
                            break
                        elif current_position[convert_to_rank_file(alg_notation[0])][i] == "R":
                            movement[0] = [i, j]
                            break
            movement[1] = [convert_to_rank_file(alg_notation[2]), convert_to_rank_file(alg_notation[3])]
        #case when a rook moves to a square that is not occupied
        else:
            if turn == "b":
                pass
            else:
                pass

    elif alg_notation[0] == "B":
        pass
    elif alg_notation[0] == "N":
        pass
    else:
        if turn == "b":
            if len(alg_notation) == 2:
                if alg_notation[1] == 5:
                    if current_position[5][convert_to_rank_file(alg_notation[0])] == "p":
                        movement[0] = [convert_to_rank_file(alg_notation[0]), 5]
                    elif current_position[6][convert_to_rank_file(alg_notation[0])] == "p":
                        movement[0] = [convert_to_rank_file(alg_notation[0]), 6]
                else:
                    movement[0] = [convert_to_rank_file(alg_notation[0]),  convert_to_rank_file(int(alg_notation[1]) + 1)]
            elif len(alg_notation) == 4:
                movement[0] = [convert_to_rank_file(alg_notation[0]),  convert_to_rank_file(int(alg_notation[3]) + 1)]
                movement[1] = [convert_to_rank_file(alg_notation[2]),  convert_to_rank_file(int(alg_notation[3]))]
        else:
            if len(alg_notation) == 2:
                if alg_notation[1] == 4:
                    if current_position[1][convert_to_rank_file(alg_notation[0])] == "p":
                        movement[0] = [convert_to_rank_file(alg_notation[0]), 1]
                    elif current_position[2][convert_to_rank_file(alg_notation[0])] == "p":
                        movement[0] = [convert_to_rank_file(alg_notation[0]), 2]
                else:
                    movement[0] = [convert_to_rank_file(alg_notation[0]),  convert_to_rank_file(int(alg_notation[1]) - 1)]
            elif len(alg_notation) == 4:
                movement[0] = [convert_to_rank_file(alg_notation[0]),  convert_to_rank_file(int(alg_notation[3]) - 1)]
                movement[1] = [convert_to_rank_file(alg_notation[2]),  convert_to_rank_file(int(alg_notation[3]))]

    return movement


#converts algebraic notation down to rank and file notation
def convert_to_rank_file(position):
    if position.isnumeric():
        return int(position) - 1
    position = position.lower()
    if position == "a":
        return 0
    elif position == "b":
        return 1
    elif position == "c":
        return 2
    elif position == "d":
        return 3
    elif position == "e":
        return 4
    elif position == "f":
        return 5
    elif position == "g":
        return 6
    elif position == "h":
        return 7