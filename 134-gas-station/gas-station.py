class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        # total = 0
        tank = 0
        start = 0
        for i in range(len(gas)):
            net = gas[i]-cost[i]
            tank += net
            # print(tank,start)
            if tank<0:
                start = i+1
                tank = 0
        return start