import pygame
from cell import Cell
from sudoku_generator import *

class Board():
  def __init__(self, width, height, screen, difficulty):
    sudoku = SudokuGenerator(9,20)
    for i in range(9):
      row = []
      for j in range(9):
        row.append('-')
      sudoku.board.append(row)
    # sudoku.print_board()
    
    sudoku.fill_values()
    # self.key = sudoku.deepcopy()
    sudoku.remove_cells()
    self.board = sudoku.board 
    self.original_board = copy.deepcopy(self.original_board)
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty
    self.current_selected_cell_coordinates = (None,None)
    self.cell_size = width // 9

  '''
  Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.  
  Draws every cell on this board.  
  '''
  def draw(self):
    # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
    for i in range(0, 10):
      line_width = self.bold_line if i % 3 == 0 else self.line_width
      pygame.draw.line(self.screen, self.line_color, (0, self.cell_size), (width, self.cell_size), line_width)
      pygame.draw.line(self.screen, self.line_color, (i * self.cell_size, 0), (i * self.cell_size, height), line_width)
  
    # Draws every cell on this board.
    for j in range(0, 9):
      for k in range(0, 9):
        integer = int_font.render(str(self.board[i][j]), 0, self.num_color)
        integer_rect = integer.get_rect(center=(j * self.cell_size, k * self.cell_size))
        screen.blit(integer, integer_rect)        

  def select(self, row, col): 
    self.current_selected_cell_coordinates = (row, col)
 
  def click(self, x, y):
    if 0 <= x <= 900 and 0<= y <= 900:
      row, col = x // 100, y // 100
      return (row, col)
      

  def clear(self, row, col):
    if self.original_board[row][col] == 0:
      self.board[row][col] = 0
      
    
  #no need for sketch as
  #GUI will be updated using draw() for place_number(),
  #which updates the self.board. draw()
  #then draw by looping through every values on the board
  # def sketch(self, value):
  #   pass
    

  def place_number(self, value):
    self.board[self.self.current_selected_cell_coordinates[0]][self.self.current_selected_cell_coordinates[1]] = value
 
  def reset_to_original(self):
    self.board = self.original_board
 
  def is_full(self):
    for i in range(9):
      for i in range(9):
        if self.board[i][j] == '-':
          return False
    return True

  #currently not need
  # def update_board(self):
  #   pass
 
  def find_empty(self):
    for i in range(9):
      for j in range(9):
        if self.board[i][j] == 0:
          return (i, j)
 
  def check_board(self):
    
    # key_horizontal = {'1':0, '2':0, '3':0 ,'4':0 ,'5':0, '6':0, '7':0, '8':0, '9':0}
    # key_vertical = {'1':0, '2':0, '3':0 ,'4':0 ,'5':0, '6':0, '7':0, '8':0, '9':0}
    # for i in range(8):
    #   for j in range(8):
    #     if self.board[i][j] in key_horizontal.keys():
    #       key_horizontal[self.board[i][j]] += 1
    #     if self.board[j][i] in key_vertical.keys():
    #       key_vertical[self.board[j][i]] += 1
    #   for x in key_horizonal.values():
    #     if x >1:
    #       return False
    #   for x in key_vertical.values():
    #     if x >1:
    #       return False
    for i in range(9):
      for j in range(9):
        if not sudoku.is_valid(i, j, self.board[i][j]) or self.board[i][j] == '0':
          return False
    return True
 
    