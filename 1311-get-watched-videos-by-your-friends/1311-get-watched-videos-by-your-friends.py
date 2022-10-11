
        
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int):
        
        visited = {id}
        q = deque([(id , 0)])
        c = Counter()
        while q:
            id_ , lev = q.popleft()
            
            if lev == level:
                for letter in watchedVideos[id_]:
                    c[letter] += 1
                continue
            for index in friends[id_]:
                if index not in visited:
                    visited.add(index)
                    q.append((index, lev + 1))
            
        return [letter for letter, count in sorted(c.items(), key = lambda x: (x[1], x[0]))]
    
    # from collections import Counter, deque
    #     visited_id = {id}
    #     deq = deque([(id, 0)])
    #     c = Counter()
    #     while deq:
    #         id, steps = deq.popleft()
    #         if steps == level:
    #             for letter in watchedVideos[id]:
    #                 c[letter] += 1
    #             continue
    #         for index in friends[id]:
    #             if index not in visited_id:
    #                 visited_id.add(index)
    #                 deq.append((index, steps + 1))
    #     return [letter for letter, count in sorted(c.items(), key = lambda x: (x[1], x[0]))]
        
        
        
        
            