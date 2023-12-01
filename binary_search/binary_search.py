# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.

def search(nums, target):
    return nums.index(target) if target in nums else -1


if __name__ == '__main__':
    search([1,2,3,4,5,6], 9)