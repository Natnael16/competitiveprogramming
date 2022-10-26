class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        The key is calculating the prifix sum and recording their remainder, if reaminder is repeated we know we have multiple of k some where.
        """
        remainder = {0 : -1} 
        psum = 0
        for ind in range(len(nums)):
            psum += nums[ind]
            modRes = psum % k
            if modRes in remainder:
                if ind - remainder[modRes] > 1: return True
            else:
                remainder[modRes] = ind 
        return False
        