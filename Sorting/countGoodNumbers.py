class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        if n % 2 == 0:
            return pow(20,(n//2),(10**9 + 7))
        elif n % 2!=0: 
            n -= 1
            return (5 * self.countGoodNumbers(n))% (10**9 + 7)
        