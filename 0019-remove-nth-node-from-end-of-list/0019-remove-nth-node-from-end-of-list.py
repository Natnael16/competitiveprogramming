# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        cur_node = head
        slow ,fast = head, head
        difference = 1
        
        while fast.next != None:
            if difference != n:
                fast = fast.next
                difference += 1
            else:  
                fast = fast.next
                prev = slow
                slow = slow.next
        
        prev.next = slow.next
        
        return dummy.next
            
            
            
        
            