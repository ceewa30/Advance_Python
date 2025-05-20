# This iterator prints all values in order from the passed container. IUt restarts printing from the beginning again when all values are printed.
# Example: cycle([1, 2, 3]) will print 1, 2, 3, 1, 2, 3, ...

import itertools
count = 0

for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end=" ")
        count += 1