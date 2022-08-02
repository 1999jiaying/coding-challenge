"""
challenge:
    https://leetcode.com/problems/product-of-array-except-self/
question:
    Given an integer array nums, return an array answer such that answer[i] is equal to the
    product of all the elements of nums except nums[i]. The product of any prefix or suffix
    of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs
    in O(n) time and without using the division operation.
idea:
    In the first round, every element will multiply the prefix product.
    In the second round, every element will multiply the postfix product.
"""

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = [1] * len(nums)
    prefix = 1
    postfix = 1

    for i in range(len(nums)):
        ans[i] *= prefix
        prefix *= nums[i]
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= postfix
        postfix *= nums[i]

    return ans

def test_answer():
    assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]