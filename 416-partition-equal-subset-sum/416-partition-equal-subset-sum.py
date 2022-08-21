class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return 
        
        tar = sum(nums)//2
        canSum = {0}
        for num in nums:
            temp = set()
            for tot in canSum:
                temp.add(tot + num)
                temp.add(tot)
            canSum = canSum.union(temp)
        if tar in canSum: return True