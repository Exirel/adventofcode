"""Advent of Code 2020, day 4, star 1"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
PASSPORT_KEYS = {
    'byr': ('Birth Year', True),
    'iyr': ('Issue Year', True),
    'eyr': ('Expiration Year', True),
    'hgt': ('Height', True),
    'hcl': ('Hair Color', True),
    'ecl': ('Eye Color', True),
    'pid': ('Passport ID', True),
    'cid': ('Country ID', False),
}
REQUIRED_KEYS = {key for key, info in PASSPORT_KEYS.items() if info[1]}


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    # get a list of passport
    passports = (
        # each field is separated by a space or break line
        dict(
            # each field is composed of `key:value`
            key_val.split(':')
            for key_val in passport.split()
        )
        # each passport is separated by a blank line == 2 break lines
        for passport in raw_input.strip().split('\n\n')
    )

    print(sum(
        1
        for passport in passports
        # a passport is valid if and only if it has all the required keys
        # dict.keys() is compatible with a union operation (&) on a set
        if (passport.keys() & REQUIRED_KEYS) == REQUIRED_KEYS
    ))
