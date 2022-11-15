# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_node(self,node, start, previous,k,orig_k,before_start,length,cur):
        if not node:
            return 
        if k == orig_k and  cur + orig_k > length:
            return
        nxt_node= node.next
        node.next = previous
        cur += 1
        
        if k == 1:
            start.next = nxt_node
            if before_start:
                before_start.next = node
                
            return self.reverse_node(nxt_node,nxt_node,None,orig_k,orig_k,start,length,cur)
        self.reverse_node(nxt_node,start,node,k-1,orig_k, before_start,length,cur)
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(val=0,next=head)
        self.reverse_node(head, head, dummy , k , k, dummy,length,0)
        
        return dummy.next
        