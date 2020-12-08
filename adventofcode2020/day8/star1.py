"""Advent of Code 2020, day 8, star 1"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


class ProgramExit(Exception):
    """Exception raised when a program exit."""
    def __init__(self, position, accumulator, visited):
        self.position = position
        self.accumulator = accumulator
        self.visited = visited
        super().__init__(
            'Program exit at %d with value %d' % (position, accumulator))


def accumulate(position, accumulator, value):
    """Implement the ``acc`` instruction.

    ``acc`` increases or decreases a single global value called the
    ``accumulator`` by the ``value`` given in the argument.

    For example, ``acc +7`` would increase the accumulator by 7. The
    accumulator starts at 0. After an ``acc`` instruction, the instruction
    immediately below it is executed next.
    """
    return position + 1, accumulator + int(value)


def jump(position, accumulator, value):
    """Implement the ``jmp`` instruction.

    ``jmp`` jumps to a new instruction relative to itself. The next instruction
    to execute is found using the argument as an offset from the ``jmp``
    instruction.

    For example, ``jmp +2`` would skip the next instruction, ``jmp +1`` would
    continue to the instruction immediately below it, and ``jmp -20`` would
    cause the instruction 20 lines above to be executed next.
    """
    return position + int(value), accumulator


def noop(position, accumulator, value):
    """Implement the ``nop`` instruction.

    ``nop`` stands for "No OPeration" - it does nothing. The instruction
    immediately below it is executed next.
    """
    return position + 1, accumulator


INSTRUCTIONS = {
    'acc': accumulate,
    'jmp': jump,
    'nop': noop,
}


def parse_program(raw):
    """Parse a program composed of ``acc``, ``jmp``, and ``nop`` instructions.

    :param str raw: a raw string of one instruction per line
    :return: a ``dict`` of instructions as ``(position: (instruction, value))``
    :rtype: dict
    """
    return {
        i: (value[:3], int(value[4:]))
        for i, value in enumerate(raw.splitlines())
    }


def run_until_loop(program):
    """Run the ``program`` until it loop or exit properly.

    :param dict program: a dict of instruction where each key is a position,
                         and each value is the operation to perform at said
                         position (including its value)
    :return: a 3-value tuple of next position, current accumulator,
             and the list of visited instructions
    :rtype: tuple
    :raise ProgramExit: when the program ends at a position that doesn't exist

    The program is a "boot code": the boot code is represented as a text file
    with one instruction per line of text. Each instruction consists of an
    operation (acc, jmp, or nop) and an argument (a signed number like +4 or
    -20).

    Each operation is mapped into the ``INSTRUCTIONS`` dict.
    """
    accumulator = 0
    position = 0
    visited = []

    while True:
        visited.append(position)
        instruction, value = program[position]
        operation = INSTRUCTIONS[instruction]
        position, accumulator = operation(position, accumulator, value)

        # want to debug?
        """
        print('%d\t%d\t%d (%s %s)' % (
            visited[-1], accumulator, position, instruction, value
        ))
        """

        if position in visited:
            # loop detected, we stop execution
            break

        if position not in program:
            # would jump to a non-existing position; exit program
            raise ProgramExit(position, accumulator, visited)

    return position, accumulator, visited


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    program = parse_program(raw_input.strip())
    position, accumulator, visited = run_until_loop(program)

    print(accumulator)
