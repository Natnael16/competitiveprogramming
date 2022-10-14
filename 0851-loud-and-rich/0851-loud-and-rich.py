class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        dp = quiet[:]
        indegree = [0] * len(quiet)
        graph_rich = defaultdict(list)
        voice_person = defaultdict(int)
        for person , v in enumerate(quiet):
            voice_person[v] = person
        for rich , poor in richer:
            graph_rich[rich].append(poor)
            
            indegree[poor] += 1
        q = deque([])
        for i , count in enumerate(indegree):
            if count == 0:
                dp[i] = quiet[i]
                q.append((i,quiet[i]))
        while q:
            cur, voice = q.popleft()
            
            for child in graph_rich[cur]:
                dp[child] = min(dp[child],dp[cur])
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append((child,quiet[child]))
        for i in range(len(dp)):
            dp[i] = voice_person[dp[i]]
        return dp