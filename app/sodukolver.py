from typing import List, Iterator
from itertools import chain


class Sodukolver:
    def __init__(self, data: List[List[int]]):
        self.data = data
        self.size = len(data)
        self.block_size = int(len(self.data) ** .5)
        self.empty_cells = [
            (i, j)
            for i in range(self.size)
            for j in range(self.size)
            if not data[i][j]
        ]

    def solve(self, next_cell_index: int = 0):
        if next_cell_index >= len(self.empty_cells):
            return True

        row, column = self.empty_cells[next_cell_index]

        for i in range(1, self.size + 1):
            if self.check(row, column, i):
                self.data[row][column] = i
                if self.solve(next_cell_index + 1):
                    return True

                self.data[row][column] = 0

        return False

    def check(self, row: int, column: int, number: int) -> bool:
        return number not in chain(
            self.iter_row(row),
            self.iter_column(column),
            self.iter_block(row, column)
        )

    def iter_row(self, row: int) -> Iterator[int]:
        return self.data[row]

    def iter_column(self, column: int) -> Iterator[int]:
        for i in range(self.size):
            yield self.data[i][column]

    def iter_block(self, row: int, column: int) -> Iterator[int]:
        row_start = row - (row % self.block_size)
        column_start = column - (column % self.block_size)

        for i in range(row_start, row_start + self.block_size):
            for j in range(column_start, column_start + self.block_size):
                yield self.data[i][j]
