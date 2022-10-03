class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.n = len(candidates)
        candidates.sort()
        
        def dp(ind , tar , path):
            if tar==0:
                return [copy.deepcopy(path)]
            if tar < 0:
                return []
            recur_results = []
            
            for i in range(ind + 1 , self.n):
                if i > ind + 1 and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                res = dp(i , tar - candidates[i],path)
                for r in res:
                    if r:
                        recur_results.append(r)
                path.pop()
            return recur_results
        return dp(-1,target,[])
        # 1,1,2,5,6,7,10  8
          