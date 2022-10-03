class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''[2,3,6,7] 7
    
                                0 , 7
                            (0,5 , [2]) (1,4) (2, 1) (3,0) 
        '''
        self.n = len(candidates)
        # memo = {}
        def dp(ind , tar , path):
            # if (ind,tar) in memo: return memo[(ind,tar)]
            if tar==0:
                return [copy.deepcopy(path)]
            if tar < 0:
                return []
            recur_results = []
            for i in range(ind,self.n):
                path.append(candidates[i])
                res = dp(i , tar - candidates[i],path)
                for r in res:
                    if r:
                        recur_results.append(r)
                path.pop()
            return recur_results
        return dp(0,target,[])
        
            