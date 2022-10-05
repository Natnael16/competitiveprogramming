class Solution:
    def racecar(self, target: int) -> int:
        # We want to Reverse if current position is less than target and we are going backwards(s < 0) or current position in greater than target and S > 0 else we want to Accelerate
        
        q = deque([(0,1,0)]) # pos and speed
        while q:
            cur_pos , cur_speed, moves = q.popleft()
            if cur_pos == target: return moves
            
            q.append((cur_pos + cur_speed, cur_speed * 2, moves + 1))
            if (cur_pos + cur_speed< target and cur_speed < 0) or (cur_pos + cur_speed> target and cur_speed > 0):
                q.append((cur_pos,-1 if cur_speed > 0 else 1, moves + 1))
        
           
        
    
    