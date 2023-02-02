class Solution:
    def numberOfWays(self, s):
        zeros, ones, zeroOnes, oneZeros, total = 0, 0, 0, 0, 0
        for char in s:
            if char == '1':
                total += oneZeros
                zeroOnes += zeros
                ones += 1
            elif char == '0':
                total += zeroOnes
                oneZeros += ones
                zeros += 1
        return total