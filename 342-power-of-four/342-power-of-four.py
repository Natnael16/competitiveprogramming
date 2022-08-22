class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        count = 0
        shift = 1
        for i in range(32):
            if n & shift: count += 1
            
            shift = shift << 2
        
        if count == 1:
            co = 0
            sh = 1
            for i in range(32):
                if n & sh: co += 1
                sh = sh << 1
            # print(co)
            
            if co == 1: return True