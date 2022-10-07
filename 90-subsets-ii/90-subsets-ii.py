class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #[1,2,2]
        #|
        nums.sort()
        self.ans = set()
        self.ans.add(())
        def backtrack(ind,path):
            if len(path) == len(nums):
                self.ans.add(tuple(path))
                return
            for i in range(ind, len(nums)):
                path.append(nums[i])
                self.ans.add(tuple(path))
                backtrack(i + 1,path)
                path.pop()
                
        backtrack(0,[])
        
        return self.ans
                
        