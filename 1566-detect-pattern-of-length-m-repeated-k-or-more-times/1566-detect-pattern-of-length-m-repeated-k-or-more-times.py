class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        patterns = arr
        left = 0
        
        for right in range(m - 1 ,len(arr)):
            tl , tr = left, right
            count = 0
           
            while tr < len(arr) and patterns[left:right + 1] == patterns[tl:tr + 1]:
                count+=1
                tl = tr + 1
                tr = tr + m
        
            
            if count >= k:
                return True
            left += 1
        return False
            
        
        
        
        
        
        
        