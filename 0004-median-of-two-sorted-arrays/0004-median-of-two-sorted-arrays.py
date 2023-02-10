class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         concatenated = sorted(nums1 + nums2) #O((n + m)log(n+m)) time and O(n + m) space
        
#         print(concatenated)
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        len1 , len2 = len(nums1) , len(nums2)
        tot_len = len1  +  len2
        half = tot_len//2
        left , right = 0, len1 - 1
        while True:
            mid = left + (right - left)//2
            second_mid = half - mid - 2
            
            leftOfOne, rightOfOne = nums1[mid] if mid >= 0 else -inf, nums1[mid + 1] if mid + 1 < len1 else inf
            leftOfTwo, rightOfTwo = nums2[second_mid] if second_mid >= 0 else -inf , nums2[second_mid + 1] if second_mid + 1 < len2 else inf
            
            if leftOfOne <= rightOfTwo and leftOfTwo <= rightOfOne:
                if tot_len % 2:
                
                    return min(rightOfOne, rightOfTwo)
                else:
                   
                    return (max(leftOfOne, leftOfTwo) + min(rightOfOne, rightOfTwo))/2
            elif leftOfOne > rightOfTwo:
                right = mid - 1
            else:
                left = mid + 1
        
              