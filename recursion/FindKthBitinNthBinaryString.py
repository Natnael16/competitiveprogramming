class Solution:
    def invert(self,s):
        s = s.replace("0","2")
        s = s.replace("1","0")
        s = s.replace("2","1")
        return s
    def reverseit(self,s):
        return s[::-1]
    def binaryString(self,n):
        if n == 1:
            return "0"
        else:
            s =  self.binaryString(n-1) + "1" + self.reverseit(self.invert(self.binaryString(n-1)))
            return s
    def findKthBit(self,n: int, k: int) -> str:
        val = self.binaryString(n)
        return val[k-1]