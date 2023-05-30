from copy import deepcopy
from Damas.constants import WHITE,RED
import pygame

def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player == WHITE:
        maxEval = float('-inf')
        best_path = None
        for move in get_all_moves(position, WHITE, game):
            #Return a board so we take only the number
            evaluation = minimax(move, depth-1, RED, game)[0]
            maxEval = max(maxEval, evaluation)
            #If the move is the best we track it
            if maxEval == evaluation:
                best_path = move

        return maxEval, best_path
    else:
        minEval = float('inf')
        best_path = None
        for move in get_all_moves(position, RED, game):
            #Return a board so we take only the number
            evaluation = minimax(move, depth-1, WHITE, game)[0]
            minEval = min(minEval, evaluation)
            #If the move is the best we track it
            if minEval == evaluation:
                best_path = move

        return minEval, best_path

def simulate_move(pieza, move, tablero, game, skip):
    tablero.move(pieza, move[0], move[1])
    #If the piece jump over another
    if skip:
        tablero.remove(skip)

    return tablero

#All possible moves for a piece
def get_all_moves(tablero, color, game):
    moves = [] #get the board with the best move for x piece

    for pieza in tablero.get_all_pieces(color):
        valid_moves = tablero.get_valid_moves(pieza)
        #Skip = This store what pieces to remove if a piece jump over another piece
        for move, skip in valid_moves.items():
            tablero_temp = deepcopy(tablero)
            pieza_temp = tablero_temp.get_piece(pieza.row, pieza.col)
            #Return the board after making a move with a piece
            new_tablero = simulate_move(pieza_temp,move,tablero_temp,game,skip)
            moves.append(new_tablero)

    return moves
