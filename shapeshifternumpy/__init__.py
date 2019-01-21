from typing import List

import numpy as np


class BasePuzzle:
    def __init__(self, piece: str):
        # turns the string into a 2D numpy array
        self.array = np.asarray([list(map(int, list(nums))) for nums in piece.split(',')])
        self.rows, self.columns = self.array.shape


class Board(BasePuzzle):
    def __init__(self, board: str, depth: int = 1):
        super().__init__(board)
        self.depth = depth

    @property
    def is_solved(self):
        return np.array_equal(self.array, np.zeros_like(self.array))

    def apply(self, piece: np.ndarray, x: int, y: int, delta: int):
        piece.array[piece.array > 0] = delta

        self.array[y:piece.array.shape[0] + y, x:piece.array.shape[1] + x] = np.add(self.array[y:piece.array.shape[0] + y, x:piece.array.shape[1] + x], piece.array)

        self.array = np.mod(self.array, np.full(self.array.shape, self.depth + 1))


class Piece(BasePuzzle):
    pass


class Solver:
    def __init__(self, board: Board, pieces: List[Piece]):
        self.board = board
        self.pieces = pieces
        self.positions = {}

    def solve(self, index=0):
        if index is len(self.pieces):
            if not self.board.is_solved:
                return None
            return self.positions
        else:
            shape = self.pieces[index]
            for column in range(1 + (self.board.columns - shape.columns)):
                for row in range(1 + (self.board.rows - shape.rows)):
                    self.positions[index] = [column, row]
                    self.board.apply(shape, column, row, 1)

                    t = self.solve(index + 1)
                    self.board.apply(shape, column, row, self.board.depth)

                    if t is not None:
                        return t
            return None
