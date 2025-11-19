"""
LeetCode Problem 0: Palindrome Number
Difficulty: Easy
Link: https://leetcode.com/problems/palindrome-number
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
xa = Solution()
print(xa.isPalindrome(121))
print(xa.isPalindrome(-121))
print(xa.isPalindrome(0))