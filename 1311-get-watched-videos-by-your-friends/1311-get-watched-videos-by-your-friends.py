class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = deque([id])
        lev = 0
        ans = []
        seen = {id}
        end = False
        while q:
            
            for i in range(len(q)):
                cur = q.popleft()
                
                if lev == level:
                    ans.extend(watchedVideos[cur])
                else:
                    for f in friends[cur]:
                        if f not in seen:
                            q.append(f)
                            seen.add(f)
            lev += 1
        pos = []
        counter = Counter(ans)
        for count in counter:
            heappush(pos,(counter[count] , count))
        ans = []
        while pos:
            cur = heappop(pos)
            ans.append(cur[1])
        return ans