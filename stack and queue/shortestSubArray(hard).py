import collections


class Solution:

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        psum = 0
        queue = collections.deque()
        queue.append((-1, psum))
        res = 1000000
        for i in range(len(nums)):
            psum += nums[i]
            while queue and psum - queue[-1][1] <= 0:
                queue.pop()
            while queue and psum - queue[0][1] >= k:
                res = min(res, i - queue.popleft()[0])
            queue.append((i, psum))
        # print(queue)
        if res == 1000000:
            return -1
        else:
            return res


## the first while loop to pop elements that
# decrease our prefix sum we dont want to consider
#  them when we reach our goal and finally come back to check the queue
