"""
challenge:
    https://leetcode.com/problems/top-k-frequent-elements/
question:
    Given an integer array nums and an integer k, return the k most frequent elements.
    You may return the answer in any order.
idea:
    use counts as an index. O(n)
"""
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    freq = [[] for i in range(len(nums))]
    count = {}
    res = []

    for i in nums:
        count[i] = 1 + count.get(i, 0)
    for i in count:
        freq[count[i] - 1].append(i)

    for i in range(len(freq) - 1, -1, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

def test_answer():
    assert topKFrequent([1,1,1,2,2,3], 2) == [1,2]
    assert topKFrequent([1], 1) == [1]