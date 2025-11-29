#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    total = 0
    for num in argv:
        total += int(num)
    print(total)
