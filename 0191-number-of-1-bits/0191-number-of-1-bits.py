class Solution:
    def hammingWeight(self, n: int) -> int:
        shift = 1
        count = 0
        for _ in range(33):
            if shift & n:
                count += 1
            shift <<= 1
        return count