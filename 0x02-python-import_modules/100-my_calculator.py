#!/usr/bin/python3
"""imports all functions from the file and handles basic operations."""
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    n = len(sys.argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    valid_operator = ['+', '-', '*', '/']

    if operator not in valid_operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

        result = 0

    if operator == '-':
        result = sub(a, b)
    elif operator == '+':
        result = add(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)

print(f"{a} {operator} {b} =", result)
