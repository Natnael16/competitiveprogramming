class WordFrequency:
    def __init__(self,word,count):
        self.word = word
        self.count = count
    def __lt__(self,other):
        if self.count > other.count:
            return True
        else:
            return False
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        heap = []

        for char,count in counter.items():
            heapq.heappush(heap,WordFrequency(word = char, count = count))
        string = ""
        while heap:
            res = heapq.heappop(heap)
            string += res.word * res.count
        return string
        