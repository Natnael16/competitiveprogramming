class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        concatenated = sorted(nums1 + nums2)
        n = len(concatenated)
        if n % 2 == 0:
           
            return (concatenated[n // 2] + concatenated[n // 2 - 1])/2
        else:
            return concatenated[n//2]