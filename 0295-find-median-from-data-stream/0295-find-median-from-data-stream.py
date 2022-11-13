from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.sorted_list = SortedList()

    def addNum(self, num: int) -> None:
        self.sorted_list.add(num)
    def findMedian(self) -> float:
        arr_length = len(self.sorted_list)
        if arr_length % 2:
            return self.sorted_list[arr_length//2]
        else:
            return (self.sorted_list[arr_length//2] + self.sorted_list[arr_length//2 -1])/2
       
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()