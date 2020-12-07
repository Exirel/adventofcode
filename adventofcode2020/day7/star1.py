"""Advent of Code 2020, day 7, star 1"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
MY_BAG = 'shiny gold bags'


def norm_key(raw):
    if raw.endswith('bag'):
        return raw + 's'

    return raw


def norm_value(raw):
    if raw == 'no':
        return 0

    return int(raw)


def parse_rule(raw):
    """Parse a bag rule.

    Format looks like either one of these:

        color bags contain X color bags, Y color bags.
        color bags contain no other bags.

    So I can split the sentence with ` contain `, and split the second part
    on `, ` (after stripping `.` of course).

    The end result is a tuple with the bag color, and the dict of what the bag
    can hold in it, where keys are bag color and values are number for each.
    """
    bag, holding = raw.split(' contain ')
    holding = (
        reversed(bags.split(' ', maxsplit=1))
        for bags in holding.rstrip('.').split(', ')
    )

    return bag, {
        norm_key(key): norm_value(value)
        for key, value in holding
    }


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    # parse rules
    rules = (
        parse_rule(line)
        for line in raw_input.strip().splitlines())

    # ignore rules that contains no bags
    rules = (
        (bag, holding)
        for bag, holding in rules
        if holding.get('other bags') is None)

    valid_bags = set()
    found = 0
    bags_rules = {
        bag: set(holding.keys())
        for bag, holding in rules
    }

    while True:
        # look for every possible bags that contains any of the found bags
        for bag, holding in bags_rules.items():
            if bag in valid_bags:
                # already known; skip it!
                continue

            if MY_BAG in holding:
                print('%s => direct' % bag)
                valid_bags.add(bag)

            elif holding & valid_bags:
                print('%s => contain (%s)' % (bag, holding & valid_bags))
                valid_bags.add(bag)

        print('There are %s valid bags' % len(valid_bags))

        print('--------------------------------------------------')

        # how many did we found? check for exit condition
        new_found = len(valid_bags)
        if found == new_found:
            break
        found = new_found

    print(found)
