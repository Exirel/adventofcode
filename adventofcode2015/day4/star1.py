"""Advent of Code 2015, day 4, star 1"""
from hashlib import md5
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    key = raw_input.strip().encode('utf-8')

    i = 0
    while True:
        i = i + 1
        if md5(key + b'%d' % i).hexdigest().startswith('00000'):
            break

    print(i)
