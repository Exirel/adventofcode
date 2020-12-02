"""Advent of Code 2020, day 2, star 2"""
import os
import re


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
PATTERN = r'^(?P<pos1>\d+)-(?P<pos2>\d+)\s(?P<char>\w):\s(?P<password>\w+)$'


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
            int(match.group('pos1')) - 1,
            int(match.group('pos2')) - 1,
            match.group('char'),
            match.group('password'),
        )
        for match in clean_data
        if match is not None
    )

    # count the number of passwords that comply with the real password policy
    print(len(list(
        password
        for pos1, pos2, c, password in clean_data
        if (int(password[pos1] == c) + int(password[pos2] == c)) == 1
    )))
