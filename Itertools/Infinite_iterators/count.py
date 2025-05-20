# This iterator starts printing from "start" number and prints infinitely. if steps are provided, it will print the numbers in steps of "step" number.
# Example: count(5, 5) will print 5, 10, 15, 20, 25, 30, 35, ...
# Example: count(5) will print 5, 6, 7, 8, 9, 10, ...
# Example: count() will print 0, 1, 2, 3, 4, 5, ...


import itertools

for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")
