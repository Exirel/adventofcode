"""Advent of Code 2020, day 10, star 1"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    adapters = list(sorted(
        int(adapter)
        for adapter in raw_input.strip().splitlines()
    ))

    adapters_diff = (
        (adapter, adapter - adapters[i-1] if i > 0 else adapter)
        for i, adapter in enumerate(adapters)
    )

    diff_1 = []
    diff_3 = []
    for adapter, diff in adapters_diff:
        if diff > 3:
            raise Exception(
                'Not every possible adapters: %d, %d diff' % (adapter, diff))

        if diff == 1:
            diff_1.append(adapter)
        elif diff == 3:
            diff_3.append(adapter)

    count_diff_1 = len(diff_1)
    count_diff_3 = len(diff_3) + 1  # +1 your device has a +3 diff too!

    print(count_diff_1, count_diff_3, count_diff_1 * count_diff_3)
