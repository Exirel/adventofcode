"""Advent of Code 2015, day 3, star 1"""
import collections
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
MAPPING = {
    '>': (1, 0),
    'v': (0, -1),
    '<': (-1, 0),
    '^': (0, 1),
}


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    grid = collections.defaultdict(lambda: collections.defaultdict(list))
    pos_x = pos_y = 0

    # add one gift to the house at the starting position
    grid[pos_x][pos_y].append(1)

    # walkthrough the grid from the instructions
    for c in raw_input:
        mod_x, mod_y = MAPPING[c]
        pos_x = pos_x + mod_x
        pos_y = pos_y + mod_y
        grid[pos_x][pos_y].append(1)

    # count the number of house visited at least once
    print(sum(
        len(line.values())
        for line in grid.values()
    ))
