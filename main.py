# from shapeshifternumpy import *  # slower, somehow
from shapeshifterpy import *

# Level 1
# board = Board('101,000,000', 1)
# pieces = ['1', '111']

# Level 2
# board = Board('110,000,111', 1)
# pieces = ['1', '1', '111']

# Level 3
# board = Board('100,000,111', 1)
# pieces = ['1', '10,11,01', '10,11,01', '111']

#####################################################################################################
# REPLACE THE CODE HERE WITH YOUR PUZZLE CODE

board = Board('100,000,111', 1)
pieces = ['1', '10,11,01', '10,11,01', '111']

#####################################################################################################

solution = Solver(board, [Piece(s) for s in pieces]).solve()

if solution is not None:
    for move in solution:
        x, y = solution[move]
        print(f'Move {move + 1}: Place piece at column {x}, row {y}')
else:
    # at some point, you've put a piece in a place that messed up every possible solution, great job.
    print('Yeah...this will not solve your puzzle.')
