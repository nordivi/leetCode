"""A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise."""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s_list = []
        for letter in s:
            if letter.lower() in letters:
                s_list.append(letter.lower())
        return s_list == s_list[::-1]