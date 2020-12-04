"""Advent of Code 2020, day 4, star 2

`Parse, don't validate`__.

.. __: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/
"""
import os
import re


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
REGEX_HGT = re.compile(r'(?P<hgt>\d+)(?P<unit>(?:in)|(?:cm))')
REGEX_HCL = re.compile(r'^#[0-9abcdefABCDEF]{6}$')


def _parse_digit(data, length, min_bound, max_bound):
    assert min_bound <= max_bound

    if len(data) != length or not data.isdigit():
        return None

    if not min_bound <= int(data) <= max_bound:
        return None

    return data


def parse_passport(data):
    """Parse passport, keeping valid keys only."""
    fields = (
        # each field is composed of `key:value`
        key_val.split(':')
        for key_val in data.split()
    )
    fields = (
        (key, PASSPORT_KEYS[key][2](value))
        for key, value in fields
        if key in PASSPORT_KEYS
    )
    passport = dict(
        (key, value)
        for key, value in fields
        if value is not None
    )
    return passport


def parse_byr(data):
    """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
    return _parse_digit(data, 4, 1920, 2002)


def parse_iyr(data):
    """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
    return _parse_digit(data, 4, 2010, 2020)


def parse_eyr(data):
    """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
    return _parse_digit(data, 4, 2020, 2030)


def parse_hgt(data):
    """hgt (Height) - a number followed by either cm or in.

    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    match = REGEX_HGT.match(data)

    if match is None:
        return None

    value, unit = match.group('hgt'), match.group('unit')

    if unit == 'cm' and not 150 <= int(value) <= 193:
        return None

    if unit == 'in' and not 59 <= int(value) <= 76:
        return None

    return (value, unit)


def parse_hcl(data):
    """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
    if REGEX_HCL.match(data) is None:
        return None

    return data


def parse_ecl(data):
    """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
    return dict(
        (x, x) for x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    ).get(data, None)


def parse_pid(data):
    """pid (Passport ID) - a nine-digit number, including leading zeroes."""
    if len(data) != 9 or not data.isdigit():
        return None

    return data


def parse_cid(data):
    """cid (Country ID) - optional, no specification."""
    return data


PASSPORT_KEYS = {
    'byr': ('Birth Year', True, parse_byr),
    'iyr': ('Issue Year', True, parse_iyr),
    'eyr': ('Expiration Year', True, parse_eyr),
    'hgt': ('Height', True, parse_hgt),
    'hcl': ('Hair Color', True, parse_hcl),
    'ecl': ('Eye Color', True, parse_ecl),
    'pid': ('Passport ID', True, parse_pid),
    'cid': ('Country ID', False, parse_cid),
}
REQUIRED_KEYS = {key for key, info in PASSPORT_KEYS.items() if info[1]}


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    # get a list of passport
    passports = (
        # each field is separated by a space or break line
        parse_passport(passport)
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
