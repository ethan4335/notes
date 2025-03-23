# Definition for singly-linked list.
from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        s,b = ListNode(0),ListNode(0)
        while head:
            if head.val < x:
                s.next = head
                s = s.next
            else:
                b.next = head
                b = b.next
            head = head.next
        s.next = b.next
        b.next = None
        return s.next

res = Solution().partition([1,4,3,2,5,2],3)