"""
challenge:
    https://leetcode.com/problems/group-anagrams/
question:
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
idea:
    Create a hashmap for each string. O(m*n)
"""
from collections import defaultdict

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagramdict = defaultdict(list)
    for i in strs:
        maps = [0] * 26
        for j in i:
            maps[ord(j) - ord('a')] += 1
        anagramdict[tuple(maps)].append(i)
    return list(anagramdict.values())


# test
def test_answer():
    assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"], ["tan", "nat"], ["bat"]]
    assert groupAnagrams([""]) == [[""]]