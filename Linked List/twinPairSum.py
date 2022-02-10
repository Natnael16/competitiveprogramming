import copy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head):
    #     previous = None
    #     node = copy.deepcopy(head)
    #     leng = 0
    #     while node != None:
    #         nextNode = node.next
    #         node.next = previous
    #         previous = node
    #         node = nextNode
    #         leng += 1
    #     return [previous,leng]
    def pairSum(self, head: Optional[ListNode]) -> int:
        previous = None
        node = copy.deepcopy(head)
        leng = 0
        while node != None:
            nextNode = node.next
            node.next = previous
            previous = node
            node = nextNode
            leng += 1
        count = 0
        msum = 0
        rev = [previous,leng]
        rev_node = rev[0]
        
        while count < rev[1]//2:
            if rev_node.val + head.val > msum:
                msum = rev_node.val + head.val
            head = head.next
            rev_node = rev_node.next
            count += 1
        return msum