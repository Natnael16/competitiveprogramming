class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n , m = len(s) , len(t)
        counter = Counter(t)
        tot = sum(counter.values())
        ans = (0,n + 1)
        left, right = 0, 0
        while right < n + 1: 
            if tot == 0:
                if right - left < ans[1] - ans[0]:
                    ans = (left, right)
                if s[left] in counter and counter[s[left]] >= 0:
                    counter[s[left]] += 1
                    tot += 1
                elif s[left] in counter:
                    counter[s[left]] += 1
                left += 1
            else:
                if right >= n: break
                if s[right] in counter and counter[s[right]] > 0:
                    counter[s[right]] -= 1
                    tot -= 1
                elif s[right] in counter:
                    counter[s[right]] -= 1
                right += 1
            
        return s[ans[0]:ans[1]] if ans[1] - ans[0] <= n else ""
                    
                
        
        
        
        