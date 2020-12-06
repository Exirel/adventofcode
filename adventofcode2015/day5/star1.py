"""Advent of Code 2015, day 5, star 1"""
import os
import string


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
VOWELS = {'a', 'e', 'i', 'o', 'u'}
DOUBLE_LETTERS = set(
    left + right
    for left, right in zip(string.ascii_lowercase, string.ascii_lowercase))
FORBIDDEN_COMBO = {'ab', 'cd', 'pq', 'xy'}


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    words = (
        # get the windowed version of the word, with 2 chars for each window
        (word, set(word[i:i+2] for i in range(0, len(word) - 1)))
        for word in raw_input.splitlines()
        # it contains at least three vowels (aeiou only) (aaa is valid)
        if sum(word.count(vowel) for vowel in VOWELS) >= 3
    )

    words = (
        word
        for word, windowed in words
        if windowed & DOUBLE_LETTERS and not windowed & FORBIDDEN_COMBO
    )

    print(sum(1 for word in words))
