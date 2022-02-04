# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        node = head
        
        while node != None:
            nextNode = node.next
            node.next = previous
            previous = node
            node = nextNode
        return previous
        
        