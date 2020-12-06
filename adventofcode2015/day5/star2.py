"""Advent of Code 2015, day 5, star 2"""
import os
import re


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
DOUBLE_REGEX = re.compile(r'(\w{2})(\1|(.+\1))')
"""Regex for double letters.

It contains a pair of any two letters that appears at least twice in the string
without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa
(aa, but it overlaps).
"""

PAL_REGEX = re.compile(r'(\w).\1')
"""Regex for repeating pattern.

It contains at least one letter which repeats with exactly one letter between
them, like xyx, abcdefeghi (efe), or even aaa.
"""


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    words = (
        word
        for word in raw_input.strip().splitlines()
        if DOUBLE_REGEX.search(word) is not None and
        PAL_REGEX.search(word) is not None
    )

    print(sum(1 for word in words))
