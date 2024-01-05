#!/usr/bin/python3
def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.
    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of three and five, print FizzBuzz instead of the number.
    """
    for number in range(1, 101):
        output = ""
        if number % 3 == 0:
            output += "Fizz"
        if number % 5 == 0:
            output += "Buzz"
        if not output:
            output = str(number)
        print(output, end=" ")

