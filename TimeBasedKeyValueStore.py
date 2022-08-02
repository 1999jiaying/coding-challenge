"""
challenge: https://leetcode.com/problems/time-based-key-value-store/submissions/
question: Design a time-based key-value data structure that can store multiple values for the same key at
different time stamps and retrieve the key's value at a certain timestamp.
Implement the TimeMap class:
    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously,
    with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with
    the largest timestamp_prev. If there are no values, it returns "".
idea: we can just follow the requirement to build a class, but I found there is a time limit. I tried using sort function
with nested dict but failed. Then I followed the binary search solution.
"""

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key, value, timestamp):
        self.hashMap[key].append([timestamp, value])

    def get(self, key, timestamp):
        if key in self.hashMap:
            values = self.hashMap[key]
            prev_value = ""
            left_ptr, right_ptr = 0, len(values) - 1
            while left_ptr <= right_ptr:
                mid = (left_ptr + right_ptr) // 2
                if values[mid][0] == timestamp:
                    return values[mid][1]
                if values[mid][0] < timestamp:
                    prev_value = values[mid][1]
                    left_ptr = mid + 1
                elif values[mid][0] > timestamp:
                    right_ptr = mid - 1
            return prev_value

        return ""


def opr(map, operations, values):
    ans = []
    for i in range(len(operations)):
        if operations[i] == 'set':
            ans.append(map.set(values[i][0], values[i][1], values[i][2]))
        else:
            ans.append(map.get(values[i][0], values[i][1]))
    return ans


# test
def test_answer():
    a = TimeMap()
    assert opr(a, ["set", "get", "get", "set", "get", "get"],
               [["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4],
                ["foo", 4], ["foo", 5]]) == [None, "bar", "bar", None, "bar2", "bar2"]
