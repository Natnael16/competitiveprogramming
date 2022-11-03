class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def backtrack(ind, path):
            if ind > len(nums):
                return
            self.ans.append(path[:])
            for i in range(ind+ 1 , len(nums)):
                path.append(nums[i])
                backtrack(i,path)
                path.pop()
        backtrack(-1,[])
        return self.ans