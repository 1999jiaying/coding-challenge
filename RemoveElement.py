"""
challenge: https://leetcode.com/problems/remove-element/
This question requires us to remove all items with value=val in array nums.
For the third solution, I used pointers and a temp variable.
"""

def removeElement(nums, val):
    a = 0  # pointer b
    b = 0  # pointer b
    while a < len(nums):
        if nums[a] != val:
            temp = nums[a]
            nums[b] = temp
            b += 1
        a += 1
    return b


#tests log
def test_answer():
    assert removeElement([3,2,2,3],3) == 2
    assert removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert removeElement([3, 2, 4, 2, 3], 3) == 3

    print('PASS')
