class Solution:

    def insertionSortList(self,
                          head: Optional[ListNode]) -> Optional[ListNode]:
        n = []
        count = 0
        while head:
            n.append(head.val)
            head = head.next
            count += 1

        for i in range(1, count):
            for j in range(i - 1, -1, -1):
                if n[j + 1] < n[j]:
                    temp = n[j + 1]
                    n[j + 1] = n[j]
                    n[j] = temp
        new = ListNode()
        ret = new
        for i in range(len(n)):
            new.val = n[i]
            if i == len(n) - 1:
                break
            new.next = ListNode()
            new = new.next
        return ret