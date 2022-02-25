class Solution:

    def findSolution(self, customfunction: 'CustomFunction',
                     z: int) -> List[List[int]]:
        # a = customfuncion()
        res = []
        nums = list(range(1, 1001))
        for i in range(1, 1001):
            left = 1
            right = len(nums)
            while left <= right:
                mid = left + (right - left) // 2
                if customfunction.f(i, mid) == z:
                    res.append([i, mid])
                    break
                elif customfunction.f(i, mid) > z:
                    right = mid - 1
                elif customfunction.f(i, mid) < z:
                    left = mid + 1
        return res