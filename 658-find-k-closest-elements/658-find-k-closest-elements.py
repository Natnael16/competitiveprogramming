class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            heappush(heap, (abs(x - num) , num))
        ans = []
        while k:
            ans.append(heappop(heap)[1])
            k -= 1
        return sorted(ans)
    
            
              
            
            
            