"""Advent of Code 2015, day 2, star 1"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    packages = (
        tuple(int(x) for x in line.split('x'))
        for line in raw_input.strip().splitlines()
    )

    packages = (
        (l, w, h, 2 * l * w + 2 * w * h + 2 * h * l, sorted([l, w, h])[0:2])
        for l, w, h in packages
    )

    packages = (
        size + smaller[0] * smaller[1]
        for l, w, h, size, smaller in packages
    )

    print(sum(packages))
