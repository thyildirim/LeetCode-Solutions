"""
LeetCode Problem 35: Search Insert Position
Difficulty: Easy
Link: https://leetcode.com/problems/search-insert-position
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target < nums[i]:
                return i

        return len(nums)


a = Solution()
print(a.searchInsert(nums = [0,1,3,6],target = 5 )) # Answer : 3