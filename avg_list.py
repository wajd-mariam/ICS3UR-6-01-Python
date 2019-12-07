#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: December 2019
# This program calculates the average of numbers in a list.

import random


def average_of_numbers(random_numbers):
    # this function calculates average

    total = 0

    for loop_counter in range(0, 10):
        total = (total + random_numbers[loop_counter])

    return (total / 10)


def main():
    # this function calcuates the average of randomized numbers

    list_random = []
    average = 0

    # input
    print("The randomized numbers are:")
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        list_random.append(random_number)
        print("{0}, ".format(random_number), end="")
    print("")

    average = average_of_numbers(list_random)

    print("The average of all numbers is {0}".format(average))


if __name__ == "__main__":
    main()
