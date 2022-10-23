class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        counter = Counter(nums)
        dup,missing = -1,-1
        for num in range(1,n+1):
            if counter[num] == 2:
                dup = num
            if counter[num] == 0:
                missing = num
        return [dup,missing]
            
        
        