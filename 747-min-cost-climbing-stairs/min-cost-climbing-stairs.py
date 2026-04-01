class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # stairs = len(cost)+1
        # dp = [0] * stairs
        # for i in range(2,stairs):
        #     dp[i] = min((dp[i-1]+cost[i-1]),(dp[i-2]+cost[i-2]))
        # return dp[stairs-1]
        
        # 
        # cost = [ 10,  15,  20 ]  E
        #         i=0  i=1  i=2  i=3  
        # prev =    0    0    0   10
        # curr =    0    0   10   15
        # dp[i]=    0    0   10   15

        prev = curr = 0
        n = len(cost)+1
        for i in range(2,n):
            curr, prev = min((curr+cost[i-1]),(prev+cost[i-2])), curr
        return curr