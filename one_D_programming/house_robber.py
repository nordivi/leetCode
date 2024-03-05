
def rob(nums):
    if len(nums) == 0:
        return 0
    prev1 = 0
    prev2 = 0
    for num in nums:
        current = max(prev2 + num, prev1)
        prev2 = prev1
        prev1 = current
    return prev1

rob([1,2,3,4,5,3,4,2,3,3,5,5,3,4,2,3,12])