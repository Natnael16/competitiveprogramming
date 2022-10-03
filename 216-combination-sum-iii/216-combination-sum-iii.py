class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        len_n = len(nums)
        def dfs(ind,tar,path):
            if ind > len_n or len(path) >= k:
                if tar == 0 and len(path) == k:
                    return [list(path)]
                return []
            rec_res = []
            for i in range(ind + 1,len_n):
                path.append(nums[i])
                res = dfs(i,tar - nums[i], path)
                path.pop()
                
                for r in res:
                    if r:
                        rec_res.append(r)
            return rec_res
        return dfs(-1,n,[] )
            