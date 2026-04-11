class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):     # not enough gas to cover the cost
            return -1
        # total = 0
        tank = 0
        start = 0
        for i in range(len(gas)):
            net = gas[i]-cost[i]    # fuel gained - cost to go the next station
            tank += net
            # total += net
            # print(tank,start)
            if tank<0:              # tank is negative start was wrong 
                start = i+1         # start at next
                tank = 0            # reset tank
        return start # if total >=0 else -1