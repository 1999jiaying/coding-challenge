"""
created: 5/23/2022
challenge: https://leetcode.com/problems/merge-intervals/
This question requires us to merge intervals.
First, I sorted the list using the x[0] for each interval x. Then I created a new list
to store the merged intervals and used a loop to compare.
"""

def merge(intervals):
    mergedInterval = []
    intervals = sorted(intervals, key=lambda x: x[0])
    newInterval = intervals.pop(0)
    for i in intervals:
        if i[0] <= newInterval[1]:
            newInterval = [min(newInterval[0], i[0]), max(newInterval[1], i[1])]
        else:
            mergedInterval.append(newInterval)
            newInterval = i
    mergedInterval.append(newInterval)
    return mergedInterval

#tests log
def test_answer():
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[4,5]]) == [[1,5]]
    assert merge([[1,2],[1,2]]) == [[1,2]]
