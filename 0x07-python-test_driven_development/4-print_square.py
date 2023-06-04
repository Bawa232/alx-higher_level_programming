#!/usr/bin/python3
""" module that prints a square if a given size """


def print_square(size):
    """
        Args:
            Size: the size of the square to be printed

        Raises:
            TypeError: is size is not an integer
            ValueErrror: if size is less than 0

        Returns:
            Prints a square of the given size

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print(f"#", end="")
        print()
