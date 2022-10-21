class RandomizedCollection:

    def __init__(self):
        self.randomSet = defaultdict(set)
        self.arr = []
        

    def insert(self, val: int) -> bool:
        flag = True
        if self.randomSet[val]:
            flag = False
        self.randomSet[val].add(len(self.arr))
        self.arr.append(val)
        return flag

    def remove(self, val: int) -> bool:
        
        if not self.randomSet[val]:
            return False
        
        del_ind = self.randomSet[val].pop()
        
        self.arr[del_ind] , self.arr[-1] = self.arr[-1] , self.arr[del_ind]
        self.randomSet[self.arr[del_ind]].add(del_ind)
        self.randomSet[self.arr[del_ind]].discard(len(self.arr) - 1)
        
        self.arr.pop()

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()