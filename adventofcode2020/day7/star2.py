"""Advent of Code 2020, day 7, star 2"""

from star1 import INPUT_FILE, MY_BAG, parse_rule


def count_bags_in(name, bags_rules):
    current_holding = bags_rules.get(name, dict())

    # return the number of bags + the number of bags in said bags
    return sum(
        multiplier * (count_bags_in(bag, bags_rules) + 1)
        for bag, multiplier in current_holding.items()
    )


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    # parse rules
    rules = (
        parse_rule(line)
        for line in raw_input.strip().splitlines())

    print(count_bags_in(MY_BAG, dict(rules)))
