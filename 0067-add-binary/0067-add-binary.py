class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #make a smaller length
        if len(b) < len(a):
            a, b = b, a
        lendiff = len(b) - len(a)
        a = ("0" * lendiff) + a # make them equal
        
        ans = []
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            carry += int(a[i]) + int(b[i])
            if carry == 0 or carry == 1:
                ans.append(str(carry))
                carry = 0
            elif carry == 2:
                ans.append("0")
                carry = 1
            elif carry == 3:
                ans.append("1")
                carry = 1
        if carry == 1:
            ans.append("1")
        return "".join(ans[::-1])
            
                
            
            
            
    
    