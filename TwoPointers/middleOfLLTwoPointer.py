import math
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node1 = head
        node2 = head
        if not node2 or not node2.next:
            return node2
        if not node2.next.next:
            return node2.next
        while node2.next:
            node1 = node1.next
            node2 = node2.next.next
            if not node2:
                break
        return node1