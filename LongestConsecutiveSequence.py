"""
challenge:
    https://leetcode.com/problems/longest-consecutive-sequence/
question:
    Given an unsorted array of integers nums, return the length of the longest
    consecutive elements sequence. You must write an algorithm that runs in O(n) time.
idea:
    The element is the start point of a sequence if its left neighbor is not in the set. then see if
    its right neighbor is in the set, if so length + 1.
"""


def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s = set(nums)  # create a set to see the neighbors
    longest = 0
    for i in nums:
        if i - 1 not in s:
            length = 1
            while i + length in s:
                length += 1
            longest = max(longest, length)
    return longest

def test_answer():
    assert longestConsecutive([100,4,200,1,3,2]) == 4
    assert longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9