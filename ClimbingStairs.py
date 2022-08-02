"""
challenge: https://leetcode.com/problems/climbing-stairs/submissions/
question: You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
idea: ways of current stair = ways of (current stair - 1) + ways of (current stair - 2)
"""

def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    # create a list to store ways of stair i
    way = [0] * (n + 1)
    way[1] = 1
    way[2] = 2
    for i in range(3, n + 1):
        way[i] = way[i - 1] + way[i - 2]

    return way[n]


def test_answer():
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3