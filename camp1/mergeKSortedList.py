class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in lists:
            while i:
                heap.append(i.val)
                i = i.next
        heapq.heapify(heap)
        if len(heap) == 0:
            return None
        new = ListNode()
        res = new
        while heap:
            new.val = heapq.heappop(heap)
            if len(heap) == 0:
                break
            new.next = ListNode()
            new = new.next
        return res
            
