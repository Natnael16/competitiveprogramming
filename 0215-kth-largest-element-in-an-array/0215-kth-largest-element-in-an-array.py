class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n = len(nums) - k
        while n + 1:
            val = heappop(nums)
            n -= 1 
        return val