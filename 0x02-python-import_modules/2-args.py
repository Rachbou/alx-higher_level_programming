#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count == 0:
        print(f"{count} arguments.")
    elif count == 1:
        print(f"{count} argument:")
    else:
        print(f"{count} arguments:")
    for i in range(1, count + 1):
        print(f"{i}: {sys.argv[i]}")
