import re

"""Parses the pgn format to create a readable format for the generate_next_move function.

    Args:
        pgn_moves (string): string containing the pgn moves

    Returns:
        parsed_pgn (list[move, player (w or b), ]): fen representation of the updated position
"""
def pgn_format_parse(pgn_moves):
    moves = []
    split_by_move = re.sub('\d+(\.) ', "", pgn_moves).split()
    i = 0
    while i < len(split_by_move):
        if i+2 >= len(split_by_move):
            moves.append([split_by_move[i], "w"])
        else:
            moves.append([split_by_move[i], "w"])
            moves.append([split_by_move[i+1], "b"])
        i += 2
    return moves


"""Takes in the algebraic notation of a move and returns its current and new position.

    Args:
        alg_notation (string): string containing the pgn moves
        current_position (list[list[]]): multidimensional array representation of the current position

    Returns:
        movement (list[current_position, new_position]): give coordinates of the starting position and the new position
"""
def algebraic_notation_to_rank_file(alg_notation, current_position, turn):
    
    print(alg_notation)
    #print(current_position)
    print("flag")
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

        movement[1] = [alg_notation[0][2], alg_notation[0][3]]
    #Rook Movement
    elif alg_notation[0][0] == "R":
        print(alg_notation)
        #case for when there are two rooks that can move to the same square
        if (len(alg_notation[0]) == 4) and ("x" not in alg_notation[0]):
            if turn == "b":
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][-2])] == "r":
                            movement[0] = [i, convert_to_rank_file(alg_notation[0][-2])]
                            break
            else:
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][-2])] == "R":
                            movement[0] = [i, convert_to_rank_file(alg_notation[0][-2])]
                            break
            movement[1] = [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]
        #case when a rook captures a piece
        elif (len(alg_notation[0]) == 4) and ("x" in alg_notation[0]):
            if turn == "b":
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][-2])] == "r":
                            movement[0] = [i, convert_to_rank_file(alg_notation[0][-2])]
                            break
                        elif current_position[convert_to_rank_file(alg_notation[0][-1])][i] == "r":
                            movement[0] = [convert_to_rank_file(alg_notation[0][-1]), i]
                            break
            else:
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][-2])] == "R":
                            movement[0] = [i, convert_to_rank_file(alg_notation[0][-2])]
                            break
                        elif current_position[convert_to_rank_file(alg_notation[0][-1])][i] == "R":
                            movement[0] = [convert_to_rank_file(alg_notation[0][-1]), i]
                            break
            movement[1] = [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]
        #case when a rook moves to a square that is not occupied
        else:
            if turn == "b":
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][-2])] == "r":
                            movement[0] = [i, convert_to_rank_file(alg_notation[0][-2])]
                            break
                        elif current_position[convert_to_rank_file(alg_notation[0][-1])][i] == "r":
                            movement[0] = [i, j]
                            break
            else:
                for i in range(len(current_position)):
                        if current_position[i][convert_to_rank_file(alg_notation[0][-2])] == "R":
                            movement[0] = [i, j]
                            break
                        elif current_position[convert_to_rank_file(alg_notation[0][-1])][i] == "R":
                            movement[0] = [convert_to_rank_file(alg_notation[0][-1]), i]
                            break
            movement[1] = [convert_to_rank_file(alg_notation[0][-1]), convert_to_rank_file(alg_notation[0][-2])]
    #bishop movement
    elif alg_notation[0][0] == "B":
        #determine whether distination square is black or white
        #find bishop that can move to that square
        square_type = white_or_black_square(alg_notation[0][-2:])
        
        board_rank = 0
        if turn == "b":
            while board_rank < 8:
                if square_type == "white":
                    board_file = 1
                else:
                    board_file = 0
                while board_file < 8:
                    if current_position[board_rank][board_file] == "b":
                        movement[0] = [board_rank, board_file]
                        break
                    board_file += 2
                board_rank += 1
        else:
            while board_rank < 8:
                if square_type == "white":
                    board_file = 1
                else:
                    board_file = 0
                while board_file < 8:
                    if current_position[board_rank][board_file] == "B":
                        movement[0] = [board_rank, board_file]
                        break
                    board_file += 2
                board_rank += 1
        movement[1] = [convert_to_rank_file(alg_notation[0][-2]), convert_to_rank_file(alg_notation[0][-1])]
    #knight movement
    elif alg_notation[0][0] == "N":
        #standard knight movement where there is only one knight that can move to the square
        if (len(alg_notation[0]) == 3):
            possible_moves = possible_knight_moves(alg_notation[0][-2:])
            print(possible_moves)
            if turn == "b":
                    for move in possible_moves:
                        if current_position[move[0]][move[1]] == "n":
                            movement[0] = [move[0], move[1]]
                            break
                        elif current_position[move[0]][move[1]] == "n":
                            movement[0] = [move[0], move[1]]
                            break
            else:
                for move in possible_moves:
                    if current_position[move[0]][move[1]] == "N":
                        movement[0] = [move[0], move[1]]
                        break
                    elif current_position[move[0]][move[1]] == "N":
                        movement[0] = [move[0], move[1]]
                        break
        elif (len(alg_notation[0]) == 4):
            #case where a knight captures a piece and only that knight can capture said piece
            if (alg_notation[0][1] == "x") or (alg_notation[0][1] == "X"):
                possible_moves = possible_knight_moves(alg_notation[0][-2:])
                if turn == "b":
                    for move in possible_moves:
                        if current_position[move[0]][move[1]] == "n":
                            movement[0] = [move[0], move[1]]
                            break
                        elif current_position[move[0]][move[1]] == "n":
                            movement[0] = [move[0], move[1]]
                            break
                else:
                    for move in possible_moves:
                        if current_position[move[0]][move[1]] == "N":
                            movement[0] = [move[0], move[1]]
                            break
                        elif current_position[move[0]][move[1]] == "N":
                            movement[0] = [move[0], move[1]]
                            break
            #case where there are two knights that can move to the same square
            else:
                if alg_notation[0][1].isalpha():
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
                            if current_position[convert_to_rank_file(alg_notation[0][1])][i] == "n":
                                movement[0] = [convert_to_rank_file(alg_notation[0][1]), i]
                                break
                    else:
                        for i in range(len(current_position)):
                            if current_position[convert_to_rank_file(alg_notation[0][1])][i] == "N":
                                movement[0] = [convert_to_rank_file(alg_notation[0][1]), i]
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
                            movement[0] = [convert_to_rank_file(alg_notation[0][1]), j]
                            break
                else:
                    for i in range(len(current_position)):
                        if current_position[convert_to_rank_file(alg_notation[0][1])][i] == "N":
                            movement[0] = [convert_to_rank_file(alg_notation[0][1]), i]
                            break
        else:
            print("Error: Invalid Algebraic Notation")
        movement[1] = [convert_to_rank_file(alg_notation[0][-2]), convert_to_rank_file(alg_notation[0][-1])]
    #pawn movement
    else:
        if turn == "b":
            if len(alg_notation[0]) == 2:
                #black checking for double first move
                if alg_notation[0][1] == "5":
                    if current_position[5][convert_to_rank_file(alg_notation[0][0])] == "p":
                        movement[0] = [5, convert_to_rank_file(alg_notation[0][0])]
                    elif current_position[6][convert_to_rank_file(alg_notation[0][0])] == "p":
                        movement[0] = [6, convert_to_rank_file(alg_notation[0][0])]
                else:
                    movement[0] = [convert_to_rank_file(int(alg_notation[0][1]) + 1), convert_to_rank_file(alg_notation[0][0])]
            elif len(alg_notation[0]) == 4:
                movement[0] = [convert_to_rank_file(int(alg_notation[0][3]) + 1), convert_to_rank_file(alg_notation[0][0])]
            movement[1] = [convert_to_rank_file(int(alg_notation[0][-1])), convert_to_rank_file(alg_notation[0][-2])]
        else:
            if len(alg_notation[0]) == 2:
                if alg_notation[0][1] == "4":
                    if current_position[1][convert_to_rank_file(alg_notation[0][0])] == "P":
                        movement[0] = [1, convert_to_rank_file(alg_notation[0][0])]
                    elif current_position[2][convert_to_rank_file(alg_notation[0][0])] == "P":
                        movement[0] = [2, convert_to_rank_file(alg_notation[0][0])]
                else:
                    movement[0] = [convert_to_rank_file(int(alg_notation[0][1]) - 1), convert_to_rank_file(alg_notation[0][0])]
            elif len(alg_notation[0]) == 4:
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
    print(position)
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
    if destination_file + 2 <= 7:
        if (destination_rank + 1) <= 7:
            possible_moves.append([destination_rank + 1, destination_file + 2])
        if (destination_rank - 1) >= 0:
            possible_moves.append([destination_rank - 1, destination_file + 2])
    #knight moves backward 2 and left or right 1
    if (destination_rank - 2) >= 0:
        if (destination_file + 1) <= 7:
            possible_moves.append([destination_rank + 1, destination_file - 2])
        if (destination_file - 1) >= 0:
            possible_moves.append([destination_rank - 1, destination_file - 2])
    #knight moves left 2 and forward or backward 1
    if (destination_file - 2) >= 0:
        if (destination_rank + 1) <= 7:
            possible_moves.append([destination_rank - 2, destination_file + 1])
        if (destination_rank - 1) >= 0:
            possible_moves.append([destination_rank - 2, destination_file - 1])
    #knight moves right 2 and forward or backward 1
    if (destination_file + 2) <= 7:
        if (destination_rank + 1) <= 7:
            possible_moves.append([destination_rank + 2, destination_file + 1])
        if (destination_rank - 1) >= 0:
            possible_moves.append([destination_rank + 2,destination_file - 1])
    return possible_moves