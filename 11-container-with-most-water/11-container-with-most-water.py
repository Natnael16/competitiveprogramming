class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height) -1
        maxi = -inf
        while left < right:
            maxi = max(maxi , min(height[left],height[right] ) *(right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxi