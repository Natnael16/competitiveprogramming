class Solution(object):
    def pivotIndex(self, nums):
        pre = [0]
        post = [0]
        tot1 = 0
        tot2 = 0
        for i in nums:
            tot1 = tot1 + i
            pre.append(tot1)
        for i in nums[::-1]:
            tot2 = tot2 + i
            post.append(tot2)
        for i in range(len(nums)):
            j = abs(i - len(nums))-1
            if pre[i] == post[j]:
                return i
        return -1