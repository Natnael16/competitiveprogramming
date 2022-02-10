import copy
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        previous = None
        node = copy.deepcopy(head)
        
        while node != None:
            nextNode = node.next
            node.next = previous
            previous = node
            node = nextNode
        return previous
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        new = ListNode()
        reference = new
        node_1 = head
        node_2 = self.reverseList(head)
        leng = 0
        temp = head
        while temp:
            leng += 1
            temp = temp.next

        def helper(node1,node2,turn,count,new):
            if count == leng:
                return reference
            else:
                if turn == 0:
                    new.next = ListNode(node1.val)
                    new = new.next
                    node1 = node1.next
                    print(new,node1,"0th",reference)
                else:
                    new.next = ListNode(node2.val)
                    new = new.next
                    node2 = node2.next
                    print(new,node2,"1th",reference)
            return helper(node1,node2,1-turn,count+1,new)
        ret = helper(node_1,node_2,0,0,new)
        print(ret.next,"this")
        head= ret.next
        print(head)
        return ret.next
# not efficient in terms of space