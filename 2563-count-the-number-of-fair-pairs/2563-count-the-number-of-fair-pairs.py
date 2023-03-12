class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        answer = 0
        l = r = len(nums) - 1
        for index in range(len(nums)):
            #for index = 5
            #l_num = -3, r_num = -1
            #l = -1
            #r = -1
            
            
            # answer = 12
            l_num = lower - nums[index]
            r_num = upper - nums[index]
            while nums[l] >= l_num and l >= 0:
                l -= 1
            
            while nums[r] > r_num and r > l:
                r -= 1
         
            if r == -1:
                break
            
            answer += r - l
            if l < index <= r:
                answer -= 1
        
        
        return answer // 2