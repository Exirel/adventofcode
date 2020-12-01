"""Advent of Code 2020, day 1, star 1"""
import itertools
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    # remove trailing spaces, split by lines, and cast as int
    clean_data = list(map(int, raw_input.strip().splitlines()))

    # get the two dates (x, y) where x + y == 2020
    years = [
        (x, y)
        # get all (sorted) combinations of two dates from the clean list
        for x, y in itertools.combinations(clean_data, 2)
        if x + y == 2020
    ][0]  # always assume one exists

    year_a, year_b = years
    print('%d * %d == %d' % (year_a, year_b, year_a * year_b))
