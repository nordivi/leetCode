"""Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        response = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                soma = nums[l] + num + nums[r]

                if soma > 0:
                    r-=1
                elif soma < 0:
                    l+=1
                else:
                    response.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1

        return response


