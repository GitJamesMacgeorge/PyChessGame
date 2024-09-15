import enum
import pygame
from pygame.time import Clock
from board import Board

WINDOW_LENGTH = 800
WINDOW_HEIGHT = 800
SQUARE_SIZE = WINDOW_LENGTH / 8

def get_square(board, square_x: int, square_y: int):
    grid = board.get_grid()
    
    for x, col in enumerate(grid):
        for y, row in enumerate(col):
            if not ((x * SQUARE_SIZE < square_x) and ((x + 1) * SQUARE_SIZE > square_x)):
                continue

            if not ((y * SQUARE_SIZE < square_y) and ((y + 1) * SQUARE_SIZE > square_y)):
                continue

            return (x, y)
                

def select_square(board, mouse_pos):
    # Activates when mouse is clicked
    square_coord = get_square(board, mouse_pos[0], mouse_pos[1])
    
    pass
    

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
                pygame.draw.rect(SCREEN, (161, 88, 5), square, 0)
            else:
                pygame.draw.rect(SCREEN, (230, 205, 177), square, 0)

            # Load Piece
            piece = grid[x][y]
            if piece != None:
                print("@@@8", piece, row)
                piece_rectI = piece.get_image().get_rect()
                piece_rect.center = (x * SQUARE_SIZE + SQUARE_SIZE / 2, y * SQUARE_SIZE + SQUARE_SIZE / 2)
                SCREEN.blit(piece.get_image(), piece_rect)
                #pygame.draw.rect(SCREEN, (0, 88, 5), square, 0)
                #continue

def main():
    global SCREEN, CLOCK
    pygame.init() 
    SCREEN = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT)) 
    CLOCK = pygame.time.Clock() 
    running = True

    # Init Board & Load Sprites
    board = Board()
    board.init_grid()
    print("@@@2")

    while running:
        render_board(board)
        print("works")

        # Poll for events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                action = select_square(board, pygame.mouse.get_pos())
        pygame.display.update()
        CLOCK.tick(60)

    pygame.quit()




if __name__ == "__main__":
    main()
