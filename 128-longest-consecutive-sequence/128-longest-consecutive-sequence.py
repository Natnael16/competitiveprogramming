class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #{100,4,200,1,3,2}
        #1 ,2 ,3, 4
        #
        #100 : 1 + dfs(100 + 1)
        #4 : 1 + dfs(5) 0
        #1 : 1 + dfs(2) (1  + dfs(3) ( 1 + dfs(4))
        #3 : 2
#         nums_set = set(nums)
        
#         cons_count = defaultdict(int)
#         self.maxi = 0
#         def dfs(num):
#             if num not in nums_set: return 0
#             if num in cons_count: return cons_count[num]
#             cons_count[num] = 1 + dfs(num + 1)
#             self.maxi = max(self.maxi , cons_count[num])
#             return cons_count[num]
#         for num in nums_set:
#             dfs(num)
#         return self.maxi
        nums_set = set(nums)
        maxi = 0
        for num in nums_set:
            if num - 1 in nums_set: continue
                
            count = 1
            target = num + 1
            while target in nums_set:
                count += 1
                target += 1
            if count > maxi:
                maxi = count
            
        return maxi
            
            
            
            
            
    
    
        