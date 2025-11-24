"""
LeetCode Problem 182: Duplicate Emails
Difficulty: Easy
Link: https://leetcode.com/problems/duplicate-emails
"""


'''

select email
from person
group by email
having count(*) > 1;


# select emails that appear more than once by grouping them
and filtering groups with a count greater than 1  

# Sql command

'''