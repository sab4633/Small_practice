"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def getVal(lln, s) -> str:
    while not lln == None:
        s = str(lln.val) + s
        lln = lln.next
    return s


def toListNode(num) -> ListNode:
    s = str(num)
    # print(s)
    lln = ListNode()
    temp = lln
    for i in range(1, len(s) + 1):
        # print(s[-i])
        temp.val = int(s[-i])
        # print(temp.val)
        temp.next = ListNode()
        if i < len(s):
            temp = temp.next
        else:
            temp.next = None
    return lln


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = int(getVal(l1, "")) + int(getVal(l2, ""))
        # print(sum)
        return toListNode(sum)

