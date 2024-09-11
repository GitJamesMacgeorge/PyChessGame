from re import X
import pygame

class Piece:
    def __init__(self, name: str, colour: str):
        self.name = name
        self.colour = colour
        self.x = x
        self.y = y
        self.alive = True

        # List of what pieces the piece has killed
        self.killed = []

    def get_name(self):
        return self.name

    def get_colour(self):
        return self.colour
