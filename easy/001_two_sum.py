"""
LeetCode Problem 1: Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 22))  # Output: [1,3]
