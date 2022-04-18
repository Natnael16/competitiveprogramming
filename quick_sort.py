import random


class Solution:

    def sortArray(self, nums):

        def quickSort(nums, start, end):
            if start >= end: return

            mid = getMiddle(nums, start, end)

            quickSort(nums, start, mid - 1)
            quickSort(nums, mid + 1, end)

        def getMiddle(nums, left, right):
            piv_ind = random.randint(left, right)

            pivot = nums[piv_ind]
            nums[piv_ind], nums[right] = nums[right], nums[piv_ind]

            target_index = left

            for ind in range(left, right):
                if nums[ind] < pivot:
                    nums[target_index], nums[ind] = nums[ind], nums[
                        target_index]
                    target_index += 1
            nums[right], nums[target_index] = nums[target_index], nums[right]

            return target_index

        quickSort(nums, 0, len(nums) - 1)
        return nums