class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        left_most_candle = []
        right_most_candle = []
        l_psum = []
        ans = []
        
        left = -1
        for ind in range(len(s)):
            if s[ind] == "|":
                left = ind
            left_most_candle.append(left)
        right = -1
        for ind in range(len(s)-1 , -1 ,-1):
            if s[ind] == "|":
                right = ind
            right_most_candle.append(right)
        right_most_candle.reverse()
        
        psum = 0 
        for i in range(len(s)):
            if s[i] == "*":
                psum += 1
            l_psum.append(psum)
        
        for left , right in queries:
            rm = right_most_candle[left]
            lm = left_most_candle[right]
            if rm == -1 or lm == -1: ans.append(0); continue

            total = l_psum[lm] - l_psum[rm]
            
            ans.append(total) if total >=0 else ans.append(0)
        return ans
            
            