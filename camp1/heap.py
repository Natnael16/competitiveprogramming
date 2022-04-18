class Heap:
    def __init__(self):
        self.heap = []

    def getList(self):
        return self.heap
    def peek(self):
        return self.heap[0]
    def isEmpty(self):
        return not self.size
    def getSize(self):
        return len(self.heap)

    def add(self, num):
        self.heap.append(num)
        cur = len(self.heap) - 1
        parent = (cur - 1) // 2
        while parent >= 0 and self.heap[cur] > self.heap[parent]:
            self.heap[cur] , self.heap[parent]  = self.heap[parent] , self.heap[cur]
            cur = parent
            parent = (cur - 1)//2
    def remove(self):
        maxi = self.heap[0]
        self.heap[0] , self.heap[-1] = self.heap[-1] , self.heap[0]
        self.heap.pop()
        cur = 0
        left = 2 * cur + 1
        right = 2 * cur + 2
        while left < len(self.heap):
            print(left , right)
            if  right < len(self.heap) and self.heap[cur] > self.heap[left] and self.heap[cur] > self.heap[left]:
                break
            elif right < len(self.heap) and self.heap[left] > self.heap[right] :
                self.heap[cur], self.heap[left] = self.heap[left], self.heap[cur]
                cur = left

            elif right < len(self.heap) and self.heap[right] > self.heap[left]:
                self.heap[cur], self.heap[right] = self.heap[right], self.heap[cur]
                cur = right

            elif self.heap[left] > self.heap[cur]:
                self.heap[cur], self.heap[left] = self.heap[left], self.heap[cur]
                cur = left
            left = 2 * cur + 1
            right = 2 * cur + 2
        return maxi




def main():
    myHeap = Heap()
    unsorted = [2,6,7,2,6,8,1,6]
    res = []
    for i in unsorted:
        myHeap.add(i)
    print(myHeap.remove())
    print(myHeap.remove())
    print(myHeap.remove())
    print(myHeap.remove())
    print(myHeap.remove())
    print(myHeap.remove())
    print(myHeap.remove())






    print(myHeap.heap)


if __name__== '__main__':
    main()
