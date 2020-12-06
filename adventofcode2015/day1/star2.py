"""Advent of Code 2015, day 1, star 2"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    floor = 0
    position = 0
    for i, c in enumerate(raw_input):
        if c == '(':
            floor = floor + 1
        else:
            floor = floor - 1

        if floor < 0:
            position = i + 1
            break

    print(position)
