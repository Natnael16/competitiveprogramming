class Solution:
    def binarysearch(self , left , right , stones , target):
        l = left
        r = right
        while l <= r:
            mid = l + (r - l)//2
            if stones[mid] > target:
                r = mid - 1
            elif stones[mid] < target:
                l = mid + 1
            else:
                return (True, mid)
            
        return (False , -1)
    
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1: return False
        @lru_cache(None)
        def jump(ind , last):
            if ind == len(stones) - 1: return True
            
            one , two , three = last - 1 , last , last + 1
            
            oneBack = self.binarysearch(ind + 1 , len(stones) - 1 , stones , one + stones[ind])
            
            stay = self.binarysearch(ind + 1 , len(stones) - 1 , stones , two + stones[ind])
            
            oneForward = self.binarysearch(ind + 1 , len(stones) - 1 , stones , three + stones[ind])
            
            flag = False
            if oneBack[0]:
                flag = flag or jump(oneBack[1] , one)
            if stay[0]:
                flag = flag or jump(stay[1] , two)
            if oneForward[0]:
                flag = flag or jump(oneForward[1] , three)
                
            return flag
        return jump(1,1)

            
            