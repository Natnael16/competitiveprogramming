class Solution:
    def count(self,m,n,mid):
        total = 0
        for i in range(1,m+1):
            total += min(n, mid//i)
        return total
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 1
        right = m* n
        while left < right:
            mid = left + (right - left)//2
            isGreater = self.count(m,n,mid)
            if isGreater < k:
                left = mid + 1
            else:
                right = mid
            # print(left,right)
        return right
      
      
