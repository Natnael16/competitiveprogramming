class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for c in count:
            if count[c] > len(nums)//2:
                return c
        
                