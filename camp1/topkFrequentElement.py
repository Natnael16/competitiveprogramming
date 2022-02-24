import heapq


class NumberCount:

    def __init__(self, num, count):
        self.num = num
        self.count = count

    def __lt__(self, other):
        if other.count > self.count:
            return True
        else:
            return False


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = Counter(nums)
        for num, count in counter.items():
            heapq.heappush(heap, NumberCount(num=num, count=count))
        heap = heapq.nlargest(k, heap, key=lambda a: a.count)
        for i in range(len(heap)):
            heap[i] = heap[i].num
        return heap