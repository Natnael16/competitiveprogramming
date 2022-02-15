class Solution:

    def merge(self, l1, l2):
        merged = []
        first, second = 0, 0
        while first < len(l1) and second < len(l2):
            if l1[first] > l2[second]:
                merged.append(l2[second])
                second += 1
            else:
                merged.append(l1[first])
                first += 1
        if first == len(l1):
            merged += l2[second:]
        else:
            merged += l1[first:]
        return merged

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ex = []
        if not head or not head.next:
            return head
        while head:
            ex.append(head.val)
            head = head.next

        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            return self.merge(mergeSort(arr[:len(arr) // 2]),
                              mergeSort(arr[len(arr) // 2:]))

        arranged = mergeSort(ex)
        ret = ListNode()
        final = ret
        for i in range(len(arranged)):
            ret.val = arranged[i]
            if i == len(arranged) - 1:
                break
            ret.next = ListNode()
            ret = ret.next
        return final