class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        total_subarrays = 0
        running_sum = 0
        for num in nums:
            
            running_sum += num
            prefix_needed = running_sum - k
            if prefix_needed in prefix_sum:
                total_subarrays += prefix_sum[prefix_needed]
            prefix_sum[running_sum] += 1
            
        return total_subarrays
    
                
         
        
         
         
         
        
        
        