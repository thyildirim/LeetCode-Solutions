"""
LeetCode Problem 196: Delete Duplicate Emails
Difficulty: Easy
Link: https://leetcode.com/problems/delete-duplicate-emails
"""


'''

delete from person where id not in (
    select MIN(id)
    from person
    group by email
)

# Keep only the email with the smallest id.
# Sql command

'''