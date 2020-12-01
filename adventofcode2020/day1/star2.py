"""Advent of Code 2020, day 1, star 2"""
import itertools
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    # remove trailing spaces, split by lines, and cast as int
    clean_data = list(map(int, raw_input.strip().splitlines()))

    # get the three dates (x, y, z) where x + y + z == 2020
    years = [
        (x, y, z)
        # get all (sorted) combinations of three dates from the clean list
        for x, y, z in itertools.combinations(clean_data, 3)
        if x + y + z == 2020
    ][0]  # always assume one exists

    year_a, year_b, year_c = years
    print('%d * %d * %d == %d' % (
        year_a,
        year_b,
        year_c,
        year_a * year_b * year_c,
    ))
