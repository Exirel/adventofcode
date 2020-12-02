"""Advent of Code 2020, day 2, star 1"""
import os
import re


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
PATTERN = r'^(?P<min>\d+)-(?P<max>\d+)\s(?P<char>\w):\s(?P<password>\w+)$'


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    # extract the data from each line
    regex = re.compile(PATTERN)
    clean_data = (
        regex.match(line)
        for line in raw_input.strip().splitlines()
        if line
    )

    # get min, max, the character to be found, and the password from each match
    clean_data = (
        (
            int(match.group('min')),
            int(match.group('max')),
            match.group('char'),
            match.group('password'),
        )
        for match in clean_data
        if match is not None
    )

    # count the number of requested character in each password
    clean_data = (
        (
            min_bound,
            max_bound,
            password,
            len(list(c for c in password if c == character)),
        )
        for min_bound, max_bound, character, password in clean_data
    )

    # count the number of passwords that comply with the min/max boundaries
    print(len(list(
        password
        for min_bound, max_bound, password, count in clean_data
        if min_bound <= count <= max_bound
    )))
