
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        rtn = head
        count = 0
        while temp:
            count +=1
            temp = temp.next
        nth = count - (n-1)
        if count == 1:
            return None
        count2 = 0
        new = ListNode()
        new.next = head
        if nth ==1:
            return head.next
        while new:
            if count2 == nth - 1:
                new.next = new.next.next
            count2 += 1
            new = new.next
        return rtn