import pygame
from .constants import BLACK, RED, WHITE, ROWS, COLS, SQUARE_SIZE
from .pieza import Pieza
class Tablero:
    def __init__(self):
        self.tablero = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings= 0
        self.create_tablero()
    
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row%2, ROWS, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    def create_tablero(self):
        for row in range(ROWS):
            self.tablero.append([])
            for col in range (COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.tablero[row].append(Pieza(row, col, WHITE))
                    elif row > 4:
                        self.tablero[row].append(Pieza(row, col, RED))
                    else:
                        self.tablero[row].append(0)
                else:
                    self.tablero[row].append(0)
    def draw(self, win):
        self.draw_squares(win)
        for row in range (ROWS):
            for col in range(COLS):
                pieza = self.tablero[row][col]
                if pieza != 0:
                    pieza.draw(win)

    def move(self, pieza, row, col):
        self.tablero[pieza.row][pieza.col], self.tablero[row][col]= self.tablero[row][col], self.tablero[pieza.row][pieza.col] #swap en 1 linea
        pieza.move(row,col)

        if row ==ROWS-1 or row == 0:
            pieza.make_king()
            if pieza.color == WHITE:
                self.white_kings+=1
            else:
                self.red_kings+=1

    def get_piece(self, row, col):
        return self.tablero[row][col]
    
    
    def get_valid_moves(self, pieza):
        moves = {}
        left  = pieza.col -1
        right = pieza.col +1 
        row = pieza.row

        if pieza.color ==RED or pieza.king:
            moves.update(self._traverse_left(row-1, max(row-3, -1), -1, pieza.color, left))
            moves.update(self._traverse_right(row-1, max(row-3, -1), -1, pieza.color, right))
            
        if pieza.color ==WHITE or pieza.king:
            moves.update(self._traverse_left(row + 1, min(row+3, ROWS), 1, pieza.color, left))
            moves.update(self._traverse_right(row + 1, min(row+3, ROWS), 1, pieza.color, right))
        
        return moves
            
    
    def _traverse_left(self, start, stop, step, color, left, skipped = []):
        moves= {}
        last= []
        for r in range(start, stop, step):
            if left<0:
                break
            current = self.tablero[r][left]#definimos la casilla a la que nos queremos mover
            if current ==0: #Si la posicion actual es 0 es porque la  casilla esta vacia
                if skipped and not last:#si nos comimos una pieza y no hay nadie mas para comer, se rompe el ciclo
                    break
                elif skipped:
                    moves[(r, left)]= last+skipped
                else:
                    moves[(r, left)]= last
                
                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+r, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                break

            elif current.color==color:#si la casilla tiene una pieza y es del mismo color que la que queremos mover, no es valido
                break
            else:
                last=[current]

            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped = []):
        moves= {}
        last= []
        for r in range(start, stop, step):
            if right>=COLS:
                break
            current = self.tablero[r][right]#definimos la casilla a la que nos queremos mover
            if current ==0: #Si la posicion actual es 0 es porque la  casilla esta vacia
                if skipped and not last:#si nos comimos una pieza y no hay nadie mas para comer, se rompe el ciclo
                    break
                elif skipped:
                    moves[(r, right)]= last+skipped
                else:
                    moves[(r, right)]= last
                
                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+r, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                break

            elif current.color==color:#si la casilla tiene una pieza y es del mismo color que la que queremos mover, no es valido
                break
            else:
                last=[current]

            right += 1
        return moves
    
    def remove(self, piezas):
            for pieza in piezas:
                self.tablero[pieza.row][pieza.col]=0
                if pieza !=0:
                    if pieza.color == RED:
                        self.red_left-= 1
                    else:  
                        self.white_left -=1
    def winner(self):
        if self.red_left <=0:
            return WHITE
        elif self.white_left <=0:
            return RED

        return None        

        
        