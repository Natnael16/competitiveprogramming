class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #    2      3
        #  a - >  b  - > c
        #   1/2      1/3

        #   a/b = 2
        #   c/b = 1/3
        #   b/a = 1/2

        #   a/c
        result = []
        graph = defaultdict(list)
        for index , equation in enumerate(equations):
            frum , to = equation
            graph[frum].append((to, values[index]))
            graph[to].append((frum, 1/values[index]))
        for num , denum in queries:
            if num and denum in graph:
                result.append(self.calculate(num, denum,graph))
            else:
                result.append(-1.0)
        return result
    def calculate(self,begin,target,graph):
        queue = deque([(begin, 1)])
        visited = set([begin])

        while queue:
            cur_var, value = queue.popleft()
            if cur_var == target:
                return value
            for neigh , multiplier in graph[cur_var]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh, multiplier * value))
        return -1

