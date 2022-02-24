import heapq


class Heap:

    def __init__(self):
        heap = []
        leng = input()
        self.numMap = {}
        for i in range(int(leng)):
            inp = input()
            inp = inp.split()
            # print(inp)
            if int(inp[0]) == 1:
                self.insert(heap, int(inp[1]))
            elif int(inp[0]) == 2:
                self.delete(heap, int(inp[1]))
            elif int(inp[0]) == 3:
                self.printMin(heap)
        # print(heap)

    def insert(self, arr, num):
        heapq.heappush(arr, num)
        # print("insert")
    def delete(self, arr, num):
        if num == arr[0]:
            heapq.heappop(arr)
        else:
            self.numMap[num] = self.numMap.get(num, 0) + 1
        while arr and arr[0] in self.numMap and self.numMap[arr[0]] > 0:
            heapq.heappop(arr)

    def printMin(self, arr):
        print(arr[0])


h = Heap()