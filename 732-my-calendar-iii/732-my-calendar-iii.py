from sortedcontainers import SortedDict


class MyCalendarThree:

    def __init__(self):
        self.events = SortedDict()

    def book(self, start: int, end: int) -> int:
        if start in self.events:
            self.events[start] += 1
        else:
            self.events[start] = 1
        if end in self.events:
            self.events[end] -= 1
        else:
            self.events[end] = -1
            
        max_booking = 0
        cur_overlapping = 0
        for time in self.events:
            cur_overlapping += self.events[time]
            max_booking = max(max_booking,cur_overlapping)
        return max_booking
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
