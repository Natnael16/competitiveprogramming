class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left , right = sys.maxsize ,sys.maxsize 
        
        for num in nums:
            left = min(left , num)
            if num > right:
                return True
            if num > left:
                right = min(num,right)
        
           