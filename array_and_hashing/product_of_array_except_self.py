"""Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation."""


class Solution:
    def productExceptSelf(self, nums):
        n, ans, suffix_prod = len(nums), [1]*len(nums), 1
        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]
        for i in range(n-1,-1,-1):
            ans[i] *= suffix_prod
            suffix_prod *= nums[i]
        return ans