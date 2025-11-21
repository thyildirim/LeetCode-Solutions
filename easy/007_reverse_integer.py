"""
LeetCode Problem 007: Reverse Integer
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-integer
"""


class Solution:
    def reverse(self, x: int) -> int:

        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        if x < 0:
            sign = -1
        else:
            sign = 1

        x_abs = abs(x)
        reversed_num = int(''.join(reversed(str(x_abs))))

        result = sign * reversed_num

        if result < INT_MIN or result > INT_MAX:
            return 0
        return result
