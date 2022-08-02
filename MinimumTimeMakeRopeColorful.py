"""
challenge:
    https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
question:
    Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the
    color of the ith balloon. Alice wants the rope to be colorful. She does not want two consecutive balloons to be
    of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful.
    You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that
    Bob needs to remove the ith balloon from the rope.
    Return the minimum time Bob needs to make the rope colorful.
idea:
    only keep the element with the largest time in a consecutive string with the same color
"""


def minCost(colors, neededTime):
    """
    :type colors: str
    :type neededTime: List[int]
    :rtype: int
    """
    i = 0
    j = 1
    t = 0
    while i < len(colors) - 1:
        sumtime = neededTime[i]
        maxtime = neededTime[i]
        while colors[i] == colors[j]:
            sumtime += neededTime[j]
            maxtime = max(neededTime[j], maxtime)
            j += 1
            if j >= len(colors):
                break
        i = j
        j += 1
        t += sumtime - maxtime

    return t

# test
def test_answer():
    assert minCost("abaac", [1,2,3,4,5]) == 3
    assert minCost("abc", [1, 2, 3]) == 0
    assert minCost("aabaa", [1,2,3,4,1]) == 2

