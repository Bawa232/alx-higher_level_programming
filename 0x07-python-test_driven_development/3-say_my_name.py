#!/usr/bin/python3
""" module that prints a person's first and last name """


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: a string with the user's first name
        last_name: a string with is last name

    Returns:
            prints a string wit te user's first & last names

    Raises:
        TypeError if first name is not a string
        TypeError if second name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
