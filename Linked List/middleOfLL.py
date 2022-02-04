class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp= head
        while(temp != None):
            count += 1
            temp = temp.next
        value = count // 2 - 1
        it = 0
        if count==1:
            return head
        while(head != None):
            if it == value:
                return head.next
            head = head.next
            it += 1S