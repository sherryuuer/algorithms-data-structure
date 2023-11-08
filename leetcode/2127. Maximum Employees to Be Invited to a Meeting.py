# A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.

# The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

# Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

# Input: favorite = [3,0,1,4,1]
#                    0,1,2,3,4
# Output: 4

# [2,2,1,2]
#  0,1,2,3

# 深度优先搜索
# 内向基环树 + 拓扑排序