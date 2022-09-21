class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        parity_sum = defaultdict(int)
        
        ans = []
        for num in nums:
            parity_sum[num % 2] += num
        for q in queries:
            num , ind = q
            num_before = nums[ind]
            cur = num_before + num
            if cur % 2 == num_before % 2:
                parity_sum[num_before % 2] += num  
            else:
                parity_sum[num_before % 2] -= num_before
                parity_sum[cur % 2] += cur
            nums[ind] = cur
            ans.append(parity_sum[0])
        return ans