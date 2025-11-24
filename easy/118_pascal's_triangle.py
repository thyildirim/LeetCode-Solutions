"""
LeetCode Problem 118: Pascal's Triangle
Difficulty: Easy
Link: https://leetcode.com/problems/pascals-triangle
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            # Start each row with 1
            row = [1]

            # Middle values (from the previous row)
            if i > 0:
                prev = result[i - 1]
                for j in range(len(prev) - 1):
                    row.append(prev[j] + prev[j + 1])

                # End each row with 1 (except the very first row)
                row.append(1)

            result.append(row)

        return result





        