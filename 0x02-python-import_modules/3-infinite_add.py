#!/usr/bin/python3
import sys
if __name__ == "__main__":
    infiniteSum = 0
    for i in range(1, len(sys.argv)):
        infiniteSum += int(sys.argv[i])
    print(f"{infiniteSum :d}")
