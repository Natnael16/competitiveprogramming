class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
    #     [1]  [17]  [8]
    # [1,8]   [8]
        n = len(nums)
        nums = Counter(nums)
        self.count = 0
        def backtrack(path):
            if len(path) == n:
                self.count += 1
                return 
            
            for cur_index, num in enumerate(nums):
                if  nums[num] > 0:
                    if not path or isPerfect(path[-1] + num):
                        path.append(num)
                        nums[num] -= 1
                        backtrack(path)
                        nums[num] += 1
                        path.pop()
        
                        
        def isPerfect(num):
            root = sqrt(num)
            if root == int(root):
                return True
            return False
        backtrack([])
        return self.count
                    
                    
    