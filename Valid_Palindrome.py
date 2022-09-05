"""
challenge:
    https://leetcode.com/problems/valid-palindrome/
question:
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
    and removing all non-alphanumeric characters, it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.
idea:
    Use two pointers.
"""


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    def alphaNum(c):
        return ((ord('A') <= ord(c) <= ord('Z'))
                or (ord('a') <= ord(c) <= ord('z'))
                or (ord('0') <= ord(c) <= ord('9')))

    a = 0  # left pointer
    b = len(s) - 1  # right pointer

    while a < b:
        while a < b and not alphaNum(s[a]):
            a += 1
        while a < b and not alphaNum(s[b]):
            b -= 1
        if s[a].lower() != s[b].lower():
            return False
        a, b = a + 1, b - 1

    return True


def test_answer():
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False
    assert isPalindrome(" ") == True
