import pygame
from pygame.time import Clock
from board import Board

WINDOW_LENGTH = 800
WINDOW_HEIGHT = 800
SQUARE_SIZE = WINDOW_LENGTH / 8

def render_board(board):
    grid = board.get_grid()
    #print("@@@1", grid)

    # Load grid
    
    for x, col in enumerate(grid):
        for y, row in enumerate(col):
            square = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

            # If x is odd, and y is even then square is black;
            # If x is even, and y is odd then square 
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and (y % 2 == 1)):
                # Square is black   
                pygame.draw.rect(SCREEN, (200, 200, 200), square, 0)
            else:
                pygame.draw.rect(SCREEN, (0, 0, 0), square, 0)

def main():
    global SCREEN, CLOCK
    pygame.init() 
    SCREEN = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT)) 
    CLOCK = pygame.time.Clock() 
    running = True

    # Init Board & Load Sprites
    board = Board()
    print("@@@2")

    while running:
        render_board(board)
        print("works")

        # Poll for events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        CLOCK.tick(60)

    pygame.quit()




if __name__ == "__main__":
    main()
