# This iterator repeatedly prints the passed value. It will print the value infinitely.
# Example: repeat(5) will print 5, 5, 5, 5, 5, ...

import itertools

print("Printing the numbers repeatedly : ")
print(list(itertools.repeat(25, 5)))  # Repeat the number 5, 5 times