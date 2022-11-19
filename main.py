from sudoku_generator import *


#initialize board
sudoku = SudokuGenerator(9,20)
for i in range(9):
  row = []
  for j in range(9):
    row.append('-')
  sudoku.board.append(row)
# sudoku.print_board()

sudoku.fill_values()
sudoku.remove_cells()

sudoku.print_board()

