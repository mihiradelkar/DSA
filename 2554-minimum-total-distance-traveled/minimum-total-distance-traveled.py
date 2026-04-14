class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # robot=[0] factory=[[5,1]] slots=[5]
        # 00
        #   s-> 01 = Inf 
        #   a-> 11 = |0-5| + 0
        #   ret min(inf,5)
        robot.sort()
        factory.sort()
        slot = []
        for p,l in factory:
            slot.extend([p]*l)
        r, s = len(robot), len(slot)
        # print(robot, slot)
        # @cache
        # def dfs(i,j):
        #     # print(i,j)
        #     if i == r : return 0
        #     if j == s : return float('inf')
        #     skip = dfs(i,j+1)
        #     assign = abs(robot[i]-slot[j]) + dfs(i+1,j+1)
        #     # print(robot[i],slot[j],skip,assign)
        #     return min(skip,assign)
        # return dfs(0,0)

        #          0=2    1=2    2=6    3=6   4=ob
        #  0=0 [[4,2+2, i,2+2,   inf,   inf,  inf], 
        #  1=4  [2,2+0, 2,2+0, i,2+0, i,2+i,  inf], 
        #  2=6  [0,4+0, 0,4+0, 0,0+0, 0,0+0,  inf], 
        #  3=ob [    0,     0,     0,     0,    0]]
        dp = [[float('inf')]*(s+1) for _ in range(r+1)]
        for j in range(s+1):
            dp[r][j]=0
        for i in range(r-1,-1,-1):
            for j in range(s-1,-1,-1):
                skip = dp[i][j+1]
                assign = abs(robot[i]-slot[j]) + dp[i+1][j+1]
                dp[i][j] = min(skip,assign)
        # print(dp)
        return dp[0][0]