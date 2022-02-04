class Solution(object):
    def rotate(self, nums, k):
        if k > len(nums):
            k = k % len(nums)
        if len(nums) == 1:
            return nums
        i,j = 0,k-1
        nums.reverse()
        o,p = k,len(nums)-1
        while j>i:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1 
            j-=1
        while p>o:
            nums[o],nums[p] = nums[p],nums[o]
            o+=1 
            p-=1
        