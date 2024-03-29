class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.front = 0
        self.last = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            
            self.queue[self.last] = value
            self.last = ((self.last +  1) % len(self.queue))
            # print("enqueue",self.queue, self.front, self.last)
            
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            
            self.queue[self.front] = -1
            self.front = ((self.front +  1) % len(self.queue))
            # print("dequeue",self.queue, self.front, self.last)
            return True

    def Front(self) -> int:
        return self.queue[self.front]

    def Rear(self) -> int:
        return self.queue[self.last - 1]

    def isEmpty(self) -> bool:
        if self.front == self.last and self.queue[self.front] == -1:
            return True

    def isFull(self) -> bool:
        if self.queue[self.last] == -1: return False
        else: return True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()