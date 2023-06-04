#!/usr/bin/python3
""" a script that prints a text wit two bew lines after it encounters certain characters """


def text_indentation(text):
    """
        Args:
            text: the text to be indented

        Raises:
            TypeError: if text is not a string

        Returns:
            prints the formatted string; text

    """

    if(type(text) is not str):
        raise TypeError("text must be a string")

    i = 0
    for _ in range(len(text)):
        if (i <= len(text) - 1):
            if(i == 0):
                while (text[i] == " "):
                    i += 1
                    if i == len(text):
                        break
            print(text[i], end="")
            if (text[i] == "." or text[i] == "?" or text[i] == ":"):
                print()
                print()
                if (i < len(text) - 1 and text[i + 1] == " "):
                    i += 1
                    while (text[i] == " "):
                        i += 1
                        if i == len(text):
                            break
                else:
                    i += 1
            else:
                i += 1
