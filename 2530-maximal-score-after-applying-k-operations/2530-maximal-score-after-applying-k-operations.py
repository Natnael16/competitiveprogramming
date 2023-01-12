class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for index , num in enumerate(nums):
            heappush(heap, (-num,index))
        
        score = 0
        while k > 0:
            value, index = heappop(heap)
            value = -value
            score += (value)
            heappush(heap , (-(math.ceil(value/3)), index))
            k -= 1
        
        return score