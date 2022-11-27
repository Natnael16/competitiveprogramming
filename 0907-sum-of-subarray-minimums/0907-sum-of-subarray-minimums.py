class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left_min = defaultdict(lambda :-1)
        right_min = defaultdict(lambda : len(arr))
        mod = 10**9 + 7
        stack = []
        for index, num in enumerate(arr):
            while stack and stack[-1][0] > num:
                pnum , pind = stack.pop()
                right_min[pind] = index
            stack.append((num, index))
        stack = []
        for index in range(len(arr) - 1, -1, -1):
            while stack and stack[-1][0] >= arr[index]:
                pnum, pind = stack.pop()
                left_min[pind] = index
            stack.append((arr[index], index))
    
        
        total = 0
        for index, num in enumerate(arr):
            left,right = index - left_min[index] - 1,right_min[index] - index - 1
            total += (left * right) * num
            total += (left) * num
            total += (right) * num
            total += num
        return total % mod
            