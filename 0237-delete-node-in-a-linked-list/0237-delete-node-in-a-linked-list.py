# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        def delete(node):
            if not node.next.next:
                node_val= node.val
                node.val = node.next.val
                node.next = None
                return node_val
            next_val = delete(node.next)
            node_val= node.val
            node.val = next_val
            return node_val
        delete(node)
        
            
        