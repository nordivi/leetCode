# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def is_happy(n: int) -> bool:
    seen = [n]
    while n != 1:
        n = sum([int(i)**2 for i in str(n)])
        if n in seen:
            return False
        seen.append(n)
    return True

if __name__ == '__main__':
    is_happy(19)