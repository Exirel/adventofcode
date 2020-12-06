"""Advent of Code 2015, day 15, star 1"""
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


if __name__ == "__main__":

    items = (
        (a, b, c, 100 - a - b - c)
        for a in range(1, 98)
        for b in range(1, 99 - a)
        for c in range(1, 100 - a - b)
    )

    # Got this from the input file - hard-coding solution here!
    mod_a = (4, -2, 0, 0, 5)
    mod_b = (0, 5, -1, 0, 8)
    mod_c = (-1, 0, 5, 0, 6)
    mod_d = (0, 0, -2, 2, 1)

    w, x, y, z = 0, 1, 2, 3

    items = (
        (
            (mod_a[w] * a + mod_b[w] * b + mod_c[w] * c + mod_d[w] * d),
            (mod_a[x] * a + mod_b[x] * b + mod_c[x] * c + mod_d[x] * d),
            (mod_a[y] * a + mod_b[y] * b + mod_c[y] * c + mod_d[y] * d),
            (mod_a[z] * a + mod_b[z] * b + mod_c[z] * c + mod_d[z] * d),
        )
        for a, b, c, d in items
    )

    items = (
        i * j * k * l
        for i, j, k, l in items
        if i > 0 and j > 0 and k > 0 and l > 0
    )

    print(max(items))
