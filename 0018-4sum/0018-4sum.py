class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        out = []
        n = len(nums)
        nums.sort()
        def twosum(tar,fi,sec):
            left = sec + 1 
            right = n - 1
            
            while left < right:
                if nums[left] + nums[right] > tar:
                    right -= 1
                elif nums[left] + nums[right] == tar:
                    out.append(tuple(sorted([nums[fi],nums[sec],nums[left],nums[right]])))
                    left += 1
                else:
                    left += 1
                    
        
        for fi in range(n):
            for sec in range(fi + 1,n):
                tar = target -(nums[fi] + nums[sec])
                twosum(tar,fi,sec)
                
        return list(set(out))
