class TopVotedCandidate(object):

    def __init__(self, persons, times):
        self.persons = persons
        self.times = times
        self.timeset = set(times)
        self.counter = {}
        self.counts = []
        for i in self.persons:
            self.counter[i] = self.counter.get(i, 0) + 1
            if len(self.counts) < 1:
                self.counts.append((i, self.counter[i]))
                continue
            if self.counter[i] >= self.counts[-1][1]:
                self.counts.append((i, self.counter[i]))

            else:
                self.counts.append(self.counts[-1])
        # print(self.counts)

    def q(self, t):
        if t > self.times[-1]:
            return self.counts[-1][0]

        mid = bisect.bisect(self.times, t, 1, len(self.times))
        return self.counts[mid - 1][0]
