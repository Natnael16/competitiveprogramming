class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_map = {0:1}
        count = 0
        pre_sum = 0
        for i in nums:
            pre_sum += i
            
            if pre_sum - k in pre_map:
                count += pre_map[pre_sum - k]
            # if pre_sum - k == 0:
            #     pre_map[0] = pre_map.get(0,0) + 1
            if pre_sum in pre_map:
                pre_map[pre_sum] += 1
            else:
                pre_map[pre_sum] = 1
            
        return count
#Do It again