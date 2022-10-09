class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #a    b   c 
        #
        #a : (b , 1.5)
        #b : (a  , 2/3) (c , 0.5)
        #c : (b , 2)
        graph = defaultdict(list)
        
        for ind, equation in enumerate(equations):
            num , denom = equation
            graph[num].append((denom,values[ind]))
            graph[denom].append((num,1/values[ind]))
        output = []
        for num ,denom in queries:
            
            if num not in graph or denom not in graph:
                output.append(-1)
                continue
            visited = set()
            q = deque([(num , 1)])
            found = False
            while q:
                cur , value = q.popleft()
                visited.add(cur)
                if cur == denom:
                    output.append(value)
                    found = True
                    break
                for neigh , val in graph[cur]:
                    if neigh not in visited:
                        q.append((neigh, val * value))
            
            if not found: output.append(-1)
        return output