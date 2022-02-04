class Solution:
    def myPow( self,x, n):
        if n == 0:
            return 1
        num = abs(n)
        if n < 0:
            return 1/self.myPow(x,num)
        if num == 1:
            return x
        
        if num % 2 == 0:
            x = x*x
            num = num // 2
            return self.myPow(x,num)
        else:
            num -= 1
            return x * self.myPow(x,num)