"""
date:20220527
challenge: https://leetcode.com/problems/reverse-linked-list/
question: given the head of a singly linked list, reverse the list, and return the reversed list.
idea: use a loop and swap each node's prev and next
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# solution
def reverseList(head):
    pre = None
    p = head
    while p:
        # swap each node's previous and next
        nex = p.next
        p.next = pre
        pre = p
        p = nex
    head = pre
    return head


# tests log

# given a head node, return the node list
def nodelist(node):
    nl = []
    h = node
    while h:
        nl.append(h)
        h = h.next
    return nl


# test case 1: create a node list
Node_3 = ListNode(3)
Node_2 = ListNode(2, Node_3)
Node_1 = ListNode(1, Node_2)

# test case 2: create a node list with single node
Node_4 = ListNode(2)


def test_answer():
    assert nodelist(reverseList(Node_1)) == [Node_3, Node_2, Node_1]
    assert nodelist(reverseList(Node_4)) == [Node_4]
