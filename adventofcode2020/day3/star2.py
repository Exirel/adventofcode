"""Advent of Code 2020, day 3, star 2"""
import functools
import os

import star1


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
SLOPES = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)


if __name__ == "__main__":
    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    world = star1.make_world(raw_input)

    print(functools.reduce(lambda x, y: x * y, (
        star1.tree_found(world, (0, 0), slope)
        for slope in SLOPES
    )))
