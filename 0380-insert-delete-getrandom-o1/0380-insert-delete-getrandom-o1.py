# from random import randint
class RandomizedSet:

    def __init__(self):
        self.randomizedSet = defaultdict(int)
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.randomizedSet: 
            return False
        self.randomizedSet[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomizedSet: 
            return False
        elem_ind = self.randomizedSet[val]
        
        self.arr[elem_ind] , self.arr[-1] = self.arr[-1] ,self.arr[elem_ind]
        self.randomizedSet[self.arr[elem_ind]] = elem_ind
        del self.randomizedSet[val]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return self.arr[randint(0,len(self.arr) - 1)]
        



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()