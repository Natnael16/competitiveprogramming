class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # [2,2,3,4,5] [1,2,3,4,5]
        # [1,4,5,1,2] [3,4,5,1,2]
        #initial station at -1
        # cur_gas > 0 
            #check if it has finished - exit
            #continue without changing initial station
        # else:
            # check if has finished - exit
            # initial station not found go to next one with fresh mind
        n = len(gas)
        gas = gas + gas
        cost = cost + cost
        streak = 0
        cur_gas = 0
        initial_station = 0
        for index, fuel in enumerate(gas):
            cur_gas += fuel
            cur_gas -= cost[index]
            if streak == n:
                return initial_station
            if cur_gas >= 0:
                streak += 1
            else:
                initial_station = index + 1
                cur_gas = 0
                streak = 0
        return -1



