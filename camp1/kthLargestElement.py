#heap Solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        largestArr = heapq.nlargest(k,nums)
        return largestArr[-1]
