# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow , fast = head , head
        prev = None
        while slow and fast:
            if fast.next:
                fast = fast.next.next
            else:
                break
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return head