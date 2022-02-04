class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        di = {}
        stack = []
        for i in nums2:
            count = 0
            for j in nums2[nums2.index(i):]:
                if i < j:
                    di[i] = j
                    count += 1
                    break
            if count == 0:
                di[i] = -1
        di[max(nums2)]=-1
        di[nums2[-1]]=-1
        for i in nums1:
            stack.append(di[i])
        print(di)
        return stack