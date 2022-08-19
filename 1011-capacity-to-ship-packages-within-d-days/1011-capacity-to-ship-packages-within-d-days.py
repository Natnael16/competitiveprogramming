class Solution:
    def checkDays(self, weights, weight , days):
        tot = 0
        day = 0
        for w in weights:
            tot += w
            if tot > weight:
                day += 1
                tot = 0
                tot += w
        return True if days > day else False
                
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # print(self.checkDays(weights , 2 , days))
        tot = sum(weights)
        left = max(weights)
        right = tot

        best = 0
        while left <= right:
            
            mid = left + (right - left)//2
            
            res = self.checkDays( weights ,mid , days)
            if res:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best
            
                