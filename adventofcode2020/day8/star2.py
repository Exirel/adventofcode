"""Advent of Code 2020, day 8, star 2"""
import copy

from star1 import INPUT_FILE, parse_program, run_until_loop, ProgramExit


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    program = parse_program(raw_input.strip())
    program_run = copy.deepcopy(program)
    modified = None
    tried = []

    while True:
        # run the modified program to see if it has a loop or if it exit
        try:
            position, accumulator, visited = run_until_loop(program_run)
        except ProgramExit as error:
            # modified program exited: it is good!
            print(error)
            break

        # look at the last visited instructions, and look for jmp/nop
        program_alter = (
            (i, program[i])
            for i in reversed(visited)
            # don't try to alter an operation already tried
            # we already know that didn't work
            if i not in tried
        )

        program_alter = (
            (i, op_val)
            for i, op_val in program_alter
            # change jump or non-zero nop
            if op_val[0] == 'jmp' or (op_val[0] == 'nop' and op_val[1] != 0)
        )

        i, op_val = next(program_alter)
        new_op_val = (
            # switch operation
            'jmp' if op_val[0] == 'nop' else 'nop',
            # keep the same value
            op_val[1],
        )

        # update a copy of the program to be run, only at that position
        program_run = copy.deepcopy(program)
        program_run[i] = new_op_val
        # remember that we tried this
        tried.append(i)

        print('Program modified at %d: %r => %r' % (i, op_val, new_op_val))
