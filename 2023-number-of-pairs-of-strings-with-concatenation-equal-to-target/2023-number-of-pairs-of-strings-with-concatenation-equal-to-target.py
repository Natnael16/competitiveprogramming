class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        count = 0 
        for i in range(n):
            a = nums[i]
            for j in range(i+1,n):
                b = nums[j]
                if a+b == target:
                    count += 1
                if b+a == target:
                    count += 1
        return count