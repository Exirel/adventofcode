"""Advent of Code 2020, day 6, star 1"""
import functools
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    # get all the answers, per group
    dataset = (
        # each group is a tuple
        # each person's answers in a group is a set
        tuple(set(line) for line in group_answers.splitlines())
        for group_answers in raw_input.strip().split('\n\n')
    )

    dataset_reduced = (
        # combine answers together per group, and get the total length
        len(functools.reduce(lambda x, y: x | y, group_answers))
        for group_answers in dataset
    )

    print(sum(dataset_reduced))
