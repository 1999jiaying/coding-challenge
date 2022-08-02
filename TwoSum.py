"""
challenge:
    https://leetcode.com/problems/two-sum/
question:
    Given an array of integers nums and an integer target, return indices of the two numbers such that
    they add up to target. You may assume that each input would have exactly one solution, and you
    may not use the same element twice. You can return the answer in any order.
idea:
    Create a hashmap for value and index. O(n)
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indexdict = dict()

    for i, value in enumerate(nums):
        diff = target - value
        if diff in indexdict:
            return [i, indexdict[diff]]
        indexdict[value] = i
    return None

# test
def test_answer():
    assert twoSum([2,7,11,15], 9) == [0,1] or twoSum([2,7,11,15], 9) == [1,0]
    assert twoSum([3,2,4], 6) == [1,2] or twoSum([3,2,4], 6) == [2,1]
    assert twoSum([3,3], 6) == [0, 1] or twoSum([3,3], 6) == [1, 0]

