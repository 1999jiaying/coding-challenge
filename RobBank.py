"""
challenge: https://leetcode.com/problems/find-good-days-to-rob-the-bank/
question: You and a gang of thieves are planning on robbing a bank.
You are given a 0-indexed integer array security, where security[i] is the number of guards on duty on the ith day.
The days are numbered starting from 0. You are also given an integer time.
The ith day is a good day to rob the bank if:
    There are at least time days before and after the ith day,
    The number of guards at the bank for the time days before i are non-increasing, and
    The number of guards at the bank for the time days after i are non-decreasing.
idea: use Prefix Sum.
"""
# solution
def goodDaysToRobBank(security, time):
    """
    :type security: List[int]
    :type time: int
    :rtype: List[int]
    """

    l = len(security)
    pre = [0] * l
    nex = [0] * l
    ans = []

    for i in range(1, l):
        if security[i - 1] >= security[i]:
            pre[i] = pre[i - 1] + 1
    for i in range(l - 2, -1, -1):
        if security[i] <= security[i + 1]:
            nex[i] = nex[i + 1] + 1

    for i in range(l):
        if nex[i] >= time and pre[i] >= time:
            ans.append(i)

    return ans

# test
def test_answer():
    assert goodDaysToRobBank([1,1,1,1,1], 0) == [0,1,2,3,4]
    assert goodDaysToRobBank([1,2,3,4,5,6], 2) == []
    assert goodDaysToRobBank([5,3,3,3,5,6,2], 2) == [2,3]
