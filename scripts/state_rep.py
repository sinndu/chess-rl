import chess
board = chess.Board()
print(board.unicode())

def print_bitboard(bitboard): # print data array where each bit corrosponds to that piece being there or not
    for i in range(8):
        if i == 0:
            print(format(bitboard, "064b")[8*(i+1)-1::-1])
        else:
            print(format(bitboard, "064b")[8*(i+1)-1:8*i-1:-1])

print("Bitboard of Pawns")
print_bitboard(board.pawns)

print("Bitboard of Kings")
print_bitboard(board.kings)