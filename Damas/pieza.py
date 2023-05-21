import pygame, sys
from .constants import RED, WHITE, PINK, SQUARE_SIZE, GREY, BLACK

class Pieza:
    PADDING = 10
    BORDER = 2
    def __init__(self, row, col, color):
        pygame.init()
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        number= "YAS"
        self.font = pygame.font.SysFont('Arial', 25)
        self.text = self.font.render(number, True, BLACK)

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x=0
        self.y=0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE //2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE //2

    def make_king(self):
        self.king= True


    def draw(self,win):
        radius =  SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, PINK, (self.x, self.y), radius+self.BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        #win.blit(self.text, (self.x-20, self.y-15))
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()


    def __repr__(self):
        return str(self.color)
