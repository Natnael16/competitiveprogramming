# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        
        if lenA < lenB:
            headA , headB = headB, headA
        diff = abs(lenA - lenB)
        while diff and headA:
            headA = headA.next
            diff -= 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
        
        
        # reverse back
    def getLength(self,head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count