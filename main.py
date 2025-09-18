import os
import time


def next_generation(grid):
    n_row, n_col = len(grid), len(grid[0])
    next_g = [[0 for _ in range(n_col)] for _ in range(n_row)]

    for row in range(n_row):
        for cell in range(n_col):
            alive_neighbours = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (row + i >= 0 and row + i < n_row) and (
                        cell + j >= 0 and cell + j < n_col
                    ):
                        alive_neighbours += grid[row + i][cell + j]

            alive_neighbours -= grid[row][cell]

            if grid[row][cell] == 1 and alive_neighbours < 2:
                next_g[row][cell] = 0
            elif grid[row][cell] == 1 and alive_neighbours > 3:
                next_g[row][cell] = 0
            elif grid[row][cell] == 0 and alive_neighbours == 3:
                next_g[row][cell] = 1
            else:
                next_g[row][cell] = grid[row][cell]

    return next_g


def print_grid(grid):
    stream = "\033[H\033[J"
    for row in grid:
        for cell in row:
            if cell == 0:
                stream += " ."
            else:
                stream += " ■"
        stream += "\n"
    print(stream[:-1], end="")


def main():
    col_s, row_s = os.get_terminal_size()

    # each cell takes 2 char space
    col_s = col_s // 2

    grid = [[0 for _ in range(col_s)] for _ in range(row_s)]

    row_h = row_s // 2
    col_h = col_s // 2

    # R-pentomino
    grid[row_h - 1][col_h + 0] = 1
    grid[row_h - 1][col_h + 1] = 1
    grid[row_h + 0][col_h - 1] = 1
    grid[row_h + 0][col_h + 0] = 1
    grid[row_h + 1][col_h + 0] = 1

    prev_g = []
    pre_pg = []

    while True:
        grid = next_generation(grid)

        if grid == prev_g:
            break

        if grid == pre_pg:
            break

        print_grid(grid)

        pre_pg = prev_g
        prev_g = grid

        time.sleep(0.1)


if __name__ == "__main__":
    main()
