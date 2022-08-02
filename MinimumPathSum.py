"""
challenge: https://leetcode.com/problems/minimum-path-sum/
question: Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
idea: use dynamic programming. d[i,j] = min(d[i-1][j], d[i][j-1]) + grid[i][j]
"""
import numpy

# solution
def minPathSum(grid):
    # create an array to store the minimum sum at each point
    row = len(grid)
    col = len(grid[0])
    distance = numpy.zeros((row, col))
    # initialize the distance
    distance[0][0] = grid[0][0]
    # use dymatic programming
    for i in range(0, row):
        for j in range(0, col):
            if j == 0 and i >= 1:
                distance[i][0] = distance[i - 1][0] + grid[i][0]
            if i == 0 and j >= 1:
                distance[0][j] = distance[0][j - 1] + grid[0][j]
            if i >= 1 and j >= 1:
                distance[i][j] = min(distance[i - 1][j], distance[i][j - 1]) + grid[i][j]

    return int(distance[row - 1][col - 1])

# test
def test_answer():
    assert minPathSum([[1,2,3],[4,5,6]]) == 12
    assert minPathSum([[1]]) == 1
    assert minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7
