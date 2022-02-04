class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [-1]*k

    def insertFront(self, value: int) -> bool:
        if self.deque[-1] != -1:
            return False
        else:
            for i in self.deque:
                if i == -1:
                    ind = self.deque.index(i)
            for i in range(ind,0,-1):
                self.deque[i] = self.deque[i-1]
            self.deque[0] = value
            return True

    def insertLast(self, value: int) -> bool:
        if self.deque[-1] != -1:
            return False
        else:
            for i in range(len(self.deque)):
                if self.deque[i] == -1:
                    self.deque[i] = value
                    return True
                    

    def deleteFront(self) -> bool:
        if self.deque[0] != -1:
            self.deque = self.deque[1:]
            self.deque.append(-1)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        count = 0
        for i in range(len(self.deque)-1,-1,-1):
            if self.deque[i] != -1:
                self.deque[i] = -1
                count += 1
                break
        if count == 0:
            return False
        else: return True

    def getFront(self) -> int:
        return self.deque[0]
        
    def getRear(self) -> int:
        for i in range(len(self.deque)-1,-1,-1):
            if self.deque[i] != -1:
                return self.deque[i]
                break
        return self.deque[-1]

    def isEmpty(self) -> bool:
        count = 0
        for i in self.deque:
            if i != -1:
                count += 1
        if count == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.deque[-1] != -1:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()