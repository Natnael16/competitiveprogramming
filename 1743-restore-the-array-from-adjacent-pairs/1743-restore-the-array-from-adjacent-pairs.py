class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        count = Counter()
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            count[u] += 1
            count[v] += 1
        path = []
        seen = set()
        for c in count:
            if count[c] == 1:
                seen.add(c)
                break
        num_count = len(count)
        while num_count:
            path.append(c)
            for child in graph[c]:
                if child != c and child not in seen:
                    c = child
                    seen.add(c)
            num_count -= 1
        return path


        
        


        

          