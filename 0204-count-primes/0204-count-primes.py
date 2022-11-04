class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime= [True] * (n)
        prime_count = n - 2
        
        for i in range(2,n):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    if isPrime[j] == True:
                        prime_count -= 1
                        isPrime[j] = False

        return prime_count
            
        