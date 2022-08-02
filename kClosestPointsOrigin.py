"""
challenge: https://leetcode.com/problems/k-closest-points-to-origin/
question: Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).The distance between two points on the X-Y plane
is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
idea: calculate the distance and then sort.
"""
import math


def kClosest(points, k):
    """
    :type points: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    distance = lambda x, y: math.sqrt(x ** 2 + y ** 2)
    point_distance = [([x, y], distance(x, y)) for x, y in points]
    point_distance.sort(key=lambda delta: delta[1])
    ans = [i[0] for i in point_distance[:k]]

    return ans


def test_answer():
    assert kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
    assert kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
