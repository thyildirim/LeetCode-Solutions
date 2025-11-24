"""
LeetCode Problem 383: Ransom Note
Difficulty: Easy
Link: https://leetcode.com/problems/ransom-note
"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))

a = Solution()
print(a.canConstruct("a","b")) #FALSE
print(a.canConstruct("a","a")) #TRUE
print(a.canConstruct("ha","taha")) #TRUE
print(a.canConstruct("taha","ha")) #FALSE

