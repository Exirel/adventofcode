"""Advent of Code 2015, day 1, star 1"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    print(raw_input.count('(') - raw_input.count(')'))
