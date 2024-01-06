#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)

    if n == 0:
        print(0)
    else:
        sum = 0
        for i in range(1, n):
            sum += int(sys.argv[i])
    print(sum)
