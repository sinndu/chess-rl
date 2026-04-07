import numpy as np
import chess
board = chess.Board()

def print_bitboard(bitboard): # print data array where each bit corrosponds to that piece being there or not
    for i in range(8):
        if i == 0:
            print(format(bitboard, "064b")[8*(i+1)-1::-1])
        else:
            print(format(bitboard, "064b")[8*(i+1)-1:8*i-1:-1])

def encode_valid_masked_moves(board): # encode valid moves into a dictionary, create mask for network (illegal moves)
    mask = np.zeros((64, 64)) # all 0s mask to start
    valid_moves_dict = {}

    for move in board.legal_moves:
        mask[move.from_square, move.to_square] = 1 # unmask legal moves
        index = 64*(move.from_square) + (move.to_square) # compute index based on starting and target square
        valid_moves_dict[index] = move
    return valid_moves_dict, mask


valid_moves_dict, mask = encode_valid_masked_moves(board)
print(valid_moves_dict)