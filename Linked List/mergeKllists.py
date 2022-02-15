class Solution:

    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i in lists:
            while i:
                arr.append(i.val)
                i = i.next
        if len(arr) == 0:
            return None
        new = ListNode()
        res = new
        arr.sort()
        for i in range(len(arr)):
            new.val = arr[i]
            if i == len(arr) - 1:
                break
            new.next = ListNode()
            new = new.next
        return res