class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #        1 2 3
        #    1 
        #   12 13  because 1 is already in path
        # 123  132
        self.ans = []
        
        def backtrack(path):
            if len(path) == len(nums):
                self.ans.append(list(path))
                return
            
            for i in nums:
                if i not in path:
                    path.append(i)
                    backtrack(path)
                    path.pop()
        backtrack([])
        return self.ans
        