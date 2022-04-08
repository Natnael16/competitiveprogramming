class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heapq.heapify(matrix)
        for i in range(k):
            minList = heapq.heappop(matrix)
            minNum = minList[0]
            if len(minList) > 1:
                heapq.heappush(matrix,minList[1:])
            # print(minList)
        return minNum
