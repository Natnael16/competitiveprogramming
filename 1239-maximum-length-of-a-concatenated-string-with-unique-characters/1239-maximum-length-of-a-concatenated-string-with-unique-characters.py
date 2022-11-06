class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr_len = len(arr)
        def max_len(ind, used):
            if ind >= arr_len:
                return 0
            if len(set(arr[ind])) != len(arr[ind]):
                return max_len(ind + 1, used)
            for char in arr[ind]:
                if used[char] > 0:
                    return max_len(ind + 1,used)
                
            for char in arr[ind]:
                used[char] += 1
                
            use = len(arr[ind]) + max_len(ind + 1,used)
            for char in arr[ind]:
                used[char] -= 1
        
            dont_use = max_len(ind + 1,used)
            return max(use, dont_use)
        return max_len(0,defaultdict(int))