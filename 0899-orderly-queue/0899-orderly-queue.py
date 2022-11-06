class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        else:
            mini_str = deque(s)
            cur_str = deque(s)
            for i in range(len(s)):
                
                first = cur_str.popleft()
                cur_str.append(first)
                
                if cur_str < mini_str:
                    mini_str = cur_str.copy()
            return "".join(mini_str)
            
        
        
        