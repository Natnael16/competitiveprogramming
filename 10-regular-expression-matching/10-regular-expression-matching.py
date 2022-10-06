class Solution:
    def isMatch(self, s: str, p: str) -> bool:
    
        "abbbczc" "a.*c"
        
        len_s , len_p = len(s), len(p)
        @lru_cache(None)
        def dp(i, j):
            if i >= len_s and j >= len_p: return True
            if j >= len_p: return False
            
            match =  i < len_s and ((s[i] == p[j]) or (p[j] == "."))
            if  j + 1 < len_p and p[j + 1] == "*":
                return dp(i , j + 2) or (match and dp(i + 1 , j ) if i < len_s else dp(i , j + 2) )
            if match:
                return dp(i + 1, j + 1)
            return False
                
        return dp(0,0)