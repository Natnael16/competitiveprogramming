# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        save = new_node
        while list1 and list2:
            if list1 == None:
                new_node.next = list2
        
            elif list2 == None:
                new_node.next = list1
        
            if list1.val <= list2.val:
                new_node.next = list1
                list1 = list1.next
            elif list2.val <= list1.val:
                new_node.next = list2
                list2 = list2.next
            print("l1",list1,"li2",list2)
            new_node = new_node.next
        if list1:
            new_node.next = list1
        if list2:
            new_node.next = list2
        return save.next