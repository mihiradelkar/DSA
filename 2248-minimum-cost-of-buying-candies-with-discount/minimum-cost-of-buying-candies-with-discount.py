class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        total = 0
        cost.sort(reverse=True)
        # print(cost)
        for i, c in enumerate(cost):
            if i%3==2:
                continue
            total+=cost[i]
        return total
        