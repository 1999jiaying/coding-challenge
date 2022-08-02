"""
challenge:
    https://leetcode.com/problems/contains-duplicate/
question:
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
idea:
    use a set. Time: O(n)
"""


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    s = set()
    for i in nums:
        if i in s:
            return True
        else:
            s.add(i)
    return False


# test
def test_answer():
    assert containsDuplicate([1, 2, 3, 1]) == True
    assert containsDuplicate([1, 2, 3, 4]) == False
    assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
