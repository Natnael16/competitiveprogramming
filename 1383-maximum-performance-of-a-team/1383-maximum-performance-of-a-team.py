class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        sorted_ = sorted(zip(efficiency,speed), reverse= True)
        
        heap = []
        tot = 0
        ans = -inf
        for ef , sp in sorted_:
            tot += sp
            heappush(heap , (sp , ef))
            if len(heap) > k:
                smallspeed = heappop(heap)
                tot -= smallspeed[0]
            ans = max(ans , tot * ef)
        return ans % (10**9 + 7)        
        
        