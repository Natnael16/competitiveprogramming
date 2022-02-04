class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        solved = self.swapPairs(head.next.next)
        new = head.next
        head.next = solved
        new.next = head
        return new