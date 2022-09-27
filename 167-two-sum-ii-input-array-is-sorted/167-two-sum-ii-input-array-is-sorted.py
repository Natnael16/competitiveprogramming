class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        def bSearch(left , right, tar):
            while left <= right:
                mid = left + (right - left )//2
                if numbers[mid] == tar:
                    return mid
                elif numbers[mid] > tar:
                    right = mid -1
                else:
                    left = mid + 1
            return -1
        for i in range(n):
            res = bSearch(i + 1, n - 1 , target - numbers[i])
            if res != -1:
                return [i + 1, res + 1]
        
                