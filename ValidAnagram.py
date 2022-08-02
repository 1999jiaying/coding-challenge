"""
challenge:
    https://leetcode.com/problems/valid-anagram/
question:
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
idea:
    use a Counter. O(n)/O(S+T)
"""


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    '''
    a = Counter(s)
    b = Counter(t)

    return a == b
    '''

    '''
    return sorted(s) == sorted(t)
    '''
    if len(s) != len(t):
        return False
    countS = {}
    countT = {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for i in countS:
        if countS[i] != countT.get(i, 0):
            return False
    return True

# test
def test_answer():
    assert isAnagram("anagram", "nagaram") == True
    assert isAnagram("rat", "car") == False
