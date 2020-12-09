"""Advent of Code 2020, day 9, star 2"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
XMAS_INVALID = 15353384
"""Invalid XMAS number found with star1 - let's not recompute that!"""


def get_numbers_until_invalid(iterable, xmas_invalid):
    for i in iterable:
        if i == xmas_invalid:
            break
        yield i


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    numbers = list(get_numbers_until_invalid((
        int(line)
        for line in raw_input.strip().splitlines()
    ), XMAS_INVALID))

    total = 0
    start = 0

    # Loop between every possible ranges (start:invalid number)
    while total != XMAS_INVALID and numbers[start:]:
        total = 0
        print('')
        print('*☆*――*☆*――*☆*――*☆*――*☆*――*☆*――*☆*――*☆*――*☆*――*☆*――*☆*――*☆*')
        print('Start iteration at %d, looking for %d' % (start, XMAS_INVALID))

        for rel_pos, number in enumerate(numbers[start:]):
            pos = start + rel_pos

            # did we reach a bad number?
            if number > XMAS_INVALID:
                # reset total and start again after that bad number
                print('Found %d at position %i must start again.' % (
                    number, pos
                ))
                total = 0
                start = pos + 1
                break

            # let's update the total
            # total = sum(numbers[start:pos+1])
            total = total + number

            # did we reach the XMAS_INVALID?
            if total == XMAS_INVALID:
                print('We found it at [%d:%d]' % (start, pos+1))
                break

            # we are too low: just continue
            if total > XMAS_INVALID:
                break

        if total == XMAS_INVALID:
            # we are done here
            print('We are done here')
            break

        if total == 0:
            # we have to do another round
            print('We need another round')
            continue

        # we are too high, we need to remove numbers from the begining
        print('We reach a value to high for [%d:%d] == %d' % (
            start,
            pos + 1,
            total,
        ))
        print('Starting to decrease from start=%d...' % start)
        for i in range(start, pos+2):
            start = i + 1
            total = total - numbers[i]

            if total == XMAS_INVALID:
                print('We found it at [%d:%d]' % (start, pos+1))
                assert sum(numbers[start:pos+1]) == XMAS_INVALID
                valid_numbers = sorted(numbers[start:pos+1])
                low, high = valid_numbers[0], valid_numbers[-1]
                print('Result: %d + %d == %d' % (low, high, low + high))
                break

            if total < XMAS_INVALID:
                print('We got below, next up at [%d:]' % start)
                total = 0
                break
