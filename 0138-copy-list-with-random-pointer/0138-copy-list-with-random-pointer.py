"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        identicals = {None: None}
        cur_node = head
        while cur_node:
            identicals[cur_node] = Node(cur_node.val)
            cur_node = cur_node.next
        
        cur_node = head
        while cur_node:
            identicals[cur_node].next = identicals[cur_node.next]
            identicals[cur_node].random = identicals[cur_node.random]
            cur_node = cur_node.next
        
        return identicals[head]