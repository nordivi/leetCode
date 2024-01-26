from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        l = len(nums)
        if len(set(nums)) == 1 and nums[0] == val:
            return 0
        for num in nums:
            if num == val:
                last = -1
                while nums[last] == val:
                    last-=1
                if k - last - 1 == l:
                    return k
                nums[k] = nums[last]
                nums[last] = val
            k+=1
        return k

sol = Solution()
res = sol.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
print()