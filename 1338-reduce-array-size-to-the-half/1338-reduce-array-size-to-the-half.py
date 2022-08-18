
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        '''
            reserve the count of all 
            choose a number in step that max count first
            romove them and check if <= len(arr)/2
        '''
        counter = Counter(arr)
        heap = []
        # O(n)
        for num in counter:
            heappush(heap , (-counter[num] ,num ))

        tot = len(arr)
        count = 0
        #O(n)
        while True:
            freq , num = heappop(heap)
            count += 1
            tot -= (-freq)
            if tot <= len(arr)/2:
                break
        return count
            
        