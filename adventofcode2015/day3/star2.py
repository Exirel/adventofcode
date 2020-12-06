"""Advent of Code 2015, day 3, star 2"""
import collections

from star1 import INPUT_FILE, MAPPING


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    grid = collections.defaultdict(lambda: collections.defaultdict(list))
    pos_x = pos_y = 0
    rob_pos_x = rob_pos_y = 0

    # add one gift to the house at the starting position
    grid[pos_x][pos_y].append(1)
    # and a second one, because the robot is here too
    grid[rob_pos_x][rob_pos_y].append(1)

    # walkthrough the grid from the instructions
    # Santa and Robot Santa shares the same grid
    for i, c in enumerate(raw_input):
        mod_x, mod_y = MAPPING[c]

        if i % 2:
            pos_x = pos_x + mod_x
            pos_y = pos_y + mod_y
            grid[pos_x][pos_y].append(1)
        else:
            rob_pos_x = rob_pos_x + mod_x
            rob_pos_y = rob_pos_y + mod_y
            grid[rob_pos_x][rob_pos_y].append(1)

    # count the number of house visited at least once
    print(sum(
        len(line.values())
        for line in grid.values()
    ))
