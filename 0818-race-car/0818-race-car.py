class Solution:
    def racecar(self, target: int) -> int:

        queue =  deque([(0,1, 0)]) # pos , speed, steps
        visited = set()
        while queue:
            
            cur_pos, cur_speed, cur_step = queue.popleft()
            if (cur_pos, cur_speed) in visited:
                continue
            visited.add((cur_pos, cur_speed))
            if cur_pos == target:
                return cur_step
            queue.append((cur_pos + cur_speed,cur_speed * 2, cur_step + 1))

            queue.append((cur_pos ,-1 if cur_speed >= 0 else 1, cur_step + 1))




