"""Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
 """
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r =  0, len(height) - 1

        left_max, right_max = height[l], height[r]
        result = 0

        while l < r:
            if left_max < right_max:
                l+=1
                left_max = max(left_max, height[l])
                result += left_max - height[l]
            else:
                r-=1
                right_max = max(right_max, height[r])
                result += right_max - height[r]
        return result


if __name__ == '__main__':
    sol = Solution()
    water = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(water)