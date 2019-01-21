from typing import List


class Piece:
    def __init__(self, spec):
        self.row_specs = spec.split(',')
        self.rows = len(self.row_specs)
        self.columns = len(self.row_specs[0])

        self.cells = []
        for row in range(self.rows):
            for column in range(self.columns):
                if self.row_specs[row][column] == '1':
                    self.cells.append([column, row])


class Board:
    def __init__(self, spec, depth=1):
        self.row_specs = spec.split(',')
        self.depth = depth
        self.rows = len(self.row_specs)
        self.columns = len(self.row_specs[0])
        self.cells = [int(o) for o in spec if o is not ',']

    def apply(self, piece, column, row, delta):
        for cell in piece.cells:
            o = column + cell[0] + (row + cell[1]) * self.columns
            self.cells[o] = (self.cells[o] + delta) % (self.depth + 1)


class Solver:
    def __init__(self, board: Board, pieces: List[Piece]):
        self.board = board
        self.pieces = pieces
        self.positions = {}

    def solve(self, index=0):
        if index is len(self.pieces):
            if any(self.board.cells):
                return None
            return self.positions
        else:
            piece = self.pieces[index]
            for column in range(1 + (self.board.columns - piece.columns)):
                for row in range(1 + (self.board.rows - piece.rows)):
                    self.positions[index] = [column, row]
                    self.board.apply(piece, column, row, 1)

                    t = self.solve(index + 1)
                    self.board.apply(piece, column, row, self.board.depth)

                    if t is not None:
                        return t
            return None
