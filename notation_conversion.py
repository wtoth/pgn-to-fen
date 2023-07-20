import re

"""Parses the pgn format to create a readable format for the generate_next_move function.

    Args:
        pgn_moves (string): string containing the pgn moves

    Returns:
        parsed_pgn (list[move, player (w or b), ]): fen representation of the updated position
"""
def pgn_format_parse(pgn_moves):
    moves = []
    pgn_moves = pgn_moves.replace('\n', ' ')
    split_by_move = re.sub('\d+(\.) ', "", pgn_moves)
    split_by_move = re.sub('\d+(\.)', "", split_by_move).replace('+', '').replace('#', '').split()
    i = 0
    while i < len(split_by_move):
        if i+2 >= len(split_by_move):
            moves.append([split_by_move[i], "w"])
        else:
            moves.append([split_by_move[i], "w"])
            moves.append([split_by_move[i+1], "b"])
        i += 2
    if (moves[-1][0] == "1-0" or moves[-1][0] == "0-1" or moves[-1][0] == "1/2-1/2"):
        moves = moves[:-1]
    return moves


"""Takes in the algebraic notation of a move and returns its current and new position.

    Args:
        alg_notation (string): string containing the pgn moves
        current_position (list[list[]]): multidimensional array representation of the current position

    Returns:
        movement (list[current_position, new_position]): give coordinates of the starting position and the new position
"""
def algebraic_notation_to_rank_file(alg_notation, current_position, turn):
    #print(alg_notation)
    #print(current_position)
    #print("flag")
    #print(turn)
    #movement of form [current_position[rank, file], new_position[rank, file]]
    movement = [None,None]
    #current_position = current_position[0]
    if (alg_notation[0] == "o-o") or (alg_notation[0] == "O-O"):
        return ["O-O", turn]
    elif (alg_notation[0] == "o-o-o") or (alg_notation[0] == "O-O-O"):
        return ["O-O-O", turn]
    
    #process each move individually to determine the starting position
    #black is lowercase white is uppercase
    #king movement
    #print(alg_notation[0])
    if alg_notation[0][0] == "K":
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
        movement[1] = [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]
    #queen movement
    elif alg_notation[0][0] == "Q":
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

        movement[1] = [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]
    #Rook Movement
    elif alg_notation[0][0] == "R":
        #print(alg_notation)
        #case for when there are two rooks that can move to the same square
        if (len(alg_notation[0]) == 4) and ("x" not in alg_notation[0]):
            #Case where the rook specifies the rank (ex: R5f4)
            if alg_notation[0][-3].isdigit():
                movement[0] = [convert_to_rank_file(alg_notation[0][-3]), convert_to_rank_file(alg_notation[0][-2])]
            #case where the rook specifies the file (ex: Rff6) 
            else:
                if turn == "b":
                    for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][-3])] == "r":
                            movement[0] = [i, convert_to_rank_file(alg_notation[0][-3])]
                            break
                else:
                    for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][-3])] == "R":
                            movement[0] = [i, convert_to_rank_file(alg_notation[0][-3])]
                            break

            movement[1] = [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]
        #case when a rook captures a piece
        elif (len(alg_notation[0]) == 4) and ("x" in alg_notation[0]):
            if turn == "b":
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][-2])] == "r":
                            if rook_path_clear(current_position, [i, convert_to_rank_file(alg_notation[0][-2])], [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]):
                                movement[0] = [i, convert_to_rank_file(alg_notation[0][-2])]
                                if not reveals_checkmate(current_position, movement[0], turn):
                                    break
                        elif current_position[convert_to_rank_file(alg_notation[0][-1])][i] == "r":
                            if rook_path_clear(current_position, [convert_to_rank_file(alg_notation[0][-1]), i], [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]):
                                movement[0] = [convert_to_rank_file(alg_notation[0][-1]), i]
                                if not reveals_checkmate(current_position, movement[0], turn):
                                    break
            else:
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][-2])] == "R":
                            if rook_path_clear(current_position, [i, convert_to_rank_file(alg_notation[0][-2])], [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]):
                                movement[0] = [i, convert_to_rank_file(alg_notation[0][-2])]
                                if not reveals_checkmate(current_position, movement[0], turn):
                                    break
                        elif current_position[convert_to_rank_file(alg_notation[0][-1])][i] == "R":
                            if rook_path_clear(current_position, [convert_to_rank_file(alg_notation[0][-1]), i], [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]):
                                movement[0] = [convert_to_rank_file(alg_notation[0][-1]), i]
                                if not reveals_checkmate(current_position, movement[0], turn):
                                    break
            movement[1] = [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]
        #
        elif len(alg_notation[0]) == 5:
            #ex: R8xd5
            if alg_notation[0][1].isdigit():
                movement[0] = [convert_to_rank_file(alg_notation[0][-4]), convert_to_rank_file(alg_notation[0][-2])]
            #ex: Rbxd6
            else:
                for i in range(len(current_position)):
                    if turn == "b":
                        if current_position[i][convert_to_rank_file(alg_notation[0][-4])] == "r":
                            movement[0] = [i, convert_to_rank_file(alg_notation[0][-4])]
                    else:
                        if current_position[i][convert_to_rank_file(alg_notation[0][-4])] == "R":
                            movement[0] = [i, convert_to_rank_file(alg_notation[0][-4])]    

            movement[1] = [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]
        #case when a rook moves to a square that is not occupied
        else:
            if turn == "b":
                for i in range(len(current_position)):
                        #print(current_position[i][convert_to_rank_file(alg_notation[0][-2])])
                        #print(current_position[convert_to_rank_file(alg_notation[0][-1])][i])
                        if current_position[i][convert_to_rank_file(alg_notation[0][-2])] == "r":
                            if rook_path_clear(current_position, [i, convert_to_rank_file(alg_notation[0][-2])], [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]):
                                movement[0] = [i, convert_to_rank_file(alg_notation[0][-2])]
                                if not reveals_checkmate(current_position, movement[0], turn):
                                    break
                        elif current_position[convert_to_rank_file(alg_notation[0][-1])][i] == "r":
                            if rook_path_clear(current_position, [convert_to_rank_file(alg_notation[0][-1]), i], [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]):
                                movement[0] = [convert_to_rank_file(alg_notation[0][-1]), i]
                                if not reveals_checkmate(current_position, movement[0], turn):
                                    break
            else:
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][-2])] == "R":
                            if rook_path_clear(current_position, [i, convert_to_rank_file(alg_notation[0][-2])], [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]):
                                movement[0] = [i, convert_to_rank_file(alg_notation[0][-2])]
                                if not reveals_checkmate(current_position, movement[0], turn):
                                    break
                        elif current_position[convert_to_rank_file(alg_notation[0][-1])][i] == "R":
                            if rook_path_clear(current_position, [convert_to_rank_file(alg_notation[0][-1]), i], [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]):
                                movement[0] = [convert_to_rank_file(alg_notation[0][-1]), i]
                                if not reveals_checkmate(current_position, movement[0], turn):
                                    break
            movement[1] = [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]
    #bishop movement
    elif alg_notation[0][0] == "B":
        #determine whether distination square is black or white
        #find bishop that can move to that square
        square_type = white_or_black_square(alg_notation[0][-2:])
        
        board_rank = 0
        white_squares = [[0, 1], [0, 3], [0, 5], [0, 7], [1, 0], [1, 2], [1, 4], [1, 6], [2, 1], [2, 3], [2, 5], [2, 7], [3, 0], [3, 2], [3, 4], [3, 6], [4, 1], [4, 3], [4, 5], [4, 7], [5, 0], [5, 2], [5, 4], [5, 6], [6, 1], [6, 3], [6, 5], [6, 7], [7, 0], [7, 2], [7, 4], [7, 6]]
        black_squares = [[0, 0], [0, 2], [0, 4], [0, 6],
                 [1, 1], [1, 3], [1, 5], [1, 7],
                 [2, 0], [2, 2], [2, 4], [2, 6],
                 [3, 1], [3, 3], [3, 5], [3, 7],
                 [4, 0], [4, 2], [4, 4], [4, 6],
                 [5, 1], [5, 3], [5, 5], [5, 7],
                 [6, 0], [6, 2], [6, 4], [6, 6],
                 [7, 1], [7, 3], [7, 5], [7, 7]]
        
        if square_type == "white":
            for square in white_squares:
                if turn == "w":
                    if current_position[square[0]][square[1]] == "B":
                        movement[0] = square
                        break
                else:
                    if current_position[square[0]][square[1]] == "b":
                        movement[0] = square
                        break
        else:
            for square in black_squares:
                if turn == "w":
                    if current_position[square[0]][square[1]] == "B":
                        movement[0] = square
                        break
                else:
                    if current_position[square[0]][square[1]] == "b":
                        movement[0] = square
                        break
        movement[1] = [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]
    #knight movement
    elif alg_notation[0][0] == "N":
        #standard knight movement where there is only one knight that can move to the square
        if (len(alg_notation[0]) == 3):
            possible_moves = possible_knight_moves(alg_notation[0][-2:])
            #print(possible_moves)
            if turn == "b":
                    for move in possible_moves:
                        if current_position[move[0]][move[1]] == "n":
                            movement[0] = [move[0], move[1]]
                            if not reveals_checkmate(current_position, movement[0], turn):
                                break
                        elif current_position[move[0]][move[1]] == "n":
                            movement[0] = [move[0], move[1]]
                            if not reveals_checkmate(current_position, movement[0], turn):
                                break
            else:
                for move in possible_moves:
                    if current_position[move[0]][move[1]] == "N":
                        movement[0] = [move[0], move[1]]
                        if not reveals_checkmate(current_position, movement[0], turn):
                                break
                    elif current_position[move[0]][move[1]] == "N":
                        movement[0] = [move[0], move[1]]
                        if not reveals_checkmate(current_position, movement[0], turn):
                                break
        elif (len(alg_notation[0]) == 4):
            #case where a knight captures a piece and only that knight can capture said piece
            if (alg_notation[0][1] == "x") or (alg_notation[0][1] == "X"):
                possible_moves = possible_knight_moves(alg_notation[0][-2:])
                if turn == "b":
                    for move in possible_moves:
                        if current_position[move[0]][move[1]] == "n":
                            movement[0] = [move[0], move[1]]
                            if not reveals_checkmate(current_position, movement[0], turn):
                                break
                        elif current_position[move[0]][move[1]] == "n":
                            movement[0] = [move[0], move[1]]
                            if not reveals_checkmate(current_position, movement[0], turn):
                                break
                else:
                    for move in possible_moves:
                        if current_position[move[0]][move[1]] == "N":
                            movement[0] = [move[0], move[1]]
                            if not reveals_checkmate(current_position, movement[0], turn):
                                break
                        elif current_position[move[0]][move[1]] == "N":
                            movement[0] = [move[0], move[1]]
                            if not reveals_checkmate(current_position, movement[0], turn):
                                break
            #case where there are two knights that can move to the same square
            else:
                if alg_notation[0][1].isdigit():
                    if turn == "b":
                        for i in range(len(current_position)):
                            if current_position[convert_to_rank_file(alg_notation[0][1])][i] == "n":
                                movement[0] = [convert_to_rank_file(alg_notation[0][1]), i]
                                break
                    else:
                        for i in range(len(current_position)):
                            if current_position[convert_to_rank_file(alg_notation[0][1])][i] == "N":
                                movement[0] = [convert_to_rank_file(alg_notation[0][1]), i]
                                break
                else:
                    if turn == "b":
                        for i in range(len(current_position)):
                            if current_position[i][convert_to_rank_file(alg_notation[0][1])] == "n":
                                movement[0] = [i, convert_to_rank_file(alg_notation[0][1])]
                                break
                    else:
                        for i in range(len(current_position)):
                            if current_position[i][convert_to_rank_file(alg_notation[0][1])] == "N":
                                movement[0] = [i, convert_to_rank_file(alg_notation[0][1])]
                                break

        elif (len(alg_notation[0]) == 5):
            #case where two knights that can capture the same piece
            if alg_notation[0][1].isalpha():
                if turn == "b":
                    for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][1])] == "n":
                            movement[0] = [i, convert_to_rank_file(alg_notation[0][1])]
                            break
                else:
                    for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][1])] == "N":
                            movement[0] = [i, convert_to_rank_file(alg_notation[0][1])]
                            break
            #super special case where there are two knights on the same file that can move to the same square
            else:
                if turn == "b":
                    for i in range(len(current_position)):
                        if current_position[convert_to_rank_file(alg_notation[0][1])][i] == "n":
                            movement[0] = [convert_to_rank_file(alg_notation[0][1]), i]
                            break
                else:
                    for i in range(len(current_position)):
                        if current_position[convert_to_rank_file(alg_notation[0][1])][i] == "N":
                            movement[0] = [convert_to_rank_file(alg_notation[0][1]), i]
                            break
        else:
            print("Error: Invalid Algebraic Notation")
        movement[1] = [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]
    #pawn movement
    else:
        if turn == "b":
            if len(alg_notation[0]) == 2:
                #black checking for double first move
                if alg_notation[0][1] == "5":
                    if (current_position[5][convert_to_rank_file(alg_notation[0][0])] == "p"):
                        movement[0] = [5, convert_to_rank_file(alg_notation[0][0])]
                    elif (current_position[6][convert_to_rank_file(alg_notation[0][0])] == "p") and (current_position[5][convert_to_rank_file(alg_notation[0][0])] == " "):
                        movement[0] = [6, convert_to_rank_file(alg_notation[0][0])]
                else:
                    movement[0] = [convert_to_rank_file(int(alg_notation[0][1]) + 1), convert_to_rank_file(alg_notation[0][0])]
            elif len(alg_notation[0]) == 4:
                if current_position[convert_to_rank_file(int(alg_notation[0][-1]))][convert_to_rank_file(alg_notation[0][-2])] == " ":
                    movement.append("en passant")
                movement[0] = [convert_to_rank_file(int(alg_notation[0][3]) + 1), convert_to_rank_file(alg_notation[0][0])]
            movement[1] = [convert_to_rank_file(int(alg_notation[0][-1])), convert_to_rank_file(alg_notation[0][-2])]
        else:
            if len(alg_notation[0]) == 2:
                #white checking for double first move
                if alg_notation[0][1] == "4":
                    if (current_position[1][convert_to_rank_file(alg_notation[0][0])] == "P") and (current_position[2][convert_to_rank_file(alg_notation[0][0])] == " "):
                        movement[0] = [1, convert_to_rank_file(alg_notation[0][0])]
                    elif current_position[2][convert_to_rank_file(alg_notation[0][0])] == "P":
                        movement[0] = [2, convert_to_rank_file(alg_notation[0][0])]
                else:
                    movement[0] = [convert_to_rank_file(int(alg_notation[0][1]) - 1), convert_to_rank_file(alg_notation[0][0])]
            elif len(alg_notation[0]) == 4:
                print(alg_notation)
                for file in reversed(current_position):
                    print(file)
                print("rank")
                print(convert_to_rank_file(int(alg_notation[0][-1])-1))
                print("file")
                print(convert_to_rank_file(alg_notation[0][-2]))
                if current_position[convert_to_rank_file(int(alg_notation[0][-1]))][convert_to_rank_file(alg_notation[0][-2])] == " ":
                    movement.append("en passant")
                movement[0] = [convert_to_rank_file(int(alg_notation[0][3]) - 1), convert_to_rank_file(alg_notation[0][0])]
            movement[1] = [convert_to_rank_file(int(alg_notation[0][-1])), convert_to_rank_file(alg_notation[0][-2])]

    return movement

#converts algebraic notation down to rank and file notation
def convert_to_rank_file(position):
    if isinstance(position, int) or (position.isnumeric()):
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
    
#determines whether a square is black or white
def white_or_black_square(position):
    #print(position)
    if position[0] == "a" or position[0] == "c" or position[0] == "e" or position[0] == "g":
        if position[1] == "1" or position[1] == "3" or position[1] == "5" or position[1] == "7":
            return "black"
        else:
            return "white"
    else:
        if position[1] == "1" or position[1] == "3" or position[1] == "5" or position[1] == "7":
            return "white"
        else:
            return "black"

#returns a list of [file, rank] for all possible knight moves
def possible_knight_moves(destination):
    possible_moves = []
    destination_file= convert_to_rank_file(destination[0])
    destination_rank = convert_to_rank_file(destination[1])
    #knight moves forward 2 and left or right 1
    if destination_rank + 2 <= 7:
        if (destination_file + 1) <= 7:
            possible_moves.append([destination_rank + 2, destination_file + 1])
        if (destination_file - 1) >= 0:
            possible_moves.append([destination_rank + 2, destination_file - 1])
    #knight moves backward 2 and left or right 1
    if (destination_rank - 2) >= 0:
        if (destination_file + 1) <= 7:
            possible_moves.append([destination_rank - 2, destination_file + 1])
        if (destination_file - 1) >= 0:
            possible_moves.append([destination_rank - 2, destination_file - 1])
    #knight moves right 2 and forward or backward 1
    if (destination_file + 2) <= 7:
        if (destination_rank + 1) <= 7:
            possible_moves.append([destination_rank + 1, destination_file + 2])
        if (destination_rank - 1) >= 0:
            possible_moves.append([destination_rank - 1,destination_file + 2])
    #knight moves left 2 and forward or backward 1
    if (destination_file - 2) >= 0:
        if (destination_rank + 1) <= 7:
            possible_moves.append([destination_rank + 1, destination_file - 2])
        if (destination_rank - 1) >= 0:
            possible_moves.append([destination_rank - 1, destination_file - 2])
    return possible_moves

def rook_path_clear(current_board, starting_position, destination):
    #print("rook path clear")
    #print(starting_position)
    #print(destination)
    #rooks on the same rank
    if starting_position[0] == destination[0]:
        if starting_position[1] < destination[1]:
            for i in range(starting_position[1]+1, destination[1]):
                if current_board[starting_position[0]][i] != " ":
                    return False
        else:
            for i in range(destination[1]+1, starting_position[1]):
                if current_board[starting_position[0]][i] != " ":
                    return False
    #rooks on the same file
    elif starting_position[1] == destination[1]:
        if starting_position[0] < destination[0]:
            for i in range(starting_position[0]+1, destination[0]):
                if current_board[i][starting_position[1]] != " ":
                    return False
        else:
            for i in range(destination[0]+1, starting_position[0]):
                if current_board[i][starting_position[1]] != " ":
                    return False
    return True

#check if a move reveals check on the king
def reveals_checkmate(current_board, moving_piece, turn):
    piece_type = current_board[moving_piece[0]][moving_piece[1]]
    #calculate where the king is located
    king_position = [None, None]
    for i in range(len(current_board)):
        for j in range(len(current_board[i])):
            if turn == "b":
                if current_board[i][j] == "k":
                    king_position = [i, j]
            else:
                if current_board[i][j] == "K":
                    king_position = [i, j]
    #if king is on the same rank as the starting position investigate
    if moving_piece[0] == king_position[0]:
        if moving_piece[1] > king_position[1]:
            for i in range(moving_piece[1]+1, 8):
                if current_board[moving_piece[0]][i] != " ":
                    if turn == "b":
                        if current_board[moving_piece[0]][i] == "R":
                            return True
                        elif current_board[moving_piece[0]][i]== "Q":
                            return True
                        else:
                            return False
                    else:
                        if current_board[moving_piece[0]][i] == "r":
                            return True
                        elif current_board[moving_piece[0]][i] == "q":
                            return True
                        else:
                            return False
        else:
            for i in range(moving_piece[1]-1, 0, -1):
                if current_board[moving_piece[0]][i] != " ":
                    if turn == "b":
                        if current_board[moving_piece[0]][i] == "R":
                            return True
                        elif current_board[moving_piece[0]][i] == "Q":
                            return True
                        else:
                            return False
                    else:
                        if current_board[moving_piece[0]][i] == "r":
                            return True
                        elif current_board[moving_piece[0]][i] == "q":
                            return True
                        else:
                            return False
    #if king is on the fame file as the starting position investigate
    elif moving_piece[1] == king_position[1]:
        if moving_piece[0] > king_position[0]:
            for i in range(moving_piece[1]+1, 8):
                if current_board[i][moving_piece[1]] != " ":
                    if turn == "b":
                        if current_board[i][moving_piece[1]] == "R":
                            return True
                        elif current_board[i][moving_piece[1]]== "Q":
                            return True
                        else:
                            return False
                    else:
                        if current_board[i][moving_piece[1]] == "r":
                            return True
                        elif current_board[i][moving_piece[1]] == "q":
                            return True
                        else:
                            return False
        else:
            for i in range(moving_piece[1]-1, 0, -1):
                if current_board[i][moving_piece[1]] != " ":
                    if turn == "b":
                        if current_board[i][moving_piece[1]] == "R":
                            return True
                        elif current_board[i][moving_piece[1]] == "Q":
                            return True
                        else:
                            return False
                    else:
                        if current_board[i][moving_piece[1]] == "r":
                            return True
                        elif current_board[i][moving_piece[1]]== "q":
                            return True
                        else:
                            return False
    #if king is on the same diagonal as the starting position investigate
    elif abs(moving_piece[0] - king_position[0]) == abs(moving_piece[1] - king_position[1]):
        if moving_piece[0] > king_position[0]:
            if moving_piece[1] > king_position[1]:
                i = moving_piece[0] + 1
                j = moving_piece[1] + 1
                while (i < 8) and (j < 8):
                    if current_board[i][j] != " ":
                        if turn == "b":
                            if current_board[i][j] == "B":
                                return True
                            elif current_board[i][j] == "Q":
                                return True
                            else:
                                return False
                        else:
                            if current_board[i][j] == "b":
                                return True
                            elif current_board[i][j] == "q":
                                return True
                            else:
                                return False
                    i += 1
                    j += 1
            else:
                i = moving_piece[0] + 1
                j = moving_piece[1] - 1
                while (i < 8) and (j >= 0):
                    if current_board[i][j] != " ":
                        if turn == "b":
                            if current_board[i][j] == "B":
                                return True
                            elif current_board[i][j] == "Q":
                                return True
                            else:
                                return False
                        else:
                            if current_board[i][j] == "b":
                                return True
                            elif current_board[i][j] == "q":
                                return True
                            else:
                                return False
                    i += 1
                    j -= 1
        else:
            if moving_piece[1] > king_position[1]:
                i = moving_piece[0] - 1
                j = moving_piece[1] + 1
                while (i >= 0) and (j < 8):
                    if current_board[i][j] != " ":
                        if turn == "b":
                            if current_board[i][j] == "B":
                                return True
                            elif current_board[i][j] == "Q":
                                return True
                            else:
                                return False
                        else:
                            if current_board[i][j] == "b":
                                return True
                            elif current_board[i][j] == "q":
                                return True
                            else:
                                return False
                    i -= 1
                    j += 1
            else:
                i = moving_piece[0] - 1
                j = moving_piece[1] - 1
                while (i >= 0) and (j >= 0):
                    if current_board[i][j] != " ":
                        if turn == "b":
                            if current_board[i][j] == "B":
                                return True
                            elif current_board[i][j] == "Q":
                                return True
                            else:
                                return False
                        else:
                            if current_board[i][j] == "b":
                                return True
                            elif current_board[i][j] == "q":
                                return True
                            else:
                                return False
                    i -= 1
                    j -= 1
    return False