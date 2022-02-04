class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        node = l1
        while node != None:
            nextNode = node.next
            node.next = previous
            previous = node
            node = nextNode
            
        previous2 = None
        node = l2
        while node != None:
            nextNode = node.next
            node.next = previous2
            previous2 = node
            node = nextNode
        # print(previous,previous2)
        s1 = ""
        s2 = ""
        while previous:
            s1 += str(previous.val)
            previous = previous.next
        while previous2:
            s2 += str(previous2.val)
            previous2 = previous2.next
        val = int(s1) + int(s2)
        ret = [int(i) for i in str(val)]
        # ret = ret [::-1]
        last = None
    
        for i in ret:
            new = ListNode(0)
            new.val = i
            new.next = last
            last = new
        return new