"""Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
 """
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        nums_set = set(nums)
        for num in nums_set:
            counter[num] = nums.count(num)
        return list(dict(sorted(counter.items(), key = lambda x: -x[1])).keys())[:k]

