import pygame
from piece import Piece

WINDOW_LENGTH = 800
WINDOW_HEIGHT = 800
SQUARE_SIZE = WINDOW_LENGTH / 8

class Board:
    def __init__(self):
        self.boardMap = []
        for i in range(8):
            self.boardMap.append([None] * 8)
        self.black_pawns = []
        self.black_rooks = []
        self.black_knights = []
        self.black_bishops = []
        self.black_queen = []
        self.black_king = []
        self.white_pawns = []
        self.white_rooks = []
        self.white_knights = []
        self.white_bishops = []
        self.white_queen = []
        self.white_king = []
        self.initial_selected = None

    def get_grid(self):
        return self.boardMap

    def load_pieces_pos(self):
        print("@@@5", self.black_king[0].get_bx())
        print("@@@7", self.boardMap)
        self.boardMap[self.black_king[0].get_bx()][self.black_king[0].get_by()] = self.black_king[0]
        self.boardMap[self.white_king[0].get_bx()][self.white_king[0].get_by()] = self.white_king[0]
        self.boardMap[self.black_queen[0].get_bx()][self.black_queen[0].get_by()] = self.black_queen[0]
        self.boardMap[self.white_queen[0].get_bx()][self.white_queen[0].get_by()] = self.white_queen[0]
        
        for i in range(8):
            if i < 2:
                self.boardMap[self.black_rooks[i].get_bx()][self.black_rooks[i].get_by()] = self.black_rooks[i]
                self.boardMap[self.white_rooks[i].get_bx()][self.white_rooks[i].get_by()] = self.white_rooks[i]
                self.boardMap[self.black_knights[i].get_bx()][self.black_knights[i].get_by()] = self.black_knights[i]
                self.boardMap[self.white_knights[i].get_bx()][self.white_knights[i].get_by()] = self.white_knights[i]
                self.boardMap[self.black_bishops[i].get_bx()][self.black_bishops[i].get_by()] = self.black_bishops[i]
                self.boardMap[self.white_bishops[i].get_bx()][self.white_bishops[i].get_by()] = self.white_bishops[i]

            self.boardMap[self.black_pawns[i].get_bx()][self.black_pawns[i].get_by()] = self.black_pawns[i]
            self.boardMap[self.white_pawns[i].get_bx()][self.white_pawns[i].get_by()] = self.white_pawns[i]


            print("@@@6", self.boardMap)

    
    def init_grid(self):
        # Initialises all grid pieces
        self.black_queen.append(Piece("queen", "black", 4, 0, "resources/pieces/black_queen.png"))
        self.black_king.append(Piece("king", "black", 3, 0, "resources/pieces/black_king.png"))
        self.white_king.append(Piece("king", "white", 3, 7, "resources/pieces/white_king.png"))
        self.white_queen.append(Piece("queen", "white", 4, 7, "resources/pieces/white_queen.png"))
        self.black_rooks.append(Piece("rook", "black", 0, 0, "resources/pieces/black_rook.png"))
        self.black_rooks.append(Piece("rook", "black", 7, 0, "resources/pieces/black_rook.png"))
        self.white_rooks.append(Piece("rook", "white", 7, 7, "resources/pieces/white_rook.png"))
        self.white_rooks.append(Piece("rook", "white", 0, 7, "resources/pieces/white_rook.png"))
        self.black_knights.append(Piece("knight", "black", 1, 0, "resources/pieces/black_knight.png"))
        self.black_knights.append(Piece("knight", "black", 6, 0, "resources/pieces/black_knight.png"))
        self.white_knights.append(Piece("knight", "white", 6, 7, "resources/pieces/white_knight.png"))
        self.white_knights.append(Piece("knight", "white", 1, 7, "resources/pieces/white_knight.png"))
        self.black_bishops.append(Piece("bishop", "black", 2, 0, "resources/pieces/black_bishop.png"))
        self.black_bishops.append(Piece("bishop", "black", 5, 0, "resources/pieces/black_bishop.png"))
        self.white_bishops.append(Piece("bishop", "white", 2, 7, "resources/pieces/white_bishop.png"))
        self.white_bishops.append(Piece("bishop", "white", 5, 7, "resources/pieces/white_bishop.png"))

        for i in range(8):
            self.black_pawns.append(Piece("pawn", "black", i, 1, "resources/pieces/black_pawn.png"))
            self.white_pawns.append(Piece("pawn", "white", i, 6, "resources/pieces/white_pawn.png"))

        self.load_pieces_pos()

    def get_initial_selected(self):
        return self.initial_selected

    def set_initial_selected(self, x, y):
        self.initial_selected = (x, y)
