class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        ans = 0
        for num in range(1, n + 1):
            digits = math.floor(math.log2(num) + 1)
            ans = ((ans << digits) + num ) %mod
            
        return ans