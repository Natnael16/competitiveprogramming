class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        loop = True
        while loop:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    loop = False
                    break
                if tickets[i] != 0:
                    tickets[i] -= 1
                    time += 1
                
        return time