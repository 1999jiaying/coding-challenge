"""
challenge: https://leetcode.com/problems/longest-continuous-increasing-subsequence/
question: Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray).
The subsequence must be strictly increasing.
idea: use two variables, one is for the latest increasing subsequence, one is for the longest by now.
"""

# solution
def findLengthOfLCIS(nums):
    # max_length is the longest length by now
    # temp is the length of the latest increasing subsequence
    max_length = 1
    temp = 1

    for i in range(1, len(nums)):

        if nums[i] > nums[i - 1]:
            temp += 1
        else:
            max_length = max(max_length, temp)
            temp = 1
    max_length = max(max_length, temp)

    return max_length

# test
def test_answer():
    assert findLengthOfLCIS([1,3,5,4,7]) == 3
    assert findLengthOfLCIS([2,2,2,2,2]) == 1
