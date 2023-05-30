import pygame
from .constants import RED, WHITE, PINK, SQUARE_SIZE
from .tablero import Tablero

class Game:
    def __init__(self, win):
        self._init()
        self.win = win


    def update(self):
        self.tablero.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.tablero = Tablero()
        self.turn = RED
        self. valid_moves = {} 

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        
        pieza = self. tablero.get_piece(row, col)
        if pieza !=0 and pieza.color == self.turn:
            self.selected = pieza
            self.valid_moves = self.tablero.get_valid_moves(pieza)
            pygame.display.update()
            return True
        pygame.display.update()
        return False
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, PINK, (col * SQUARE_SIZE + SQUARE_SIZE//2, row* SQUARE_SIZE+SQUARE_SIZE//2), 15)
        
    def _move(self, row, col):
        pieza = self.tablero.get_piece(row, col)
        if self.selected and pieza == 0 and (row, col) in self.valid_moves:
            self.tablero.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.tablero.remove(skipped)
            self.change_turn()
        else:
            return False
        return True
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn==RED:
            self.turn=WHITE
        else: 
            self.turn=RED 
    def winner(self):
        return  self.tablero.winner()


