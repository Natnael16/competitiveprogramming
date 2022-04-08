import itertools

class Solution:
    def check(self, weights, days, mid):
        total = 0
        for w in weights:
          
            total += w
            if total - mid > 0:
                days -= 1
                total = w
                if days == 0:
                    break
        return days > 0
                
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # psum = list(itertools.accumulate(weights))
        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = left + (right - left)//2
            canCarryAll = self.check(weights,days,mid)
            if canCarryAll:
                best = mid
                right = mid -1
            else:
                left = mid + 1
        return best
