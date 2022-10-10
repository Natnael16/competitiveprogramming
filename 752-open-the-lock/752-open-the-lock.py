class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends: return -1
        q = deque([[[0,0,0,0],0]])
        while q:
            
            lock , moves = q.popleft()
            if "".join(map(str,lock)) == target:
                
                return moves
            # print(lock)
            for i in range(4):
                for dirn in (-1,1):
                    lock[i] = (lock[i] + dirn) % 10
                    if "".join(map(str,lock)) not in deadends  :
                        q.append([lock[:],moves + 1])
                        deadends.add("".join(map(str,lock)))
                    lock[i] = (lock[i] - dirn) % 10
                    
        return -1
        
                
                