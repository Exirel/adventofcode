"""Advent of Code 2020, day 3, star 1"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
TILE_TREE = '#'


class OutOfBound(ValueError):
    """Out of bound value error for a X or Y position in a world"""


def take_slope(world, pos, slope):
    """Return the next position according to current ``pos`` and a ``slope``.

    :param dict world: a dict of dict of the world as ``[y][x] == tile``
    :param tuple pos: the current position as ``(x, y)``
    :param tuple slope: the slope parameter as ``(x modifier, y modifier)``
    :raise OutOfBound: when the new Y would be out of bound of the world
    :return: a 2-value tuple of ``(new_pos, is_tree)``

    The world is composed of a section that repeat itself on the x-axis, so
    the new X position is relative to the size of the world at the Y level.
    """
    # get current position and slope modifiers
    pos_x, pos_y = pos
    slope_x, slope_y = slope

    # apply the slope to the current position to get the next one
    new_pos_x = pos_x + slope_x
    new_pos_y = pos_y + slope_y

    # if the new Y position is out of bound, raise
    if new_pos_y not in world:
        raise OutOfBound('Out of bound Y: %d (was %d)' % (new_pos_y, pos_y))

    # get the line on the Y axis
    line_y = world[new_pos_y]
    # get the relative X position, since the world repeat on the X axis
    new_rel_pos_x = new_pos_x % len(line_y)

    # return the new position and tell if it's a tree or not
    return (new_pos_x, new_pos_y), line_y[new_rel_pos_x] == TILE_TREE


def walkthrough(world, pos, slope):
    """Yield each position in a world starting at ``pos`` using a ``slope``

    :param dict world: a dict of dict of the world as ``[y][x] == tile``
    :param tuple pos: the current position as ``(x, y)``
    :param tuple slope: the slope parameter as ``(x modifier, y modifier)``
    :return: a generator for each new position in the world until it reach
             the boundary on the Y axis (the world repeat itself on the X axis)
    """
    while True:
        try:
            pos, is_tree = take_slope(world, pos, slope)
            yield pos, is_tree
        except OutOfBound:
            break


def solve(raw_data):
    """Solve the problem for Day 3 Star 1"""
    # parse the world into a dict of dict structure
    world = {
        y: dict(enumerate(line))
        for y, line in enumerate(raw_data.strip().splitlines())
    }

    # initial position and slope
    slope = (3, 1)
    pos = (0, 0)

    # compute slope the world
    return sum(
        1 for line in walkthrough(world, pos, slope) if line[1] is True
    )


if __name__ == "__main__":
    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    print(solve(raw_input))
