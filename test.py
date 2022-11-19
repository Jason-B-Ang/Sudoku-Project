from sudoku_generator import SudokuGenerator
from board import Board
import pygame

pygame.init()
screen = pygame.display.set_mode((900, 900))

sudoku = Board(900, 900, screen, 'easy')
board = sudoku.board

print(board)

if sudoku.check_board() == False:
  print('pass')