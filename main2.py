import pygame
from Damas.constants import HEIGHT, WIDTH, SQUARE_SIZE, RED, WHITE
from Damas.tablero import Tablero
from Damas.game import Game
from minmax.algorithm import minimax


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Damas')
FPS=60

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y //SQUARE_SIZE
    col = x //SQUARE_SIZE
    return row, col

def main():
    
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW )
    
    while run:
        if game.turn == WHITE:
            value, new_tablero = minimax(game.get_tablero(), 2, WHITE, game)
            game.ai_choice(new_tablero)
        # if game.turn == RED:
        #     value, tablero = minimax(game.get_tablero(), 2, RED, game)
        #     game.ai_choice(tablero)

        clock.tick(FPS)
       
        if game.winner() != None:
            print(game.winner())
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                run=False

            if event.type ==pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        game.update()
    pygame.quit()
main()
