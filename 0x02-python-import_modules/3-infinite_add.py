#!/usr/bin/python3
import sys

if __name__ == "__main__":
    len = len(sys.argv)
    sum = 0

    if len > 1:
        for i in range(1, len):
            sum = sum + int(sys.argv[i])

        print("{}".format(sum))
