# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.

from typing import List
def plus_one(digits: List[int]) -> List[int]:
    return [int(i) for i in str(int(''.join([str(d) for d in digits])) + 1).split()[0]]

if __name__ == '__main__':
    plus_one([1,2,3])