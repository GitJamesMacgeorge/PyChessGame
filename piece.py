import pygame

class Piece:
    def __init__(self, name: str, colour: str, bx: int, by: int, image_path: str):
        self.name = name
        self.colour = colour
        self.bx = bx
        self.by = by
        self.alive = True
        self.image_path = image_path
        print("@@@4", image_path)
        self.image = pygame.image.load(image_path)

        # List of what pieces the piece has killed
        self.killed = []

    def get_name(self):
        return self.name

    def get_colour(self):
        return self.colour

    def get_image(self):
        return self.image

    def get_bx(self):
        return self.bx 

    def get_by(self):
        return self.by


