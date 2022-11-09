class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:

        nums_len = len(nums)
        total = sum(nums)
        @cache
        def canSplit(index, sum1, length1):
            
            if length1 and nums_len - length1:
                if sum1/length1 == (total - sum1)/(nums_len - length1):
                    return True
            if index >= nums_len:
                return False
            
            return canSplit(index + 1, sum1 + nums[index], length1 + 1) or canSplit(index + 1, sum1,length1)
        
        #Prunning
        for i in range(1,nums_len):
            if not total * i % nums_len:
                return canSplit(0,0,0)
        return False
            
                
        