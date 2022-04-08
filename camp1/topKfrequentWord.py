import heapq
class Solution:

    def topKFrequent(self, words: List[int], k: int) -> List[int]:
        heap = []
        counter = Counter(words)
        for word, count in counter.items():
            heap.append((-count,word))
        # heap = heapq.nlargest(k, heap, key=lambda a: a.count)
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
