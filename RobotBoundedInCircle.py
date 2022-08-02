"""
challenge:
    https://leetcode.com/problems/robot-bounded-in-circle/
question:
    On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
        The north direction is the positive direction of the y-axis.
        The south direction is the negative direction of the y-axis.
        The east direction is the positive direction of the x-axis.
        The west direction is the negative direction of the x-axis.
    The robot can receive one of three instructions:
        "G": go straight 1 unit.
        "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
        "R": turn 90 degrees to the right (i.e., clockwise direction).
        The robot performs the instructions given in order, and repeats them forever.

    Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
idea:
    For this question, we need to look at the last step. If the final direction is not north, after 4 rounds, we can go
    back to the (0,0). Else: If we arrive (0,0), it is also ok. But if we are not at (0,0), then it won't be in a circle.
"""


def isRobotBounded(instructions):
    """
    :type instructions: str
    :rtype: bool
    """
    p = [0, 0]
    d = 0
    direction = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
    for i in instructions:
        if i == 'L':
            d = (d + 3) % 4
        if i == 'R':
            d = (d + 1) % 4
        if i == 'G':
            p = [p[0] + direction[d][0], p[1] + direction[d][1]]
    if d == 0:
        if p[0] == 0 and p[1] == 0:
            return True
        else:
            return False
    else:
        return True

# test
def test_answer():
    assert isRobotBounded("GGLLGG") == True
    assert isRobotBounded("GG") == False
    assert isRobotBounded("GL") == True

