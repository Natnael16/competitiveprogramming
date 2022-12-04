class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = sqrt(x**2 + y**2) 
            heappush(heap, [dist ,(x,y)])
        ans = []
        while k:
            ans.append(heappop(heap)[1])
            k -= 1
        return ans