class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        target =k

        fib = [1,1]
        left , right = 0, 1
        while fib[left] + fib[right] <= target:
            fib.append(fib[left]+fib[right])
            left+=1
            right+=1
        summation = 0
        count = 0
        for i in range(len(fib)-1,-1,-1):
            while summation+fib[i] <= target:
                summation += fib[i]
                count += 1
        return count
