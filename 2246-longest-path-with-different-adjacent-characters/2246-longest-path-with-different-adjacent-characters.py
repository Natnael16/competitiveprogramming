class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for child,  par in enumerate(parent):
            tree[par].append(child)
        max_length = 1
        def maxLength(node):
            nonlocal max_length
            if not tree[node]:
                return 1
            heap = [-1,-1]
            for child in tree[node]:
                if s[child] != s[node]:
                    heappush(heap,-1*(maxLength(child) + 1))
                else:
                    maxLength(child)
            first_max= -heappop(heap)
            second_max = -heappop(heap)
            cur_max = first_max + second_max - 1
            max_length = max(max_length,cur_max)
            
            return first_max
        maxLength(0)
        return max_length
            
            