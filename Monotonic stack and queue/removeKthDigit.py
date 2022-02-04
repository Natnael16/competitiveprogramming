class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        monoStack = []
        if len(num) == k:
            return "0"
        for i  in num:
            while len(monoStack) > 0 and k > 0 and monoStack[-1] > i:
                monoStack.pop()
                k -= 1
            monoStack.append(i)
        for i in range(k):
            monoStack.pop()
            
        out = ''
        
        for i in monoStack:
            out += i
        ans = out.lstrip("0")
        if len(ans) > 0:
            return ans
        else: return "0"