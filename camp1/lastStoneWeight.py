class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            num1 = -(heapq.heappop(stones))
            num2 = -(heapq.heappop(stones))
            if num1 == num2:
                continue
            difference = num2 - num1 if num2 > num1 else num1 - num2
            heapq.heappush(stones,-difference)
        if not stones:
            return 0
        else:
            return -stones[0]
