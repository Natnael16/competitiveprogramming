import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(nums)

        self.largest = heapq.nlargest(self.k, self.nums)
        while len(self.largest) < self.k:
            self.largest.append(-10000000)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        self.largest.append(val)
        self.largest.sort(reverse=True)
        self.largest.pop()
        # if self.k >= len(self.largest)
        # print(self.largest)

        return self.largest[-1]