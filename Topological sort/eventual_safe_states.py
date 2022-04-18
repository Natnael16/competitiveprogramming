class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        result = []
        memo = {}
        
        def dfs(ind):
            if not graph[ind]:
                self.bools.append(True)
                memo[ind] = True
                return memo[ind]
            if ind in memo:
                self.bools.append(memo[ind])
                return memo[ind]
            self.visited.add(ind) 
            truth = True
            for neigh in graph[ind]:
                if neigh in self.visited and neigh not in memo:
                    # print(ind , neigh)
                    self.bools.append(False)
                    truth = False
                    memo[ind] = False
                    return memo[ind]
                if neigh in memo:
                    self.bools.append(memo[neigh])
                    truth = truth and memo[neigh]
                else:
                    t = dfs(neigh)
                    truth = truth and t
                    self.bools.append(t)
                    
            memo[ind] = truth
            return memo[ind]
        for node in range(len(graph)):
            self.visited = set()
            self.bools = []
            dfs(node)
            if not (False in self.bools):
                result.append(node)
         
        # print(memo)
        return result
