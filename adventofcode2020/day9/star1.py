"""Advent of Code 2020, day 9, star 1"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
PREAMBLE = 25


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    numbers = list(
        int(line)
        for line in raw_input.strip().splitlines()
    )

    invalid_numbers = (
        number
        for i, number in enumerate(numbers[PREAMBLE:])
        if not any(
            number == x + y
            for x in numbers[i:i + PREAMBLE]
            for y in numbers[i:i + PREAMBLE]
        )
    )

    print(next(invalid_numbers))
