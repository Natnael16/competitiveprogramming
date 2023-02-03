class Solution:

    def __init__(self, w: List[int]):

        self.ranges = []
        psum = prev =  0
        # find the min and the max value using prefix sum
        for weight in w:
            psum += weight
            r =[prev,psum - 1]
            prev = psum
            self.ranges.append(r)
        self.low, self.high = 0, psum -1
        
    def pickIndex(self) -> int:
        
        # get random number in range(min,max)
        rand_num = choice(range(self.low, self.high + 1))
        
        # do binary search to get the index
        return self.getNumIndex(self.ranges, rand_num)
    def getNumIndex(self, nums,target):
        left , right = 0 , len(nums) - 1
        
        while left <= right:
            mid = (right + left)//2
            if nums[mid][0] <= target <= nums[mid][1]:
                return mid
            elif target > nums[mid][1]:
                left = mid + 1
            elif target < nums[mid][0]:
                right = mid - 1
            
        
        
            
            
            
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()