"""
LeetCode Problem 58: Length of Last Word
Difficulty: Easy
Link: https://leetcode.com/problems/length-of-last-word
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        count = 0
        for i in range(len(s) -1 , -1 ,-1 ):
            if s[i] ==  " ":
                break
            count = count + 1
        return count


a = Solution()
print(a.lengthOfLastWord("taha ")) # 4
