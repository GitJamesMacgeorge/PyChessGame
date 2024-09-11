import pygame

class Board:
    def __init__(self):
        self.boardMap = [[[None]*8]*8]
        self.black_pawns = []
        self.black_rooks = []
        self.black_knight = []
        self.black_bishops = []
        self.black_queen = []
        self.black_king = []
        self.white_pawns = []
        self.white_rooks = []
        self.white_knight = []
        self.white_bishops = []
        self.white_queen = []
        self.white_king = []

    def get_grid(self):
        return self.boardMap[0]
    
    def init_grid(self):
        # Initialises all the pieces on the grid 
        pass





