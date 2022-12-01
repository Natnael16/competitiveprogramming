class Solution:
    def largestPalindromic(self, num: str) -> str:
        def removeZeros(s):
            left , right = 0, len(s) - 1
            while left <= right:
                if s[left] != "0" and s[right] != '0':
                    return s[left: right+1]
                if s[left] == "0":
                    left += 1
                if s[right] == "0":
                    right -= 1
                
            
        count = Counter(str(num))
        s = []
        back_order = sorted(count,reverse=True)
        
        found = False
        big = False
        for num in back_order:
            if not found and  count[num] % 2:
                big = num
                found = True
            chunk = str(num * (count[num]//2)) 
            if chunk:
                s.append(chunk)
        if big:
            s.append(big)
        s += list(reversed(s[:len(s) - 1])) if big else list(reversed(s))
        res =  removeZeros("".join(s))
        return res if res else "0"
            