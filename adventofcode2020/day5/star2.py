"""Advent of Code 2020, day 5, star 2"""
from star1 import get_seat_column, get_seat_row, INPUT_FILE


if __name__ == "__main__":
    # get raw input from text file
    with open(INPUT_FILE, 'r', encoding='utf-8') as fd:
        raw_input = fd.read()

    # get all the seat IDs, sorted
    seat_ids = sorted(
        get_seat_row(seat) * 8 + get_seat_column(seat)
        for seat in raw_input.strip().splitlines()
    )

    # let's find the one that is exactly at seat -1 < seat < seat + 1
    for i, seat_id in enumerate(seat_ids):
        try:
            next_seat_id = seat_ids[i + 1]
        except IndexError:
            # I'm lazy, I'd just check if i +  1 exists, but meh.
            pass
        else:
            if next_seat_id == seat_id + 2:
                # we found a gap of exactly 1 seat
                print('Gap between %d and %d' % (seat_id, next_seat_id))
