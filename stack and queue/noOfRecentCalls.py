class RecentCounter:

    def __init__(self):
        self.counter = []
    def ping(self, t: int) -> int:
        self.counter.append(t)
        c = 0
        # for i in self.counter:
        #     if t-3000 <= i:
        #         c+=1
        #     else:
        #         self.counter.
        while self.counter[0] < t - 3000:
            self.counter.pop(0)
        return len(self.counter)