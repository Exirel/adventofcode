"""Advent of Code 2015, day 2, star 2"""
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
        (
            # The ribbon required to wrap a present is the shortest distance
            # around its sides, or the smallest perimeter of any one face.
            2 * sorted([l + w, l + h, w + h])[0],
            # The feet of ribbon required for the perfect bow is equal to
            # the cubic feet of volume of the present
            l * w * h,
        )
        for l, w, h in packages
    )

    packages = (
        wrap + bow
        for wrap, bow in packages
    )

    print(sum(packages))
