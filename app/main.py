from typing import List
from sodukolver import Sodukolver
from sys import argv


def main():
    if len(argv) < 2:
        print('Please insert file name')

    data = get_data(argv[1])
    solver = Sodukolver(data)
    solved = solver.solve()

    if not solved:
        print('Given board is not solvable')
    else:
        print_board(solver.data)


def print_board(data: List[List[int]]) -> None:
    for row in data:
        for cell in row:
            print(cell, end=' ')
        print()


def get_data(filename: str) -> List[List[int]]:
    with open(filename, 'r') as f:
        return [
            [int(cell) for cell in str.split(line)]
            for line in f
        ]


if __name__ == "__main__":
    main()
