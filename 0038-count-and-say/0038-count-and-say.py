class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(n):
            if n == 1: return "1"
            
            say = list(helper(n - 1))
            say.append("0")
            
            count = 0
            i = 0
            out = []
            prev = say[0]
            while i < len(say):
                if say[i] == prev:
                    count += 1
                    prev = say[i]
                    i+=1
                    
                else:
                    out.append(str(count))
                    out.append(str(prev))
                    count = 1
                    prev = say[i]
                    i += 1
            say.pop()
            return "".join(out)
        return helper(n)