"""
challenge: https://leetcode.com/problems/maximum-subarray/
question: Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum. A subarray is a contiguous part of an array.
idea: if prefix sum < 0, we remove the prefix array.
"""


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxsum = nums[0]
    presum = 0
    for i in nums:
        if presum < 0:
            presum = 0
        maxsum = max(maxsum, presum + i)
        presum += i
    return maxsum

# test
def test_answer():
    assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert maxSubArray([1]) == 1
    assert maxSubArray([5,4,-1,7,8]) == 23
