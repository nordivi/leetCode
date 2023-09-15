"""Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once."""
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26  # letras do alfabeto || alphabet letters
            for c in string:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(string)

        return res.values()


