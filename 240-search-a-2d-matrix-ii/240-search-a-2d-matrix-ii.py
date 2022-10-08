class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bSearch(arr , tar , hi ,lo):
            while lo <= hi:
                mid = (hi + lo)//2
                
                if arr[mid] > tar:
                    hi = mid - 1
                elif arr[mid] < tar:
                    lo = mid + 1
                else:
                    return mid
            return -1
        for row in matrix:
            found = bSearch(row,target,len(row)-1,0)
            if found != -1:
                return True
        return False