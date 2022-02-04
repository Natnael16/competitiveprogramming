class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        output = 0
        start = int(len(piles)/3)
        for i in range(start,len(piles),2):
            output += piles[i]
        return output