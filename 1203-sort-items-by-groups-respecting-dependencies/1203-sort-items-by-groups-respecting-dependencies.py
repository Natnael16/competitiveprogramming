class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * n
        change = 0
        group_list = defaultdict(list)
        group_dependency = defaultdict(list)
        group_indegree = {}
        for g in range(len(group)):
            if group[g] == -1:
                group[g] -= change
                change += 1
        
        for i in group:
            group_indegree[i] = 0
        for i in range(n):
            for before in beforeItems[i]:
                graph[before].append(i)
                if group[before] != group[i]:
                    group_dependency[group[before]].append(group[i])
                    if group[i] in group_indegree:
                        group_indegree[group[i]] += 1
                indegree[i] += 1
        
        q = deque([])
        for ind, count in enumerate(indegree):
            if count == 0:
                q.append((group[ind],ind))
        while q:
            cat , node = q.popleft()
            group_list[cat].append(node)
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append((group[neigh],neigh))
                    
        queue = deque([])
        ans = []
        for deg in group_indegree:
            if group_indegree[deg] == 0:
                queue.append(deg)
        
        while queue:
            cur_group = queue.popleft()
            ans.extend(group_list[cur_group])
            for child in group_dependency[cur_group]:
                group_indegree[child] -= 1
                if group_indegree[child] == 0:
                    queue.append(child)
        if len(ans) != n: return []
        return ans
            
        
        
                    
            
            
            
            