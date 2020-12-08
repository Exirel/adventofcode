"""Advent of Code 2020, day 8, star 1"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


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


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    program = parse_program(raw_input.strip())
    accumulator = 0
    position = 0
    visited = []

    while True:
        visited.append(position)
        instruction, value = program[position]
        operation = INSTRUCTIONS[instruction]
        position, accumulator = operation(position, accumulator, value)

        print('%d\t%d\t%d (%s %s)' % (
            visited[-1], accumulator, position, instruction, value
        ))

        if position in visited:
            break

        if position not in program:
            raise RuntimeError('Program instruction overflow')

    print(accumulator)
