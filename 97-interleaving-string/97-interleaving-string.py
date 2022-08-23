class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) > len(s1) + len(s2) or len(s3) < len(s1) + len(s2):
            return False
        
        @lru_cache(None)
        def isSubstring(i3 , i1 , i2):
            
            
            if i3 == len(s3) and i1 == len(s1) and i2 == len(s2):
                return True;
            if i3 ==len(s3): return False
            
            if i1 < len(s1) and i2 < len(s2) and s2[i2] == s3[i3] and s1[i1] == s3[i3]:
                return isSubstring(i3 + 1 , i1 + 1 , i2) or isSubstring(i3 + 1 , i1 , i2 + 1);
            elif i1 < len(s1) and s1[i1] == s3[i3] :
                return isSubstring(i3+1 , i1 + 1 , i2)
            elif i2 < len(s2) and s2[i2] == s3[i3]:
                return isSubstring(i3 + 1 , i1 , i2 + 1);
            else:
                return False
        return isSubstring(0 , 0 , 0)
        