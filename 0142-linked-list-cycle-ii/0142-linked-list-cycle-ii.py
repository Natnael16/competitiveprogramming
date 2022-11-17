# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def meetsAt(self,node):
        hare, tortoise = node, node
        
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return hare
            
        return None
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        meetPos = self.meetsAt(head)
        if not meetPos:
            return None
        tortoise, hare = head , meetPos
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
        return hare
        
            