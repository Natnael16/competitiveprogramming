class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hindex = len(citations)
        leng = len(citations)
        left = 1
        right = len(citations)
        while left <= right:    
            mid = left + (right - left)//2
            if leng - mid >= citations[mid -1]:
                hindex = leng - mid
                left = mid + 1
            else:
                right = mid - 1
        return hindex
