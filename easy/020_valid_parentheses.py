"""
LeetCode Problem 20: Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if char == ')' and top != '(':
                    return False
                if char == '}' and top != '{':
                    return False
                if char == ']' and top != '[':
                    return False

        return not stack

a = Solution()
print(a.isValid("()")) #True
print(a.isValid("(]")) #False
print(a.isValid("([)]")) #False
print(a.isValid("{[]}")) #True
print(a.isValid("{{{((()))}}]")) #False
print(a.isValid("{{{((()))}}}")) #True

