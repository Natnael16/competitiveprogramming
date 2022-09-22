class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        inbound = lambda x : 0 <= x <= 9
        def increament(s):
            if len(s) == n: 
                self.ans.append(s)
                return
            last = int(s[-1])            
            if inbound(last + k):
                increament(s + str(last + k))
            if inbound(last - k):
                increament(s + str(last - k))
            
           
                
        self.ans = []
        for i in range(1,10):
            increament(str(i))
        return list(set(self.ans))
        
        