class Solution:
    def decodeString(self, s: str) -> str:
        
        def isnum(ind , s):
            res = ""
            i = ind
            num = ""
            for j in range(i , len(s)):
                if s[j].isdigit():
                     num += s[j]
                    
                else:
                    i = j +1
                    break
              
            while i < len(s):
               
                if s[i] =="[":
                    i+=1
                elif s[i].isdigit():
                  
                    new , index = isnum(i ,  s)
                    res += new
                    i = index
                elif s[i].isalpha():
                    res += s[i]
                    i += 1
                elif s[i] == "]":
                   
                   
                    return (res * int(num) if num else res , i + 1)
                    
                    
        i = 0
        out = ""
        while i < len(s):
            if s[i].isalpha():
                out += s[i]
                i+=1
            elif s[i].isdigit():
                
                fromRecur , ind = isnum(i ,s)
                out += fromRecur
                i = ind
            
        return out
            