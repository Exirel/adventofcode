"""Advent of Code 2020, day 5, star 1"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def get_seat_row(seat):
    """Figure out the row from a seat.

    The first 7 characters will either be F or B; these specify exactly one of
    the 128 rows on the plane (numbered 0 through 127). Each letter tells you
    which half of a region the given seat is in.

    Start with the whole list of rows; the first letter indicates whether the
    seat is in the front (0 through 63) or the back (64 through 127). The next
    letter indicates which half of that region the seat is in, and so on until
    you're left with exactly one row.
    """
    # we take only the first seven letters
    # F is 0, B is 1
    # we get a base 2 int for the seat row
    seat_binary = seat[0:7].replace('F', '0').replace('B', '1')
    return int(seat_binary, 2)


def get_seat_column(seat):
    """Figure out the column from a seat.

    The last three characters will be either L or R; these specify exactly one
    of the 8 columns of seats on the plane (numbered 0 through 7). The same
    process as above proceeds again, this time with only three steps. L means
    to keep the lower half, while R means to keep the upper half.
    """
    # we take only the last three letters
    # L is 0, R is 1
    # we get a base 2 int for the seat row
    seat_binary = seat[-3:].replace('L', '0').replace('R', '1')
    return int(seat_binary, 2)


if __name__ == "__main__":

    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    # As a sanity check, look through your list of boarding passes.
    # What is the highest seat ID on a boarding pass?
    print(max(
        # Every seat also has a unique seat ID:
        # multiply the row by 8, then add the column.
        get_seat_row(seat) * 8 + get_seat_column(seat)
        for seat in raw_input.strip().splitlines()
    ))
