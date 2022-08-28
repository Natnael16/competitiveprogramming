class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        heapdict = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                heappush(heapdict[row - col] , mat[row][col])
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                mat[row][col] = heappop(heapdict[row - col])
        return mat