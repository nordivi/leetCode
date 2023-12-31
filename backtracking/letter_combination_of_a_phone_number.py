# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


def letter_combination(digits):
    phone_dict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    res = []

    def backtrack(i, cur):
        if len(cur) == len(digits):
            res.append(cur)
            return
        for c in phone_dict[digits[i]]:
            backtrack(i+1, cur + c)

    if digits:
        backtrack(0, "")

    return res
